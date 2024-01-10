

def write_to_file(lines='', filetype='txt'):

    from Comms import speak, listen
    from fileutils import camel_case

    print(filetype, lines)
    speak(f"Do you want me to write the response to a file?")
    file_write = listen()
    while 'yes' not in file_write and 'no' not in file_write:
        speak("I am sorry. Do you want me to write the response to a file")
        file_write = listen()
    if 'yes' in file_write:
        speak("What filename would you like me to give it?")
        while True:
            try:
                filename = camel_case(listen())
                with open(filename + '.' + filetype, 'w') as f:
                    f.write(lines)
                return lines
            except:
                speak("Please say the filename again.")
                continue
    return lines


# if __name__ == '__main__':
#     write_to_file('test', 'py')


