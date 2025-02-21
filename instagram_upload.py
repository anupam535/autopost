from instagrapi import Client
import os

# ✅ Instagram Login Credentials
USERNAME = "its_me.aryan0112"
PASSWORD = "323416"

# ✅ LOGIN TO INSTAGRAM
cl = Client()
cl.login(USERNAME, PASSWORD)
print("✅ Instagram Login Successful!")

# ✅ GET GENERATED IMAGES
IMAGE_DIR = "/content/generated_images"
images = [os.path.join(IMAGE_DIR, img) for img in os.listdir(IMAGE_DIR) if img.endswith(".jpg")]

# ✅ UPLOAD IMAGES ONE BY ONE
for image in images:
    caption = "🚀 AI-Generated Art | #AI #Cyberpunk #DigitalArt"
    cl.photo_upload(image, caption)
    print(f"✅ Uploaded: {image}")

print("🎉 All Images Uploaded to Instagram Successfully!")
