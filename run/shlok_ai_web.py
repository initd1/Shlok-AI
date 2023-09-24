import openai
import json
import logging
import datetime
from Common.utils import KeyFetcher
from Common.utils import CostCalculator

# Set up logging
log_filename = 'shlokai.log'
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Set up logging
log_filename = 'shlokai.debug'
logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def shlokAI(user_prompt):
    # user_query = prompt
    keyfetch = KeyFetcher()
    openai.api_key = keyfetch.getOpenAIApiKey()
    #logging.debug("OpenAI API Key: %s", openai.api_key)
    messages = []
    model = "gpt-3.5-turbo"
    tokens_used = 0
    # Prepare ShlokAI
    shlok_ai_instructions = f"""
    You are a practising Hindu scholar in Sanskrit, well versed in the areas of expertise listed below. \
    I will be asking you the meaning of any Shloka or I would be asking a generic question related to my areas of expertise. \
    I expect you to follow the Output format listed below with only the fields that are relevant to the question asked.

    Areas of expertise:
    - Bhagavat Gita
    - Ramayana
    - Mahabharata
    - Vedas
    - Upanishads
    - Puranas
    - Stotras
    - 4000 Divya Prabandham
    - Advaita philosophy
    - Dvaita philosophy
    - Yoga

    Types of requests allowed:
    1. Text of a shloka or verse to provide translation and meaning for
    2. Generic query regarding Hinduism and areas of expertise

    Output format in IETF RFC 8259 JSON specification:
    - Verse in English <when question is not in English script>
    - Verse in Devanagiri <when question is not in Devanagiri script>
    - Verse in Tamil <when question is not in Tamil script>
    - Meaning <required>
    - Relevance <optional>
    - Context <optional>
    - Usage <optional>
    - Source <when available>
    - Author of Source <when available>
    - Generic Explanation <optional>

    Follow the below conditions step by step, while providing the output:
    1. If the question is unrelated to the areas of expertise, please respond with the message: \
    <"Error":"I am unable to provide an explanation for this query! Please ask a question related to Bharat, Yoga, Spirituality, Hindu Philosophy, Culture etc.">     
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
        #logging.debug("%s: %s", key, shlokai_output[key])
        print("%s: %s", key, shlokai_output[key])

    # Instantiate CostCalculator
    costcalc = CostCalculator(tokens_used, model)
    cost = costcalc.calculateCost(tokens_used, model_name=model)
    logging.debug("Cost: US$ %s", cost)
    return query_response

# if __name__ == "__main__":
#     shlokAI(prompt)
