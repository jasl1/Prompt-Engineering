import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the prompt without any examples
prompt = """
Translate the following sentence from English to Spanish:

The cat is sleeping on the couch.
"""

# Generate the translation using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated translation
print(response.choices[0].text.strip())
