import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the prompt with a few examples
prompt = """
You are an AI assistant that can answer questions based on the provided context. Here are some examples:

Context: The quick brown fox jumps over the lazy dog.
Question: What color is the fox?
Answer: The fox is brown.

Context: Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversations?'
Question: Who was Alice sitting with?
Answer: Alice was sitting with her sister.

Context: In the United States, the president is the head of the executive branch of the federal government and is elected to a four-year term by the people through an Electoral College. The president is responsible for implementing and enforcing the laws written by Congress and, to that end, appoints the heads of the federal agencies, including the Cabinet.
Question: What is the role of the president in the United States?
Answer:

Context: [CONTEXT]
Question: [QUESTION]
Answer:
"""

# Get the context and question from the user
context = input("Enter the context: ")
question = input("Enter your question: ")

# Construct the final prompt with the user input
final_prompt = prompt.replace("[CONTEXT]", context).replace("[QUESTION]", question)

# Generate the answer using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=final_prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated answer
print(response.choices[0].text.strip())
