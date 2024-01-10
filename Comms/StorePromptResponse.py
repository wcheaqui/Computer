

def store_prompt_response(prompt, response):
    """Stores a prompt and response in a database."""

    import sqlite3
    # Create connection to database
    conn = sqlite3.connect('ChatGPTComms.db')
    # Create a cursor"
    c = conn.cursor()
    # Execute SQL command to store prompt-response pair
    c.execute('INSERT INTO prompts_and_responses(prompt, response) VALUES(?, ?)', (prompt, response))
    # Commit changes to database
    conn.commit()
    # Close connection to database
    conn.close()