Hotdev Mailer
=
Support very easy way to use python emails(https://github.com/lavr/python-emails) library.
Emails is alreay human friendly python email libary.

Install
=
	>>> pip install hdv_mailer	

Usage
=
    >>> from hdv_mailer import Message, GMailSMTP
    >>> gmail = GMailSMTP('gmail@gmail.com', password='gmailpassword')
    >>> message = Message(
                  html="hello",
                  subject="test",
                  mail_from=('your@email.com', 'John Doe'),
                  mail_to=[('John Doe1', 'your1@email.com'), ('John Doe2', 'your2@email.com')],
                  bcc=["your@email.com"],
                  cc=["your@email.com"],
                  )
    >>> message.attach(data='/tmp/hello1', filename='hello1')
    >>> message.attach(data='/tmp/hello2', filename='hello2')
	>>> gmail.send(message)


