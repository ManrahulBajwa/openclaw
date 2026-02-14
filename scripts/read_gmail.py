import imaplib
import email
from email.header import decode_header

def get_email_body(latest_email_id):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            return body
                else:
                    return msg.get_payload(decode=True).decode()
        mail.logout()
    except Exception as e:
        return f"Error: {str(e)}"

def check_mail_full():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        # Search for messages from Hostinger regarding the domain
        status, messages = mail.search(None, '(FROM "Hostinger" SUBJECT "manrahul.in")')
        if status != "OK":
            return "Error searching inbox"

        mail_ids = messages[0].split()
        if not mail_ids:
            return "No matching emails found."

        latest_email_id = mail_ids[-1]
        body = get_email_body(latest_email_id)
        mail.logout()
        return body
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(check_mail_full())
