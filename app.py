from flask import Flask, render_template, request
import openai
import os
import base64
import uuid
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None

    if request.method == "POST":
        prompt = request.form["prompt"]
        prompt = prompt[:800]

        jung_prompt = f"""
You are a Jungian dream analyst. Interpret the user's dream using Carl Jung's ideas:
archetypes, the shadow, anima/animus, collective unconscious, and individuation.
Focus on symbols, emotions, and psychological meaning.

Dream:
{prompt}
"""

        # -------- TEXT --------
        try:
            response = openai.responses.create(
                model="gpt-4.1-mini",
                input=[
                    {
                        "role": "developer",
                        "content": "You are a Jungian dream analyst. Interpret dreams symbolically using Carl Jung’s psychology. Identify archetypes (Shadow, Anima/Animus, Self, Hero, Trickster), emotional tone, figures, actions, and settings. Explain what these symbols reflect about the dreamer’s unconscious conflicts, desires, and transformations. Write in a soft, mystical, introspective tone."
                    },
                    {
                        "role": "user",
                        "content": jung_prompt
                    }
                ],
                temperature=0.9,
                max_output_tokens=100
            )

            result = response.output_text

        except Exception as e:
            result = f"Text Error: {str(e)}"

        # -------- IMAGE --------
        try:
            image_prompt = f"""Soft, mystical, shadowy surreal dream illustration inspired by Carl Jung.
Symbolic archetypes, subconscious atmosphere, cinematic lighting. Dream content:
{prompt}
"""

            image = openai.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="auto",
                quality="low"
            )

            b64 = image.data[0].b64_json

            # Embed directly (no saving)
            image_url = f"data:image/png;base64,{b64}"

        except Exception as e:
            print("IMAGE ERROR:", e)
            image_url = None

    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)








