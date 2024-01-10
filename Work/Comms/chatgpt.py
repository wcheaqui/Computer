
def test_chat_gpt(prompt, user_name='Will', bot_name='Jarvis', code_name='python', code_only=False, is_type='function',
                  search_query=None, search_convo=None, model="text-davinci-003", temperature=0.7, max_tokens=1000,
                  top_p=1, frequency_penalty=0, presence_penalty=0):
    import json

    import openai
    import configparser
    from Speak import speak

    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        api_key = config['chatgpt'].get('api_key')
    except KeyError:
        raise ValueError("API key not found in configuration file.")

    openai.api_key = api_key

    code = ''
    if code_only:
        code = f" in {code_name} just give me the code inside of a {is_type} with comments within the {is_type}"

    prompt = prompt + code + ":"

    response_file = 'Responses.json'

    d = ''

    try:

        # Read the response file line by line
        with open(response_file, "r") as f:
            conversation = json.load(f)

        # Loop through each line and calculate the similarity score between the prompt and the response
        if search_query is not None:
            for k, v in conversation.items():
                for key, value in v.items():
                    if search_query in str([k.lower(), key.lower(), value.lower()]):
                        d += f'{key}: {value}'
        if search_convo is not None:
            for k, v in conversation.items():
                if search_convo in k.lower():
                    d += f'{k}: {v}'
                    search_query = k

    except ValueError:
        print('not able to read Responses.json')
    except FileNotFoundError:
        print('test')

    prompt = f"{d} {user_name}: {prompt} {code} {bot_name}:"

    print(f'I am researching "{prompt}" now')
    speak(f'Researching now')

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    with open('Responses.json') as f:
        d = json.load(f)
        print(response.choices[0].text.strip())
    d.update({search_query: {prompt[:prompt.rindex(":")].strip(): response.choices[0].text.strip()}})

    with open("Responses.json", mode='w') as f:
        f.write(json.dumps(d, indent=4))

    response_text = response.choices[0].text.strip()
    response_text = response_text.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

    return response_text


def chatgpt(prompt, user_name='Will', bot_name='Jarvis', code_name='python', code_only=False, is_type='function',
                  search_query=None, search_convo=None, model="text-davinci-003", temperature=0.7, max_tokens=1000,
                  top_p=1, frequency_penalty=0, presence_penalty=0):
    import json

    import openai
    import configparser
    from Speak import speak

    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        api_key = config['chatgpt'].get('api_key')
    except KeyError:
        raise ValueError("API key not found in configuration file.")

    openai.api_key = api_key

    code = ''
    if code_only:
        code = f" in {code_name} just give me the code inside of a {is_type} with comments within the {is_type}"

    prompt = prompt + code + ":"

    response_file = 'Comms/Responses.json'

    d = ''

    try:

        # Read the response file line by line
        with open(response_file, "r") as f:
            conversation = json.load(f)

        # Loop through each line and calculate the similarity score between the prompt and the response
        if search_query is not None:
            for k, v in conversation.items():
                for key, value in v.items():
                    if search_query in str([k.lower(), key.lower(), value.lower()]):
                        d += f'{key}: {value}'
        if search_convo is not None:
            for k, v in conversation.items():
                if search_convo in k.lower():
                    d += f'{k}: {v}'
                    search_query = k

    except ValueError:
        print('not able to read Responses.json')
    except FileNotFoundError:
        print('test')

    prompt = f"{d} {user_name}: {prompt} {code} {bot_name}:"

    print(f'I am researching "{prompt}" now')
    speak(f'Researching now')

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    with open(response_file) as f:
        d = json.load(f)
        print(response.choices[0].text.strip())
    d.update({search_query: {prompt[:prompt.rindex(":")].strip(): response.choices[0].text.strip()}})

    with open(response_file, mode='w') as f:
        f.write(json.dumps(d, indent=4))

    response_text = response.choices[0].text.strip()
    response_text = response_text.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

    return response_text


if __name__ == '__main__':
    prompt = """
        how can I jupter notebook from a python script: just give me the code with comments:
    """
    import sys
#     prompt = sys.argv[1]
    chatgpt(prompt)
