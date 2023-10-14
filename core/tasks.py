from celery import shared_task
from core.models import Message, Newsletter, Client
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
from dateutil import parser

load_dotenv()

API_ADDRESS = os.getenv("API_ADDRESS")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
PROJECT_NAME = os.getenv("PROJECT_NAME")

@shared_task(bind=True)
def send_start(self, newsletter_id): 
    #####* ---- Getting newsletter data from the API ---- #####


    try:
        response_newsletter = requests.get(f"http://127.0.0.1:8000/api/newsletters/?id={newsletter_id}")
        newsletter_data = response_newsletter.json()[0]
    except:
        return f"There is no newsletter with id [{newsletter_id}]"


    newsletter_id = newsletter_data.get("id")
    newsletter_send_start = parser.parse(newsletter_data.get("send_start"))
    newsletter_send_end = parser.parse(newsletter_data.get("send_end"))
    newsletter_filter = newsletter_data.get("mobile_code")
    newsletter_text_message = newsletter_data.get("text_message")

    #####* ---- Getting clients from the API ---- *#####

    response_clients = requests.get(f"http://127.0.0.1:8000/api/clients/?mobile_code={newsletter_filter}")
    clients_data = response_clients.json()

    message_for_user = []

    for client in clients_data:
        client_id = client.get('id')
        client_phone = client.get('phone')

        #####* ---- Creating message object ---- *#####
        newsletter_object = Newsletter.objects.get(id=newsletter_id)
        client_object = Client.objects.get(id=client_id)

        message = Message.objects.create(newsletter_id=newsletter_object, send_to=client_object, send_status=True)
        message_id = message.id

        json_object = {
        "id": message_id,
        "phone": client_phone,
        "text": newsletter_text_message
        }
        
        response = requests.post(f'{API_ADDRESS}/send/{message_id}', headers={'Authorization': AUTH_TOKEN}, json = json_object)

        if response.status_code == 200:
            message_for_user.append(f"Message with id [{message_id}] has been sent successfully!")
        else:
            message_for_user.append(f"Couldn't send the message with id [{message_id}], something went wrong.")
    return message_for_user
