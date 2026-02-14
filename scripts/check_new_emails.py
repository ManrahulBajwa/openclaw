import imaplib
import email
from email.header import decode_header

def check_mail():
    try:
        # Connect to Gmail
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        # Search for UNSEEN emails
        status, messages = mail.search(None, "UNSEEN")
        if status != "OK":
            return "Error searching inbox"

        mail_ids = messages[0].split()
        if not mail_ids:
            return "No new emails."

        results = []
        # Get up to 5 latest unseen emails
        for mail_id in mail_ids[-5:]:
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")
                    
                    # Extract snippet/body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                try:
                                    body = part.get_payload(decode=True).decode()
                                    break
                                except:
                                    pass
                    else:
                        body = msg.get_payload(decode=True).decode()
                    
                    snippet = body[:200].replace('\r', '').replace('\n', ' ') + "..."
                    results.append(f"From: {from_}\nSubject: {subject}\nSnippet: {snippet}")
        
        mail.logout()
        return "\n\n---\n\n".join(results)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(check_mail())
