

def ask_jarvis():

        from Comms import speak, listen, test_chat_gpt
        from fileutils import write_to_file

        speak("How can I assist you?")
        question = listen()
        speak("Is this related to another conversation, if so what")
        seearch_query_question = listen()
        if 'no' not in seearch_query_question:
            response = test_chat_gpt(question, search_query=seearch_query_question)
        else:
            response = test_chat_gpt(question)
        write_to_file(lines=response)



