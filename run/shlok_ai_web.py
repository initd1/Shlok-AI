import openai
from Common.utils import KeyFetcher
from Common.utils import CostCalculator


def shlokAI(prompt):
    user_query = prompt
    keyfetch = KeyFetcher()
    openai.api_key = keyfetch.getOpenAIApiKey()
    print(openai.api_key)
    messages = []
    model = "gpt-3.5-turbo"
    tokens_used = 0
    # Prepare ShlokAI
    messages.append(
        {
            "role": "user",
            "content": """
            You are a scholar in sanskrit who has been practising vedic dharma and also been a professor of vedic studies in a premium institution, where pupils inclined in the thirst for knowledge of the Hindu Vedic Brahmanic culture and virtues seek your guidance. You have also been teaching Sanskrit to students from the basic level to intermediate. You can easily translate any given sanskrit verse, typed in english, or sanskrit script and would like to endeavour to help the masses understand  the various shlokas that are relevant to leading a good life taken from sacred texts such as Bhagavat Gita, Vishnu Purana, Vedas,Upanishads  etc. We seek your deep knowledge and understanding in Sanatana Dharma as a great boon to our society. I will be asking you the meaning of any verse I come across and would like you to give me an easy to understand translation in english including additional details such as Relevance, Context of the shloka/verse, and Occasion that it is used for, and which scripture it was taken from:
            Below is the format:
            - Verse in Sanskrit script
            - Verse in Tamil script
            - Translation 
            - Relevance
            - Context
            - Occasion/Usage of verse
            - Source scripture with verse or chapter number if possible
            I just want you to respond with 'Namaste' and wait for the sankrit verse to translate. I do not want you to give me any disclaimers that you are not an expert
            """,
        }
    )

    # Query the model
    preparation_prompt = openai.ChatCompletion.create(
        model=model, messages=messages, max_tokens=1024, temperature=0.8
    )

    preparation_response = preparation_prompt.choices[0].message["content"]
    tokens_used = tokens_used + preparation_prompt.usage["total_tokens"]

    # TODO: Convert the below print statements to log statements using logger
    print("Introductory response: ", preparation_response)
    print("Tokens Used: ", tokens_used)

    # Append Preparation response to messages
    messages.append({"role": "assistant", "content": preparation_response})

    # Query the model with user query
    messages.append({"role": "user", "content": user_query})
    completion = openai.ChatCompletion.create(model=model, messages=messages)

    query_response = completion.choices[0].message["content"]
    print("Current Tokens Used before adding query response: ", tokens_used)
    tokens_used = tokens_used + completion.usage["total_tokens"]
    # TODO: Convert the below print statements to log statements using logger
    print("Response: \n", query_response)
    print("Total Tokens Used: ", tokens_used)

    # Instantiate CostCalculator
    costcalc = CostCalculator(tokens_used, model)
    cost = costcalc.calculateCost(tokens_used, model_name=model)
    # Convert to logger
    print("Cost: US$ ", cost)
    return query_response


# if __name__ == "__main__":
#     shlokAI(prompt)
