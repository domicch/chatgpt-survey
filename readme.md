# Generating Determinstic Survey from ChatGPT

## How to use
1. Install Python

2. Install python dependencies
```shell
pip isntall openai
pip install python-dotenv
```

3. Create a .env file (refer to .env.sample)

4. Run the program
```shell
python test_chat.py

Generate a survey RSVP form about feedback of my job performance as a software engineer
```

5. Response will be written to `response` folder


## How does it work?
In essence, we have to give a sample to ChatGPT about our expected format. In this simple example we give it the `sample_birthday_rsvp.json` as the expected format, and ask it to generate a similar survey in a different context. I believe we can play around with more complex samples and see how it performs.