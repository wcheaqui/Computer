

def email_update():

    from Comms import speak, listen

    import emlx
    import glob

    for filepath in glob.iglob("/Users/WCheaq/Library/Mail/V10/79936577-8B98-4E44-9E97-BE66BB7516C3/Inbox.mbox/**/*.emlx", recursive=True):
        get_email = emlx.read(filepath)
        m = get_email.headers

        hour = int(m['Date'][m['Date'].rindex(':')-5:m['Date'].rindex(':')-3])-7
        if hour < 12:
            am_pm = 'a.m.'
        else:
            hour -= 12
            am_pm = 'p.m.'

        minute = int(m['Date'][m['Date'].rindex(':')-2:m['Date'].rindex(':')])
        if minute < 10:
            minute = f"O{minute}"

        speak(f"""
            Sent from {m['From'][:m['From'].rindex('<')-1]}.
            {m['Subject']}.
            On {m['Date'][m['Date'].index(', '):m['Date'].rindex(':')-5]} at {hour}:{minute} {am_pm}.
            """)

    for filepath in glob.iglob("/Users/WCheaq/Library/Mail/V10/1E3271C8-E2E9-4B6D-883F-B650E344E371/INBOX.mbox/**/*.emlx", recursive=True):
        get_email = emlx.read(filepath)
        m = get_email.headers

        hour = int(m['Date'][m['Date'].rindex(':')-5:m['Date'].rindex(':')-3])-7
        if hour < 12:
            am_pm = 'a.m.'
        else:
            hour -= 12
            am_pm = 'p.m.'

        minute = int(m['Date'][m['Date'].rindex(':')-2:m['Date'].rindex(':')])
        if minute < 10:
            minute = f"O{minute}"

        speak(f"""
            Sent from {m['From'][:m['From'].rindex('<')-1]}.
            {m['Subject']}.
            On {m['Date'][m['Date'].index(', '):m['Date'].rindex(':')-5]} at {hour}:{minute} {am_pm}.
            ... Would you like me to read the email?    
            """)

        if 'yes' in listen():
            speak(get_email.text)
