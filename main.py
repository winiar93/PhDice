import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from utils import generate_challange, generate_seed
import io

st.set_page_config(page_title="PhDice", page_icon="📸")

max_values = 999

col1, col2, col3 = st.columns([1, 2, 1])

width, height = 550, 300
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 45
font = ImageFont.truetype("fonts/BebasNeue-Regular.ttf", font_size)
img = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

challange_id = 0

icons = {
    'Orientation': 'icons/triangular_ruler.png',
    'Color': 'icons/artist_palette.png',
    'Shutter speed': 'icons/stopwatch.png',
    'Theme': 'icons/theme.png',
    'Lens': 'icons/glass.png',
    'Days': 'icons/calendar.png',
    "Time of Day": "icons/clock.png",
    "Format": "icons/frames.png"
}

left, mid, right = st.columns([5, 7, 5])

with mid:
    st.markdown("<h1 style='text-align: center;'>PhDice</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Roll the rules.<br> Shoot the photo.</h3>", unsafe_allow_html=True)

    challange_id = st.number_input(
    label="Have a Challenge ID? \n\nEnter it below to see more details." \
    "\n\nOtherwise, click 'Generate' to create a new one.",
    min_value=10000,
    max_value=34487,
    value=10000,
    step=1
)   
    random_seed = challange_id
    if challange_id == 10000:
        random_seed = generate_seed()
    if st.button("Generate challenge!", type="primary", use_container_width=True):
        with st.spinner("Wait for it...", show_time=True):
            result = generate_challange(random_seed)
            y = 30
            
            for key, value in result.items():
                icon_img = Image.open(icons[key]).convert("RGBA").resize((50, 50))
                img.paste(icon_img, (10, y), icon_img)
                draw.text((70, y), f"{key}: {value}", font=font, fill=(0, 0, 0))
                y += 55

            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)
            st.image(buf, caption = f"Your challenge ID: {random_seed}")

            hashtag_community = "#PhDice"
            hashtag_id = f"#PhDice{random_seed}"
            st.write("Copy and paste these tags to your post on Instagram or X:")
            st.code(f"{hashtag_community} {hashtag_id}")

            st.markdown(
    f"""
    <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px;">
        <strong>Why use both?</strong><br>
        1. Use <b>{hashtag_community}</b> to join our global gallery.<br>
        2. Use <b>{hashtag_id}</b> to see how others interpreted this specific task!
    </div>
    """, 
    unsafe_allow_html=True
)
        st.download_button(
            label="Download image",
            data=buf,
            file_name=f"PhDice{random_seed}.png",
            mime="image/png",
        )