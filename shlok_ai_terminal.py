import openai
from Common.utils import KeyFetcher
from Common.utils import CostCalculator


def shlokAI(prompt):
    user_query = prompt
    keyfetch = KeyFetcher()
    openai.api_key = keyfetch.getOpenAIApiKey()
    print(openai.api_key)
    messages = []
    prompt_training_count = 0
    loop_count = 0
    while True:
        if loop_count == 0:
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
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1024,
                temperature=0.8,
            )

            response = preparation_prompt.choices[0].message["content"]
            print("Introductory response: ", response)
            print("Tokens Used: ", preparation_prompt.usage["total_tokens"])

            messages.append({"role": "assistant", "content": response})
            # print("Current message: ", messages[0])
            # print("\n\nNext message: ", messages[1])
            loop_count += 1
        # Until 2 iterations, no need to remind the AI of it's purpose
        elif loop_count <= 2:
            # prompt = input('\nAsk a question: ')
            messages.append({"role": "user", "content": user_query})
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            print("Response: \n", completion.choices[0].message["content"])
            print("Tokens Used: ", completion.usage["total_tokens"])
            messages.append({"role": "assistant", "content": response})

            # Reset the loop count when it reaches 5, so that the model can be reminded of it's purpose
            # User can continue asking questions

            # Thoughts: It doesn't remember the original instruction, so may have to reduce the count to 2 or 3 and increase the max_tokens
            # in the query
            if loop_count == 2:
                print("You have asked 2 questions, please wait for the AI to respond")
                loop_count = 0
                print("Exiting the program")


if __name__ == "__main__":
    shlokAI()
