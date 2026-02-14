import imaplib
import email
from email.header import decode_header
import datetime

def search_missed_email():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        # Search for emails from today
        today = datetime.datetime.now().strftime("%d-%b-%Y")
        status, messages = mail.search(None, f'(ON {today})')
        
        mail_ids = messages[0].split()
        results = []
        
        for mail_id in mail_ids:
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    date_str = msg.get("Date")
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")
                    results.append(f"Time: {date_str} | From: {from_} | Subject: {subject}")
        
        mail.logout()
        return "\n".join(results)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(search_missed_email())
