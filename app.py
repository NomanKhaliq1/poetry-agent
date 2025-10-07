import streamlit as st
import random

st.set_page_config(page_title="✍️ Poetry Agent", layout="centered")
st.title("✍️ Poetry Agent")

if "favorites" not in st.session_state:
    st.session_state.favorites = []

poetry = {
    "Romantic": {
        "Roman Urdu": [
            "Tumhare bina zindagi se shikwa bhi nahi,\nTum hi zindagi ho, tum se hi roshan safar hai.",
            "Mohabbat ka silsila bhi ajeeb hai,\nAnjaane logon se shuru hota hai,\nAur bepanah yaadon mein sama jaata hai."
        ],
        "English": [
            "Without you, life holds no complaint,\nYou are my journey, you are my light.",
            "Love’s journey is strange,\nIt begins with strangers,\nAnd ends in endless memories."
        ],
        "Urdu": [
            "تمہارے بنا زندگی سے شکوہ بھی نہیں،\nتم ہی زندگی ہو، تم سے ہی روشن سفر ہے۔",
            "محبت کا سلسلہ بھی عجیب ہے،\nانجانے لوگوں سے شروع ہوتا ہے،\nاور بے پناہ یادوں میں سما جاتا ہے۔"
        ]
    },

    "Sad": {
        "Roman Urdu": [
            "Jo log khamosh rehte hain,\nWoh aksar dil ke sabse gehre zakham chhupaye hote hain.",
            "Tanhaai ka dard samajhna aasaan nahi,\nWoh sirf mehsoos hota hai, bayan nahi hota."
        ],
        "English": [
            "Those who stay silent,\nOften hide the deepest wounds in their hearts.",
            "The pain of loneliness is hard to explain,\nIt can only be felt, never described."
        ],
        "Urdu": [
            "جو لوگ خاموش رہتے ہیں،\nوہ اکثر دل کے سب سے گہرے زخم چھپائے ہوتے ہیں۔",
            "تنہائی کا درد سمجھنا آسان نہیں،\nوہ صرف محسوس ہوتا ہے، بیان نہیں ہوتا۔"
        ]
    },

    "Motivational": {
        "Roman Urdu": [
            "Gir kar uthna seekh lo,\nZindagi haarne walon ko mauka nahi deti.",
            "Sapne unke sach hote hain,\nJo din mein bhi unhe dekhte hain."
        ],
        "English": [
            "Learn to rise after every fall,\nLife gives no chance to those who quit.",
            "Dreams come true for those,\nWho chase them even in daylight."
        ],
        "Urdu": [
            "گر کر اُٹھنا سیکھ لو،\nزندگی ہارنے والوں کو موقع نہیں دیتی۔",
            "خواب اُن کے ہی سچ ہوتے ہیں،\nجو دن میں بھی اُنہیں دیکھتے ہیں۔"
        ]
    },

    "Friendship": {
        "Roman Urdu": [
            "Dosti wo rishta hai jo dil se hota hai,\nWaqt ke sath nahi, ehsaas se mazboot hota hai.",
            "Asli dost wo nahi jo muskura kar sath de,\nBalki wo hai jo ro kar bhi sath na chhode."
        ],
        "English": [
            "Friendship is a bond from the heart,\nNot built by time but strengthened by feeling.",
            "A true friend isn’t the one who smiles with you,\nBut the one who stays even through tears."
        ],
        "Urdu": [
            "دوستی وہ رشتہ ہے جو دل سے ہوتا ہے،\nوقت کے ساتھ نہیں، احساس سے مضبوط ہوتا ہے۔",
            "اصلی دوست وہ نہیں جو مسکرا کر ساتھ دے،\nبلکہ وہ ہے جو رو کر بھی ساتھ نہ چھوڑے۔"
        ]
    },

    "Life": {
        "Roman Urdu": [
            "Zindagi ek safar hai, manzil nahi,\nHar mod par seekhne ka naya sabab milta hai.",
            "Khush rehna ek hunar hai,\nJo sab ke paas nahi hota."
        ],
        "English": [
            "Life is a journey, not a destination,\nEvery turn teaches something new.",
            "Happiness is an art,\nNot everyone masters it."
        ],
        "Urdu": [
            "زندگی ایک سفر ہے، منزل نہیں،\nہر موڑ پر سیکھنے کا نیا سبب ملتا ہے۔",
            "خوش رہنا ایک ہنر ہے،\nجو سب کے پاس نہیں ہوتا۔"
        ]
    }
}

st.sidebar.header("Options")
category = st.sidebar.selectbox("Category", list(poetry.keys()))
language = st.sidebar.radio("Language", ["Roman Urdu", "English", "Urdu"])

if st.sidebar.button("🎲 Random Poem"):
    poem = random.choice(poetry[category][language])
    st.text_area("Poem", poem, height=120)

    if st.button("❤️ Add to Favorites"):
        if poem not in st.session_state.favorites:
            st.session_state.favorites.append(poem)

st.subheader("⭐ Favorites")
if st.session_state.favorites:
    for fav in st.session_state.favorites:
        st.text(fav)
    favs = "\n\n---\n\n".join(st.session_state.favorites)
    st.download_button("Download Favorites", favs, "favorites.txt")
else:
    st.info("No favorites yet.")
