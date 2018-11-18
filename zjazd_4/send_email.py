import smtplib

user = "pythonbootcamp"
password = "123!@#qweQWE"

sent_from = "pythonbootcamp@wp.pl"
to = ["adresat"]
subject = "Try this"
body = "To jest terść"

email_txt = f"""
From: {sent_from}
To: {','.join(to)}
Subject: {subject}

{body}
"""
try:
    server = smtplib = smtplib.SMTP_SSL("smtp.wp.pl", 465)
    server.ehelo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_txt)
    server.close
except Exception as e:
    print(e)
    print("Coś poszło źle")