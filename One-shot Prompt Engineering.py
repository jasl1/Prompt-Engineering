import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the prompt with a single example
prompt = """
Summarize the following text in one sentence:

Example:
The quick brown fox jumps over the lazy dog. The dog wakes up and chases the fox away.

Summary: A quick fox jumps over a lazy dog, which then chases the fox away.

Text:
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?'
"""

# Generate the summary using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated summary
print(response.choices[0].text.strip())
