from app.chatbot import Chatbot

def main():
    print("Welcome to the chatbot! Type 'exit' to quit.\n")

    system_prompt = (
        "This conversation must be family friendly. Avoid using profanity, or being rude. "
        "Be courteous and use language which is appropriate for any audience. Avoid NSFW content. ###"
    )

    user_name = "User"
    bot_name = "Bot"
    chat_history = []
    api_url = "http://guanaco-submitter.guanaco-backend.k2.chaiverse.com/endpoints/onsite/chat"
    headers = {
        "Authorization": "Bearer CR_14d43f2bf78b4b0590c2a8b87f354746",
        "Content-Type": "application/json"
    }

    bot = Chatbot(
        user_name=user_name,
        bot_name=bot_name,
        system_prompt=system_prompt,
        chat_history=chat_history,
        api_url=api_url,
        headers=headers
    )

    print(f"{bot_name}: Hi there!")
    bot.chat_history.append({"sender": bot_name, "message": "Hi there!"})

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print(f"{bot_name}: Goodbye!")
            break

        response = bot.get_response(user_input)
        print(f"{bot_name}: {response}")

if __name__ == "__main__":
    main()
