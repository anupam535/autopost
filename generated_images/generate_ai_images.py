import os
import cv2
import torch
from PIL import Image
from diffusers import StableDiffusionXLImg2ImgPipeline

# ✅ CONFIGURATION
HF_TOKEN = "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"  # Hugging Face ka API Token
FACE_IMAGE_PATH = "reference_face.jpg"  # Aapka face swap ke liye reference image
PROMPT = "A highly detailed cinematic portrait of a futuristic girl with cyberpunk neon lighting, ultra-realistic, 1080p, masterpiece."
OUTPUT_DIR = "/content/generated_images"

# ✅ CHECK REFERENCE FACE IMAGE
if not os.path.exists(FACE_IMAGE_PATH):
    raise FileNotFoundError("❌ ERROR: Reference face image is missing! Upload 'reference_face.jpg' before running the script.")

# ✅ CREATE OUTPUT DIRECTORY
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ LOAD REFERENCE FACE IMAGE
ref_face = cv2.imread(FACE_IMAGE_PATH)
ref_face = cv2.cvtColor(ref_face, cv2.COLOR_BGR2RGB)
ref_face_pil = Image.fromarray(ref_face)
print("✅ Reference Face Loaded Successfully!")

# ✅ LOAD AI MODEL (Colab Compatible)
pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl",
    torch_dtype=torch.float16,
    use_safetensors=True
).to("cuda" if torch.cuda.is_available() else "cpu")

print("✅ AI Model Loaded Successfully!")

# ✅ GENERATE 5 IMAGES
generated_images = []
for i in range(5):
    print(f"🚀 Generating Image {i+1}...")
    generated_image = pipe(PROMPT, image=ref_face_pil, num_inference_steps=30, guidance_scale=7.5).images[0]
    
    output_path = os.path.join(OUTPUT_DIR, f"generated_image_{i+1}.jpg")
    generated_image.save(output_path)
    generated_images.append(output_path)
    print(f"✅ Image {i+1} Saved: {output_path}")

print("🎉 All 5 images generated successfully!")
