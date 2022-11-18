# send_gmail
Python : Sending an email via smtp Server
Default smtp Server : gmail

usage:

```python
from send_gmail import SendGMail

html = '<html><body>Hello world </body></html>'
txt = 'Hello world as text'
subject = 'First message'
pdffile = r'c:\tmp\test.pdf'

smtpsrv = SendGMail(id='xxxx@gmail.com',pwd='977823490123')

"""
send

Args:
    from_addr (str | None): sender email, if None the id field is used   
    to_addr (list | str): receiver(s) email, string for one - list for many
    subject (str | None ): subject as utf-8 text, if None current date is send
    html (str, optional):html part of message. Defaults to None.
    text (str, optional): text part of message. Defaults to None.
    attachments (list | str, optional): files to attach. Defaults to None.

Returns:
    dict: dictionary of errors, key == to_addr, value == Error
"""

errs = smtpsrv.send(from_addr='xxxx@gmail.com', 
                                to_addr='yyyy@gmail.com', 
                                subject=subject, 
                                html=html, 
                                text = txt, 
                                attachments=pdffile)
                                
# or send just the current date as subject to yyyy@gmail.com
SendGMail(id='xxxx@gmail.com',pwd='977823490123').send(None,'yyyy@gmail.com')

```


