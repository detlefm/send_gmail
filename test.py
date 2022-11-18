from pathlib import Path
import os
from send_gmail import SendGMail


def load_dotenv() -> str:
    cwd = Path.home()
    if (path := Path(cwd) / '.env'):
        for l in  path.read_text(encoding='utf-8').splitlines():
            token = [ s.strip() for s in l.split('=')]
            os.environ[token[0]] = token[1].strip('"')


load_dotenv()
html = '<html><body>Hello world </body></html>'
txt = 'Hello world as text'
subject = 'First message'
pdffile = './test/test.pdf'

smtpsrv = SendGMail(id=os.getenv('MAIL_ID'),pwd=os.getenv('MAILPWD'))

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

errs = smtpsrv.send(from_addr=os.getenv('MAIL_ID'), 
                                to_addr=os.getenv('TESTREC'), 
                                subject=subject, 
                                html=html, 
                                text = txt, 
                                attachments=pdffile)

SendGMail(id=os.getenv('MAIL_ID'),pwd=os.getenv('MAILPWD')).send(None,os.getenv('TESTREC'))