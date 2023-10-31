from django.core.mail import send_mail


# Function to send email notifications to the customers on the queue
def send_notification(email, message):
    try:
        send_mail(
            'Notification',
            message,
            'test@rovinewanjala.com',  # Replace with your email address
            [email],
            fail_silently=False,
        )
        return True  # Return True if the email is successfully sent
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Return False if sending the email fails
