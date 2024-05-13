import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the prompt with a few examples
prompt = """
Translate the following sentences from English to French:

English: Hello, how are you?
French: Bonjour, comment allez-vous?

English: I am doing well, thank you.
French: Je vais bien, merci.

English: What is your name?
French:

English: My name is John.
French:
"""

# Generate the translation using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated translation
print(response.choices[0].text.strip())
