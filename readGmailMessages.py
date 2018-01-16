import imaplib
import re
import email


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')
        type, data = mail.search(None, 'All')
        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            raw_text = (data[0][1])
            msg = email.message_from_string(raw_text.decode('utf-8'))
            print('From: %s' % msg['from'])
            print('To: %s' % (re.search(r'[\w\.-]+@[\w\.-]+', msg['to'])).group(0))
            print('Subject: %s' % msg['subject'])
            print('Date: %s' % msg['date'])
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    print('body: \n %s ' %  part.get_payload(decode=True).decode('utf-8'))
            print('***********************************************************************')
        mail.close()
        mail.logout()

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    ORG_EMAIL = "@gmail.com"
    FROM_EMAIL = "qermezkon" + ORG_EMAIL
    FROM_PWD = "Mveyma6303$Kabinet95"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    read_email_from_gmail()