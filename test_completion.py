import os
import openai

from dotenv import load_dotenv

load_dotenv()


def init():
    openai.organization = os.getenv("OPENAI_ORGANIZATION")
    openai.api_key = os.getenv("OPENAI_API_KEY")


def print_models():
    print(openai.Model.list())


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal: {}
    Names:""".format(
        animal.capitalize()
    )


def birthday_survey():
    return """
    Create a birthday RSVP form for Shawn's birthday
    """


def mine_sweeper():
    return """
    Create a Python program of the game Mine Sweeper. The program is to be run in a terminal.
    """

def main():
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=birthday_survey(),
            max_tokens=1000,
            temperature=0, # randomness. 0 - identical result every time
        )
    print(response)
    

if __name__ == "__main__":
    init()
    main()