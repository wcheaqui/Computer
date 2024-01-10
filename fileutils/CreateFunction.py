

def create_function(file=''):
    from Comms import speak, listen, chatgpt
    from fileutils import write_to_file, string_list, snake_case

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