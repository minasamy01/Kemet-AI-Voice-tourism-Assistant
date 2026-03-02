import streamlit as st
import json
from logic import transcribe_audio, detect_location_from_keys, recommend_hotel_agent, booking_agent, send_email_logic
from audio_recorder_streamlit import audio_recorder # مكتبة إضافية لتسجيل الصوت

st.set_page_config(page_title="Kemet AI Assistant", page_icon="🎙️")

st.title("🎙️ Egypt Tourist Assistant")
st.markdown("Welcome to **KEMET** - Your AI Voice Guide to Egypt")

# تحميل قاعدة البيانات
@st.cache_data
def load_db():
    with open("hotels.json", "r", encoding="utf-8") as f:
        return json.load(f)["egypt_travel_guide"]

HOTELS_DB = load_db()

# إدارة الجلسة (Session State)
if "session" not in st.session_state:
    st.session_state.session = {"hotel_details": None, "recommendation": None, "booking_info": None}

# تسجيل الصوت
audio_bytes = audio_recorder(text="Click to record your request", icon_size="2x")

if audio_bytes:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_bytes)
    
    with st.spinner("Processing your voice..."):
        user_text = transcribe_audio("temp_audio.wav")
        st.write(f"📝 **You said:** {user_text}")

        loc_key = detect_location_from_keys(user_text, list(HOTELS_DB.keys()))
        
        if loc_key:
            hotels = HOTELS_DB[loc_key]
            rec = recommend_hotel_agent(user_text, hotels)
            hotel_details = next((h for h in hotels if h['name'] == rec['recommended_hotel']), None)
            
            if hotel_details:
                st.success(f"✅ Recommended: {hotel_details['name']}")
                st.info(f"💡 **Reason:** {rec['reason']}")
                
                booking = booking_agent(hotel_details['name'])
                st.session_state.session.update({
                    "hotel_details": hotel_details,
                    "recommendation": rec,
                    "booking_info": booking
                })
                st.balloons()
        else:
            st.warning("📍 Location not detected. Please try again or speak clearly.")

# قسم إرسال الإيميل
if st.session_state.session["hotel_details"]:
    st.divider()
    email = st.text_input("Enter your email to receive the ticket:")
    if st.button("📧 Send My Ticket"):
        success = send_email_logic(
            email, 
            st.session_state.session["hotel_details"],
            st.session_state.session["booking_info"],
            st.session_state.session["recommendation"]["reason"]
        )
        if success: st.success("Ticket sent!")
        else: st.error("Email failed.")