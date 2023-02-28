from django.core.mail import EmailMessage

def send_email(request):
    subject = 'Your subject'
    body = 'Your message'
    sender = 'your-email@example.com'
    recipient = 'recipient@example.com'
    html_body = '<html><body>Your HTML message</body></html>'
    attachment = ('filename.pdf', open('/path/to/filename.pdf', 'rb').read(), 'application/pdf')
    email = EmailMessage(subject, body, sender, [recipient])
    email.content_subtype = "html"
    email.attach(*attachment)
    email.send()
