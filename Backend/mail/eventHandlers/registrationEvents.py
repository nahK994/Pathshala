import json
from django.core.mail import EmailMultiAlternatives
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mail.settings")
django.setup()
from django.conf import settings
from django.template.loader import render_to_string


def send_email(html_template, destination_email, data):
    html_content = render_to_string(html_template, data)
    msg = EmailMultiAlternatives('Pathshala teacher invitation email', '', settings.EMAIL_HOST_USER, [
        destination_email
    ])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def acceptTeacher(ch, method, properties, body):
    data = json.loads(body.decode('ASCII'))
    print(f"Invite teacher {data} {settings.EMAIL_HOST_USER}")
    send_email("accept_teacher.html", 'nkskl6@gmail.com', {
        "key": "Test teacher accept mail template"
    })
    print("done")