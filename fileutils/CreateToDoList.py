

def create_to_do_list():
    from Comms import speak, listen
    from fileutils import write_to_file

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

