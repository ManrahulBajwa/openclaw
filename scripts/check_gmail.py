import imaplib
import email
from email.header import decode_header

def check_mail():
    try:
        # Connect to Gmail
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        # Search for all emails
        status, messages = mail.search(None, "UNSEEN")
        if status != "OK":
            return "Error searching inbox"

        mail_ids = messages[0].split()
        if not mail_ids:
            return "No new emails."

        latest_email_id = mail_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        
        results = []
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                from_ = msg.get("From")
                results.append(f"From: {from_}\nSubject: {subject}")
        
        mail.logout()
        return "\n\n".join(results)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(check_mail())
