import imaplib
import email
from email.header import decode_header

# Configuration from the config.toml we found earlier
IMAP_SERVER = "imap.gmail.com"
EMAIL_USER = "manrahulbajwa@gmail.com"
EMAIL_PASS = "jtpx duqy fyks vgob"

def check_emails():
    try:
        # Connect to server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        # Search for unread messages
        status, messages = mail.search(None, 'UNSEEN')
        
        if status != 'OK':
            print("Error searching for emails.")
            return

        mail_ids = messages[0].split()
        
        if not mail_ids:
            print("NO_NEW_EMAILS")
            return

        print(f"FOUND {len(mail_ids)} NEW EMAILS")
        
        # Get the latest 3 emails
        for i in mail_ids[-3:]:
            res, msg = mail.fetch(i, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    
                    from_, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(from_, bytes):
                        from_ = from_.decode(encoding if encoding else "utf-8")
                    
                    print(f"---")
                    print(f"From: {from_}")
                    print(f"Subject: {subject}")

        mail.close()
        mail.logout()
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    check_emails()
