from chatterbot import ChatBot

chat_bot = ChatBot("Bett")

exit_cond = (":q","quit","exit","Exit", "Quit")

while True:
    query = input("> ")
    if query in exit_cond:
        break
    else:
        print(f"🪴 {chat_bot.get_response(query)}")