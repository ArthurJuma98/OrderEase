import africastalking
from django.conf import settings

# Initializing Africa's Talking with environment variables
africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms_alert(customer_name, item):
    message = f"Hello {customer_name}, your order for {item} has been received."
    sms.send(message, ["+254712349840"])