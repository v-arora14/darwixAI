from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize
import os
from diffusers import StableDiffusionPipeline
import torch

# Download tokenizer
nltk.download('punkt')

app = Flask(__name__)

# Load model (runs once)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to(device)

# Prompt enhancement
def enhance_prompt(scene, style):
    return f"{style}, highly detailed, cinematic lighting, digital art: {scene}"

@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    scenes = []

    if request.method == "POST":
        text = request.form["text"]
        style = request.form["style"]

        scenes = sent_tokenize(text)[:5]

        os.makedirs("static", exist_ok=True)

        for i, scene in enumerate(scenes):
            prompt = enhance_prompt(scene, style)
            image = pipe(prompt).images[0]

            path = f"static/scene_{i}.png"
            image.save(path)

            images.append(path)

    return render_template("index.html", images=images, scenes=scenes)

if __name__ == "__main__":
    app.run(debug=True)
