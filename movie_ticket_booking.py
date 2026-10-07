import streamlit as st
import base64
import os

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Keerthi's Ticket Booking App",
    page_icon="🎟️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- BACKGROUND IMAGE ----------------
BACKGROUND_FILE = "movie_background.png"

if os.path.exists(BACKGROUND_FILE):
    with open(BACKGROUND_FILE, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    background_css = f"""
<style>
.stApp {{
    background-color: #efe09b;
    background-image: url("data:image/png;base64,{encoded_image}");
    background-repeat: no-repeat;
    background-position: center top;
    background-size: 430px auto;
    background-attachment: fixed;
}}

.block-container {{
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}}

.main-title {{
    text-align: center;
    color: #5b4822;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.7);
}}

.subtitle {{
    text-align: center;
    color: #75643a;
    font-size: 18px;
    margin-bottom: 25px;
}}

.section-title {{
    color: #5b4822;
    font-size: 24px;
    font-weight: 700;
    margin-top: 12px;
    margin-bottom: 10px;
}}

.card {{
    background: rgba(255, 252, 235, 0.93);
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(100, 80, 30, 0.16);
    border: 1px solid rgba(255,255,255,0.8);
    margin-bottom: 20px;
}}

.movie-card {{
    background: rgba(255, 250, 220, 0.95);
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #e5d68f;
    margin-top: 10px;
}}

.movie-name {{
    color: #59451e;
    font-size: 22px;
    font-weight: 700;
}}

.movie-info {{
    color: #79683d;
    font-size: 15px;
    line-height: 1.8;
}}

.price-box {{
    background: #fff8d7;
    border: 1px solid #dfce7d;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    margin-top: 18px;
}}

.price-label {{
    color: #79683d;
    font-size: 16px;
}}

.price-value {{
    color: #57441c;
    font-size: 34px;
    font-weight: 800;
}}

.summary-box {{
    background: rgba(255, 252, 235, 0.96);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 7px 24px rgba(100, 80, 30, 0.15);
    border-left: 6px solid #d3b957;
    margin-top: 20px;
}}

.summary-heading {{
    color: #59451e;
    font-size: 25px;
    font-weight: 800;
}}

.total-label {{
    color: #4e3c18;
    font-size: 22px;
    font-weight: 800;
}}

.total-value {{
    color: #4e3c18;
    font-size: 30px;
    font-weight: 800;
}}

.success-box {{
    background: #edf6d9;
    border: 1px solid #bfd18b;
    color: #52652c;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    margin-top: 20px;
    font-size: 18px;
    font-weight: 600;
}}

.footer {{
    text-align: center;
    color: #776638;
    font-size: 14px;
    margin-top: 30px;
    padding-bottom: 15px;
}}

div[data-testid="stButton"] > button {{
    width: 100%;
    background-color: #b79b43;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px;
    font-size: 17px;
    font-weight: 700;
}}

div[data-testid="stButton"] > button:hover {{
    background-color: #967d31;
    color: white;
}}

@media (max-width: 600px) {{
    .block-container {{
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }}

    .main-title {{
        font-size: 30px;
    }}

    .subtitle {{
        font-size: 15px;
    }}

    .section-title {{
        font-size: 21px;
    }}

    .card {{
        padding: 18px;
        border-radius: 18px;
    }}

    .price-value {{
        font-size: 28px;
    }}

    .summary-box {{
        padding: 18px;
    }}
}}
</style>
"""

else:
    background_css = """
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #f5e8a8,
        #eee0a0,
        #f7edb9
    );
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    text-align: center;
    color: #5b4822;
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: #75643a;
    font-size: 18px;
}

.section-title {
    color: #5b4822;
    font-size: 24px;
    font-weight: 700;
}

.card {
    background: rgba(255, 252, 235, 0.93);
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(100, 80, 30, 0.16);
}

.summary-box {
    background: rgba(255, 252, 235, 0.96);
    padding: 25px;
    border-radius: 20px;
    border-left: 6px solid #d3b957;
}

div[data-testid="stButton"] > button {
    background-color: #b79b43;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
}
</style>
"""

st.markdown(background_css, unsafe_allow_html=True)

# ---------------- MOVIE DATA ----------------
movies = {
    "🎬 Chakkora": {
        "language": "Telugu",
        "genre": "Drama / Romance",
        "duration": "2h 20m"
    },
    "🎬 Aadarsha Kutumbam House No: 47": {
        "language": "Telugu",
        "genre": "Action / Comedy",
        "duration": "2h 20m"
    },
    "🎬 Ranabaali": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "duration": "2h 20m"
    },
    "🎬 Itllu Arjuna": {
        "language": "Telugu",
        "genre": "Drama / Action / Romance",
        "duration": "2h 20m"
    },
    "🎬 #Cult": {
        "language": "Telugu",
        "genre": "Drama",
        "duration": "2h 20m"
    },
    "🎬 Mysaa": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "duration": "2h 20m"
    }
}

# ---------------- TICKET PRICES ----------------
ticket_prices = {
    "Standard": 150,
    "Premium": 220,
    "VIP": 350
}

