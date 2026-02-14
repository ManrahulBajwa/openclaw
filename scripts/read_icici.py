import imaplib
import email
from email.header import decode_header

def get_icici_details():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        # Search for ICICI bank emails
        status, messages = mail.search(None, '(FROM "cards@icicibank.com")')
        if status != "OK":
            return "Error searching inbox"

        mail_ids = messages[0].split()
        if not mail_ids:
            return "No ICICI emails found."

        latest_email_id = mail_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()
                
                return f"Subject: {subject}\n\nBody Snippet:\n{body[:1000]}"
        
        mail.logout()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(get_icici_details())
