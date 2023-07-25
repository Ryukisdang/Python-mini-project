import random

# List of possible greetings from the friend chatbot
greetings = ["Hello!", "Hi there!", "Hey, how can I help you?", "Greetings!"]

# List of possible responses to questions
responses = [
    "I'm glad you asked! The answer is...",
    "Oh, that's an interesting question. Let me think... The answer is...",
    "I happen to know the answer! It's...",
    "I've got the answer right here! It's..."
]

# List of possible farewell messages
farewells = ["Goodbye!", "Farewell!", "Have a great day!", "See you later!"]

# Function to generate a response to user input
def generate_response(user_input):
    # Generate a random response from the list of possible responses
    random_response = random.choice(responses)
    return f"{random_response} {user_input}."

# Start the conversation
print(random.choice(greetings))

# Keep the conversation going until the user decides to exit
while True:
    user_input = input("> ")
    
    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print(random.choice(farewells))
        break
    
    # Generate and print a response
    response = generate_response(user_input)
    print(response)
