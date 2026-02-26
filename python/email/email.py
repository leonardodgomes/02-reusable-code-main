import os
import datetime
import win32com.client as win32


def get_path():
    full_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)

    return {
        "Full Path": full_path,
        "Folder Path": folder_path,
        "File Name": file_name
    }


def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    return "Good evening"


def load_template(template_path, placeholders=None):
    """
    Load an HTML template and replace placeholders like {{greeting}}.
    """
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if placeholders:
        for key, value in placeholders.items():
            html = html.replace(f"{{{{{key}}}}}", value)

    return html


def send_email(subject, html_body, recipient_email, attachment_path=None):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = subject
    mail.HTMLBody = html_body
    mail.To = recipient_email

    if os.path.exists(attachment_path):
        mail.Attachments.Add(attachment_path)
    else:
        print("WARNING: Attachment not found:", attachment_path)


    mail.Display()  # or mail.Send()


def main():
    paths = get_path()
    folder = paths["Folder Path"]

    subject = "Hello from Python!"
    recipient = "example@example.com"
    attachment = os.path.join(folder, "file_to_attach.txt")

    template_path = os.path.join(folder, "templates", "email_template.html")

    html_body = load_template(
        template_path,
        placeholders={
            "greeting": get_greeting(),
            "name": "Leonardo"
        }
    )

    send_email(subject, html_body, recipient, attachment)

    #send_email(subject, html_body, recipient)

if __name__ == "__main__":
    main()
