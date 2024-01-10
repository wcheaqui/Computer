

def create_sql_query(command):
    from Comms import speak, listen, chatgpt
    from fileutils import write_to_file

    speak("what would you like the query to do")
    query = listen()

    prompt = f"create a sql query that {query}"

    response = chatgpt(prompt=prompt, code_only=True, is_type='query')

    write_to_file(lines=response, filetype='sql')