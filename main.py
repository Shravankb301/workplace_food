# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install -r requirements.txt

from dotenv import load_dotenv
import os

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
load_dotenv()
# Access the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
#     print(m.name)

# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("What is the meaning of life?")

model = genai.GenerativeModel('gemini-1.5-flash')


feedback = "can you name dog names"
response = model.generate_content(feedback)
# print (response)
to_markdown(response.text)

