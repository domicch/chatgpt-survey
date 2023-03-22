import os
import openai
import json
import time

from dotenv import load_dotenv

load_dotenv()


def init():
    openai.organization = os.getenv("OPENAI_ORGANIZATION")
    openai.api_key = os.getenv("OPENAI_API_KEY")


def print_models():
    print(openai.Model.list())



def json_file_2_escaped_text(filename: str) -> str:
    with open(filename, 'r') as fp:
        data = json.load(fp)
        return json.dumps(json.dumps(data))


def escaped_text_2_json_file(escaped_text: str, filename: str):
    with open(filename, "w") as fp:
        data_dict = json.loads(escaped_text)
        json.dump(data_dict, fp, indent=4)


def write_dict_to_file(data: dict, filename: str):
    with open(f"response/{filename}_{int(time.time())}", "w") as fp:
        json.dump(data, fp, indent=4)


def escaped_json_2_dict(escaped_text: str) -> dict:
    return json.loads(json.loads(escaped_text))


def template_messages():
    return [
        {
            "role": "user",
            "content": "Generate a birthday RSVP form for my son Shawn's birthday in JSON format"
        },
        {
            "role": "system",
            "content": json_file_2_escaped_text("samples/sample_birthday_rsvp.json")
        },
    ]


def get_user_message(question: str) -> dict:
    return {
        "role": "user",
        "content": question
    }


def main():
    messages = template_messages()
    # e.g. "Generate a survey RSVP form about feedback of my job performance as a software engineer"
    question = input()
    messages += [get_user_message(question)]

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,
            temperature=0, # randomness. 0 - least variations on results
        )
    print(response)
    
    output = {
        "question": question,
        "response": response
    }
    write_dict_to_file(output, "response")
    write_dict_to_file(escaped_json_2_dict(response["choices"][0]["message"]["content"]), "content")



if __name__ == "__main__":
    init()
    main()
