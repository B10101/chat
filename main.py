from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from clean import clean

file = "text.txt"
chat_bot = ChatBot("Bett")

trainer = ListTrainer(chat_bot)
cleaned = clean(file)
trainer.train(cleaned)

exit_cond = (":q","quit","exit","Exit", "Quit")
while True:
    query = input("> ")
    if query in exit_cond:
        break
    else:
        print(f"🪴 {chat_bot.get_response(query)}")