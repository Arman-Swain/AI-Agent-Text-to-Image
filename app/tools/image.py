import requests
import uuid
import os
import urllib.parse

# -----------------------------
# Resolve project root safely
# -----------------------------
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

# -----------------------------
# Images directory (GLOBAL)
# -----------------------------
IMAGES_DIR = os.path.join(BASE_DIR, "images")

# Create images folder if it doesn't exist
os.makedirs(IMAGES_DIR, exist_ok=True)


def generate_image(prompt: str) -> str:
    """
    Generates an image from text prompt and
    stores it inside /images folder by default.
    Returns absolute image path.
    """

    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    filename = f"image_{uuid.uuid4().hex}.png"
    image_path = os.path.join(IMAGES_DIR, filename)

    with open(image_path, "wb") as f:
        f.write(response.content)

    return image_path