# ---------------- SESSION STATE ----------------
if "booking_confirmed" not in st.session_state:
    st.session_state.booking_confirmed = False

if "booking_details" not in st.session_state:
    st.session_state.booking_details = {}

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>🎟️ Keerthi's Ticket Booking App</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Book your movie tickets quickly and easily 🍿</div>",
    unsafe_allow_html=True
)

# ---------------- CUSTOMER DETAILS ----------------
st.markdown(
    "<div class='section-title'>👤 Customer Details</div>",
    unsafe_allow_html=True
)

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter your name"
)

# ---------------- MOVIE SELECTION ----------------
st.markdown(
    "<div class='section-title'>🎬 Select Your Movie</div>",
    unsafe_allow_html=True
)

selected_movie = st.selectbox(
    "Choose a movie",
    list(movies.keys())
)

movie_info = movies[selected_movie]

st.markdown(
    f"""
<div class="movie-card">
    <div class="movie-name">{selected_movie}</div>
    <div class="movie-info">
        🎞️ Genre: {movie_info["genre"]}<br>
        🗣️ Language: {movie_info["language"]}<br>
        ⏱️ Duration: {movie_info["duration"]}
    </div>
</div>
""",
    unsafe_allow_html=True
)

# ---------------- SHOW DETAILS ----------------
st.markdown(
    "<div class='section-title'>📅 Show Details</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    show_date = st.date_input(
        "Select Date"
    )

with col2:
    show_time = st.selectbox(
        "Select Show Time",
        [
            "10:00 AM",
            "1:00 PM",
            "4:00 PM",
            "7:00 PM",
            "10:00 PM"
        ]
    )

# ---------------- TICKET DETAILS ----------------
st.markdown(
    "<div class='section-title'>🎫 Ticket Details</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    ticket_category = st.selectbox(
        "Ticket Category",
        list(ticket_prices.keys())
    )

with col2:
    number_of_tickets = st.number_input(
        "Number of Tickets",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

price_per_ticket = ticket_prices[ticket_category]

total_price = price_per_ticket * number_of_tickets

st.markdown(
    f"""
<div class="price-box">
    <div class="price-label">
        {ticket_category} Ticket Price
    </div>
    <div class="price-value">
        ₹{price_per_ticket}
    </div>
</div>
""",
    unsafe_allow_html=True
)

# ---------------- BOOKING SUMMARY ----------------
st.markdown(
    "<div class='section-title'>🧾 Booking Summary</div>",
    unsafe_allow_html=True
)

summary_col1, summary_col2 = st.columns([1, 1])

with summary_col1:
    st.write("**Customer**")
    st.write("**Movie**")
    st.write("**Date**")
    st.write("**Show Time**")

with summary_col2:
    st.write(
        customer_name if customer_name else "Not entered"
    )
    st.write(selected_movie)
    st.write(str(show_date))
    st.write(show_time)

st.markdown("---")

summary_col1, summary_col2 = st.columns([1, 1])

with summary_col1:
    st.write("**Ticket Type**")
    st.write("**Number of Tickets**")
    st.write("**Price Per Ticket**")

with summary_col2:
    st.write(ticket_category)
    st.write(number_of_tickets)
    st.write(f"₹{price_per_ticket}")

st.markdown("---")

total_col1, total_col2 = st.columns([1, 1])

with total_col1:
    st.markdown(
        "<div class='total-label'>Grand Total</div>",
        unsafe_allow_html=True
    )

with total_col2:
    st.markdown(
        f"<div class='total-value'>₹{total_price}</div>",
        unsafe_allow_html=True
    )

# ---------------- CONFIRM BOOKING ----------------
st.markdown("")

if st.button(
    "🎟️ Confirm Booking",
    use_container_width=True
):

    if not customer_name.strip():

        st.warning(
            "⚠️ Please enter your name before confirming the booking."
        )

    else:

        st.session_state.booking_confirmed = True

        st.session_state.booking_details = {
            "customer": customer_name,
            "movie": selected_movie,
            "date": str(show_date),
            "time": show_time,
            "category": ticket_category,
            "tickets": number_of_tickets,
            "total": total_price
        }

# ---------------- CONFIRMATION ----------------
if st.session_state.booking_confirmed:

    details = st.session_state.booking_details

    st.markdown(
        "<div class='success-box'>",
        unsafe_allow_html=True
    )

    st.markdown("### ✅ Booking Confirmed Successfully!")

    st.write(f"🎬 **Movie:** {details['movie']}")

    st.write(
        f"🎟️ **Tickets:** {details['tickets']} × "
        f"{details['category']}"
    )

    st.write(
        f"📅 **Date:** {details['date']}"
    )

    st.write(
        f"⏰ **Show Time:** {details['time']}"
    )

    st.write(
        f"💰 **Grand Total:** ₹{details['total']}"
    )

    st.success(
        f"Thank you, {details['customer']}! Enjoy your movie 🍿"
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>🎬 Enjoy your movie! • Made with ❤️ by Keerthi</div>",
    unsafe_allow_html=True
)