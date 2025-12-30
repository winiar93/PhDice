import streamlit as st
from utils import generate_challange, generate_seed
from image_generator import generate_challenge_card

st.set_page_config(page_title="PhDice", page_icon="📸")

left, mid, right = st.columns([5, 7, 5])

if "current_img" not in st.session_state:
    st.session_state.current_img = None
    st.session_state.current_id = None

with mid:
    st.markdown("<h1 style='text-align: center;'>PhDice</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: center; color: gray;'>Roll the rules.<br> Shoot the photo.</h3>",
        unsafe_allow_html=True,
    )

    challange_id = st.number_input(
        label="Have a Challenge ID? \n\nEnter it below to see more details."
        "\n\nOtherwise, click 'Generate' to create a new one.",
        min_value=10000,
        max_value=34487,
        value=10000,
        step=1,
    )
    random_seed = challange_id
    if challange_id == 10000:
        random_seed = generate_seed()
    if st.button("Generate challenge!", type="primary", use_container_width=True):
        with st.spinner("Wait for it...", show_time=True):
            result = generate_challange(random_seed)
            image_buffer = generate_challenge_card(result)
            st.image(image_buffer, caption=f"Your challenge ID: {random_seed}")

            st.session_state.current_img = image_buffer
            st.session_state.current_id = random_seed

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
                unsafe_allow_html=True,
            )
        st.download_button(
            label="Download image",
            data=image_buffer,
            file_name=f"PhDice{random_seed}.png",
            mime="image/png",
        )
