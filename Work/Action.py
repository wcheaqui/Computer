

# Define a function to perform actions based on user input
def perform_action(command, file='', old_file_path='', directory='', new_name=''):
    from fileutils import write_to_file, camel_case, snake_case, string_list, search_files, start_project, set_timer
    from Comms import chatgpt, test_chat_gpt, get_weather, speak, listen

    import os
    import shutil

    import subprocess
    import asyncio

    if 'jupiter' in command.lower():
        try:
            subprocess.run(['jupyter', 'notebook'], check=True)
        except subprocess.CalledProcessError as e:
            print("Error:", e)

    # Check if the command is a timer request
    elif 'timer' in command.lower():

        # Extract the time amount and reminder text from the command
        time_amount = 0
        if 'for' in command and 'minute' in command:
            time_amount = int(command[command.index("for") + 3:].split()[0])

        while time_amount == 0:
            speak("how long would you like the timer for")
            # try:
            time_amount = int(listen())
            # except Exception as e:
            #     print(e)
            #     continue

        # extract reminder text from command
        if 'reminder text' in command.lower():
            reminder_text = command[command.lower().index("reminder text") + 3:].split()[0]
        else:
            reminder_text = 'Reminder1'

        # Set the timer using the extracted values
        asyncio.create_task(set_timer(time_amount, reminder_text))

    elif "to-do list" in command:
        speak(f"What are the tasks you want to add to the to-list? Say Stop when finished")
        tasks = []
        while True:
            task = listen()
            if 'stop' in task:
                break
            tasks.append(task)
        speak("To-do list created. Here's your to-list:")
        print(tasks)
        speak("would you like me to save this list?")
        if 'yes' in listen():
            tasks_string = ''
            for i in tasks:
                tasks_string = tasks_string + i + '\n'
            write_to_file(lines=tasks_string)
            return tasks
        return tasks

    # write a prompt for chatgpt
    elif "question" in command.lower():
        speak("How can I assist you?")
        question = listen()
        speak("Is this related to another conversation, if so what")
        seearch_query_question = listen()
        if 'no' not in seearch_query_question:
            response = test_chat_gpt(question, search_query=seearch_query_question)
        else:
            response = test_chat_gpt(question)
        write_to_file(lines=response)

    elif 'python' in command.lower() and 'function' in command.lower():
        speak("what would you like the function to do")
        func = listen()

        parameters = ''
        speak("Any parameters you would like it to have")
        parameters_question = listen()
        if 'no ' not in parameters_question:
            parameters = 'and takes the following parameters ' + string_list(parameters_question)

        speak("Would you like name the function, is so what?")
        func_name_question = listen()

        func_name = ''
        if 'something' not in func_name_question and 'no' not in func_name_question:
            func_name = f'called {snake_case(func_name_question)}'

        prompt = f"create a function {func_name} that {func} {parameters}: {file}"

        response = chatgpt(prompt=prompt, code_only=True)

        write_to_file(lines=response, filetype='py')

    elif 'python' in command and 'class' in command:
        speak("what are you creating a class for?")
        class_create = listen()
        speak("what class will it have any inheritance?")
        inheritance = listen()

        if 'no ' not in inheritance and 'none' not in inheritance:
            inheritance = f' and the class should inherit the following classes ' + string_list(inheritance)

        speak("Would you like to name the class?")
        class_name_question = listen()

    elif 'query' in command:
        speak("what would you like the query to do")
        query = listen()

        prompt = f"create a sql query that {query}"

        response = chatgpt(prompt=prompt, code_only=True, is_type='query')

        write_to_file(lines=response, filetype='sql')

    elif 'look' in command and 'file' in command or \
            'search' in command and 'file' in command:

        search_files(command=command)

    elif 'move' in command:
        command_later = ''
        if old_file_path == '':
            if 'put' in command:
                command_later = command[command.index("put"):]
                command = command[:command.index("put")]
            search_files(command)
            if command_later != '':
                command = command_later

        else:
            speak(f'where would you like me to put {old_file_path}')
            command = listen()
        search_files(command=command, directory_only=True)
        shutil.move(old_file_path, directory)

    elif 'copy' in command:
        if old_file_path == '':
            speak("which file would you like me to move")
            old_file_path = listen()
            search_files(old_file_path)

            speak(f'where would you like me to put {old_file_path}')
            command = listen()

        directory = ''
        while directory == '':
            if 'utility' in command:
                shutil.copy(old_file_path, os.getcwd() + '/fileutils/')
            elif 'download' in command:
                shutil.copy(old_file_path, '/Users/WCheaq/Downloads/')
            elif 'desktop' in command:
                shutil.copy(old_file_path, '/Users/WCheaq/Desktop/')
            elif 'work' in command:
                shutil.copy(old_file_path, os.getcwd() + '/Work/')
            elif 'current directory' in command or 'here' in command:
                shutil.copy(old_file_path, os.getcwd() + '/')
            else:
                speak("I did not find that directory. What was it again?")
                command = listen()

    elif 'rename' in command and 'file' in command:
        new_file_name = ''
        agreeable_name = 'no'
        while agreeable_name != 'yes':
            speak("what would you like to name it?")
            new_file_name = camel_case(listen())
            speak(f"is the {new_file_name} Satisfactory to you?")
            agreeable_name = listen()
        shutil.move(old_file_path, new_file_name)

    elif 'start' in command and 'project' in command:
        start_project()

    elif 'weather' in command:
        get_weather()

    elif 'print' in command:
        import subprocess

        file_path = old_file_path
        printer_uri = 'ipp://BRW900F0C9ED286.local:631/ipp/print'

        subprocess.run(['lpr', '-P', printer_uri, file_path])

    elif (('create' or 'make') and ('directory' or 'folder')) in command:

        if (directory or new_name) == '':
            search_files(command=command, directory_only=True)
        try:
            os.mkdir(directory + camel_case(new_name))
        except FileExistsError:
            speak("Folder already exists")

    else:
        speak("Sorry, I did not understand that command.")


perform_action("hey Jarvis let's set a timer")
