import imaplib
import email
from email.header import decode_header
import re

def get_icici_amount():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("manrahulbajwa@gmail.com", "jtpxduqyfyksvgob")
        mail.select("inbox")

        status, messages = mail.search(None, '(FROM "cards@icicibank.com")')
        mail_ids = messages[0].split()
        if not mail_ids:
            return "No ICICI emails found."

        latest_email_id = mail_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                body = ""
                for part in msg.walk():
                    if part.get_content_type() in ["text/plain", "text/html"]:
                        body += part.get_payload(decode=True).decode(errors='ignore')
                
                # Try to find amount and purpose
                # Look for INR or Rs followed by numbers
                amount_match = re.findall(r"(?:INR|Rs\.?|Amount:)\s?(\d+(?:\.\d+)?)", body)
                merchant_match = re.findall(r"Merchant Name:\s?([^<]+)", body)
                date_match = re.findall(r"Date:\s?([^<]+)", body)
                
                return {
                    "subject": msg.get("Subject"),
                    "amounts": amount_match,
                    "merchant": merchant_match[0].strip() if merchant_match else "Unknown",
                    "date": date_match[0].strip() if date_match else "Unknown",
                    "raw_body_snippet": body[:2000] # for backup
                }
        mail.logout()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import json
    print(json.dumps(get_icici_amount(), indent=2))
