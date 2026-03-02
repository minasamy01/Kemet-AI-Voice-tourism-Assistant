import cohere
import whisper
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# إعداد النماذج
co = cohere.Client(os.getenv("COHERE_API_KEY"))
whisper_model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]

def detect_location_from_keys(user_text, keys):
    prompt = f"Map user message: '{user_text}' to ONE of: {', '.join(keys)}. Return ONLY the key or NONE."
    response = co.chat(model="command-r-08-2024", message=prompt, temperature=0)
    key = response.text.strip()
    return key if key in keys else None

def recommend_hotel_agent(user_text, hotels):
    hotels_text = "".join([f"- {h['name']} ({h['category']}) ⭐ {h['rating']}\n" for h in hotels])
    prompt = f"User request: '{user_text}'\nList of Hotels:\n{hotels_text}\nRules: Recommend ONE best hotel. Return ONLY JSON: {{\"recommended_hotel\": \"...\", \"reason\": \"...\"}}"
    response = co.chat(model="command-r-plus-08-2024", message=prompt, temperature=0)
    import json
    try: return json.loads(response.text)
    except: return {"recommended_hotel": None, "reason": "Parsing error"}

def booking_agent(hotel_name, nights=2):
    conf_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return {
        "status": "Confirmed",
        "hotel": hotel_name,
        "nights": nights,
        "confirmation_code": conf_code,
        "message": f"Successfully booked {nights} nights at {hotel_name}."
    }

def send_email_logic(receiver_email, hotel, booking_info, reason):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["Subject"] = f"🏨 Booking Confirmed: {hotel['name']}"
    body = f"Hello,\n\nYour booking is CONFIRMED!\n\nHotel: {hotel['name']}\nCode: {booking_info['confirmation_code']}\n\nReason: {reason}"
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except:
        return False