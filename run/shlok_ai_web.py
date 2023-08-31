import openai
import json
import logging
import datetime
from Common.utils import KeyFetcher
from Common.utils import CostCalculator

# # Set up logging
# log_filename = 'shlokai.log'
# logging.basicConfig(filename=log_filename, level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Set up logging
# log_filename = 'shlokai_debug.log'
# logging.basicConfig(filename=log_filename, level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

def shlokAI(user_prompt):
    # user_query = prompt
    keyfetch = KeyFetcher()
    openai.api_key = keyfetch.getOpenAIApiKey()
    logging.debug("OpenAI API Key: %s", openai.api_key)
    messages = []
    model = "gpt-3.5-turbo"
    tokens_used = 0
    # Prepare ShlokAI
    shlok_ai_instructions = f"""
    You are a practising Hindu scholar in Sanskrit well versed in Vedic Dharma. You are well versed in all the sacred scriptures such as \
    Bhagavat Gita, Puranas, Vedas, Stotras, Upanishads, 4000 Divya Prabandham, etc., as well as all forms of Yogic practices. \
    I will be asking you the meaning of any verse and would like you to give me an easy to understand explanation. 

    Output format in IETF RFC 8259 JSON specification:
    - Verse in English        
    - Verse in Sanskrit
    - Verse in Tamil
    - Meaning 
    - Relevance
    - Context
    - Usage
    - Source
    - Author of Source
    - Generic Explanation

    Follow the below conditions step by step, while providing the output:
    1. If the question is too generic or unrelated to India, Bharat, Yoga, Vedic, Spirituality, Hinduism, Culture etc., please respond with the message: \
    <"Error":"I am unable to provide an explanation for this query. Please ask a question related to Bharat, Yoga, Spirituality, Hindu Philosophy, Culture etc.">
    2. There must be no extra text except for what the output format requires.
    3. If any value for the required keys is not available, do not add the key in the JSON output.
    4. If you are unable to provide an explanation for an input for any other reason, please output response in IETF RFC 8259 JSON specification \
    <"Error":"reason for error">
    5. Do not provide any disclaimers that you are not a scholar in the subject.
    """

    # Set user submitted query
    user_prompt = user_prompt
    logging.info("User Prompt: %s", user_prompt)
    shlok_ai_prompt = f"""
    Follow the instructions delimited by triple backticks step by step. \
    Instructions: ```{shlok_ai_instructions}``` \
    Respond to user query delimited by angle brackets: <{user_prompt}>"""
    # print("ShlokAI Prompt: ", shlok_ai_prompt)
    # Query the model
    messages = [{"role": "user", "content": shlok_ai_prompt}]
    response_raw = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        # stream=True
    )
    
    query_response = response_raw.choices[0].message["content"]
    logging.info("Query Response: %s", query_response)
    # response_content = ''.join(response_raw).strip()
    # print("response_content:", response_content)
    tokens_used = tokens_used + response_raw.usage["total_tokens"]

    try:
        json.loads(query_response)
    except Exception as e:
        logging.info("Response is not in proper JSON format. Please try again.")
        logging.error("Error: %s", e)
        return json.dumps({"Error": e})
    
    shlokai_output = json.loads(query_response)

    for key in shlokai_output:
        logging.debug("%s: %s", key, shlokai_output[key])

    # Instantiate CostCalculator
    costcalc = CostCalculator(tokens_used, model)
    cost = costcalc.calculateCost(tokens_used, model_name=model)
    logging.debug("Cost: US$ %s", cost)
    return query_response

# if __name__ == "__main__":
#     shlokAI(prompt)
