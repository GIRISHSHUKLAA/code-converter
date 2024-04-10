import google.generativeai as genai
import textwrap
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key='')  # Default API key, should be replaced by user input

model = genai.GenerativeModel('gemini-pro')

def code_converter(source_code, source_language, target_language):
    prompt = f"Convert the following code from {source_language} to {target_language}:\n\n{source_code}"
    response = model.generate_content(prompt)
    converted_code = response.text
    return converted_code
