import ChatBot


# Create a new instance of a ChatBot
bot = ChatBot('Example Bot')

# Train the chatbot based on the english corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Get a response for some initial input
print(bot.get_response("Hello, how are you?"))

while True:
    try:
        user_input = input("User: ")
        bot_response = bot.get_response(user_input)
        print(f"Bot: {bot_response}")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
