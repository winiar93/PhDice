from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

width, height = 550, 300
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
font_size = 45
font = ImageFont.truetype("fonts/BebasNeue-Regular.ttf", font_size)

icons = {
    "Orientation": "icons/triangular_ruler.png",
    "Color": "icons/artist_palette.png",
    "Shutter speed": "icons/stopwatch.png",
    "Theme": "icons/theme.png",
    "Lens": "icons/glass.png",
    "Days": "icons/calendar.png",
    "Time of Day": "icons/clock.png",
    "Format": "icons/frames.png",
}


def generate_challenge_card(parameters: dict) -> BytesIO:
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    y_offset = 30
    icon_size = 50

    for key, value in parameters.items():
        icon_img = Image.open(icons[key]).convert("RGBA").resize((icon_size, icon_size))
        img.paste(icon_img, (10, y_offset), icon_img)
        draw.text((70, y_offset), f"{key}: {value}", font=font, fill=(0, 0, 0))
        y_offset += 55

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return img_byte_arr
