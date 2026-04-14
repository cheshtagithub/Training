import smtplib
from email.mime.text import MIMEText

from fastapi import HTTPException, status

from app.core.config import get_settings


def send_email(to_email: str, subject: str, body: str) -> None:
    settings = get_settings()

    # Build a plain-text email message.
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = settings.email_user
    message["To"] = to_email

    try:
        # Connect to Gmail SMTP over TLS and send the email.
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(settings.email_user, settings.email_pass)
            server.sendmail(settings.email_user, to_email, message.as_string())
    except smtplib.SMTPException as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send email",
        ) from exc
