import signal, sys, json
import logging
import openai
import configparser
from Common.utils import KeyFetcher
from Common.utils import CostCalculator


def signal_handler(signal, frame):
    print("You have requested to exit the program using Ctrl+C. Exiting.")
    logging.info("You have requested to exit the program using Ctrl+C. Exiting.")
    sys.exit(0)

def shlokAI():
    keyfetch = KeyFetcher()
    openai.api_key = keyfetch.getOpenAIApiKey()
    while True:
        shlok_ai_instructions = f"""
        You are a practising Hindu scholar in Sanskrit well versed in Vedic Dharma. You are well versed in all the sacred scriptures such as \
        Bhagavat Gita, Puranas, Vedas, Stotras, Upanishads, 4000 Divya Prabandham, etc. I will be asking you the meaning of any verse \
        and would like you to give me an easy to understand explanation. 

        Only respond with the message: \"Namaste, I am ready to help you with your query regarding any Shloka\".                                                       

        Output format in JSON:
        - Verse in English script        
        - Verse in Sanskrit script
        - Verse in Tamil script
        - Translation 
        - Relevance
        - Context
        - Usage of Verse
        - Source Scripture with Verse or Chapter Number if available.
        - Author

        Follow the below conditions step by step, while providing the output:
        1. If the question is too generic or unrelated to India, Bharat, Vedic, Spirituality, Hinduism, Culture etc., please respond with the message: \
        <I am unable to provide an explanation for this query. Please ask a question related to India, Bharat, Vedic, Spirituality, Hinduism, Culture etc.>
        2. There must be no extra text except for what the output format requires.
        3. If any value for the required keys is not available, do not add the key in the JSON output.
        4. If you are unable to provide an explanation for an input, please output response in JSON format with the key \"Error\" and explain \
        why you are unable to provide an explanation.
        5. Do not provide any disclaimers that you are not a scholar in the subject.
        """

        user_prompt = input("\nAsk a question: ")
        # messages.append({"role": "user", "content": user_prompt})
        # print(messages)
        prompt = f"""
        Follow the instructions delimited by triple backticks step by step. \
        Instructions: ```{shlok_ai_instructions}``` \
        Respond to user query delimited by angle brackets: <{user_prompt}>
        """

        # Query the model
        messages = [{"role": "user", "content": prompt}]
        response_raw = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
            stream=True
        )
        # Stream output as it's generated
        # create variables to collect the stream of chunks
        collected_chunks = []
        collected_messages = []
        for chunk in response_raw:
            try: 
                content = chunk["choices"][0]["delta"]["content"]
                if content:
                    collected_chunks.append(content)
                    # Do not print every chunk in new line
                    print(content, end="", flush=True)
            except:
                pass
        print(collected_chunks)
        # Strip extra characters from final output        
        response_content = ''.join(collected_chunks).strip()
        print(response_content)
        print("Tokens used for this prompt: ", response_raw.usage["total_tokens"])

        # Check if response_content is proper json format
        try:
            json.loads(response_content)
        except:
            print("Response is not in proper JSON format. Please try again.")
            continue
        
        shlokai_output = json.loads(response_content)
        
        # Separate output into different variables if required for front end
        # if shlokai_output["Relevance"]:
        #     print(shlokai_output["Relevance"])
        # else:
        #     pass

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    shlokAI()
