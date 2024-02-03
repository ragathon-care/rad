

while True:
    try:
        text_input = input("User: ")
        if text_input == "exit":
            break
        response = agent.chat(text_input)
        print(f"Agent: {response}")
    except KeyboardInterrupt:
        # quit
        sys.exit()