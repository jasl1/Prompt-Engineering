import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the prompt with a chain-of-thought example
prompt = """
Question: There are 15 bats on the ground. Some go up a tree. Now there are 10 bats left on the ground. How many bats went up the tree?

Chain of Thought:
1) Initially, there were 15 bats on the ground.
2) After some bats went up the tree, there were 10 bats left on the ground.
3) To find how many bats went up the tree, we need to subtract the number of bats left on the ground from the initial number of bats.
4) 15 - 10 = 5
5) Therefore, 5 bats went up the tree.

Answer: 5 bats went up the tree.

Question: There are 25 birds in a tree. Some fly away. Now there are 15 birds left in the tree. How many birds flew away?

Chain of Thought:
"""

# Generate the chain-of-thought response using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.7,
)

# Print the generated chain-of-thought response
print(response.choices[0].text.strip())
