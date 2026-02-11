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
                size="512x512",
                quality="low"
            )

            b64 = image.data[0].b64_json

            # Embed directly (no saving)
            image_url = f"data:image/png;base64,{b64}"

        except Exception as e:
            print("IMAGE ERROR:", e)
            image_url = None

    return render_template("index.html", result=result, image_url=image_url)












# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = None
#     image_url = None   # <-- ADD

#     if request.method == "POST":
#         prompt = request.form["prompt"]

#         jung_prompt = f"""
# You are a Jungian dream analyst. Interpret the user's dream using Carl Jung's ideas:
# archetypes, the shadow, anima/animus, collective unconscious, and individuation.
# Focus on symbols, emotions, and psychological meaning.

# Dream:
# {prompt}
# """

#         try:
#             # -------- TEXT --------
#             response = openai.responses.create(
#                 model="gpt-4.1",
# #                 
#                 input=[
#                     {
#                         "role": "developer",
#                         "content": "You are a Jungian dream analyst. Interpret dreams symbolically using Carl Jung’s psychology. Identify archetypes (Shadow, Anima/Animus, Self, Hero, Trickster), emotional tone, figures, actions, and settings. Explain what these symbols reflect about the dreamer’s unconscious conflicts, desires, and transformations. Write in a soft, mystical, introspective tone."
#                         # "content": "You are a Jungian psychologist interpreting dreams symbolically."
#                         # "content": "You are a Jungian Dream Analysis Machine. You interpret dreams using Carl Jung’s psychological framework. Focus on symbolic meaning rather than literal events. Identify archetypes (such as the Shadow, Anima/Animus, Self, Hero, Trickster), emotional tone, figures, actions, and settings. Explain what each symbol may represent in the dreamer’s unconscious life. Avoid giving direct advice; instead, reflect possible inner conflicts, desires, and transformations. Write in a soft, mystical, introspective tone as if translating the language of the unconscious mind."

#                     },

#                     {
#                         "role": "user",
#                         "content": jung_prompt
#                     }
#                 ],
#                 temperature=0.9,
#                 max_output_tokens=100
#             )

#             result = response.output_text


#         except Exception as e:
#             result = f"Text Error: {str(e)}"



#     # -------- IMAGE --------
#     image_url = None

#            try:
#     image_prompt = f"""Soft, mystical, shadowy surreal dream illustration inspired by Carl Jung.
#     Symbolic archetypes, subconscious atmosphere, cinematic lighting.Dream content:
# {prompt}
# """

#     image = openai.images.generate(
#         model="gpt-image-1",
#         prompt=image_prompt,
#         size="auto",
#         quality="low"
#     )

#     b64 = image.data[0].b64_json

#     # Embed directly, no saving to disk
#     image_url = f"data:image/png;base64,{b64}"

# except Exception as e:
#     print("IMAGE ERROR:", e)
#     image_url = None


# if __name__ == "__main__":
#     app.run(debug=True)








#    # -------- IMAGE --------
#         image_url = None
#         try:
#           image_prompt = f""" Surreal, symbolic, dreamlike illustration based on this dream: 
# {prompt}
# """

         
#           image = openai.images.generate(
#                 model="gpt-image-1",
#                 prompt=image_prompt,
#                 size="auto",
#                 quality="low"
#             )
          

#           b64 = image.data[0].b64_json
#           img_bytes = base64.b64decode(b64)


#           os.makedirs("static", exist_ok=True)

#           filename = f"{uuid.uuid4()}.png"
#           path = os.path.join("static", filename)

#           with open(path, "wb") as f:
#                 f.write(img_bytes)

#           image_url = "/" + path.replace("\\", "/")

#         except Exception as e:
#             print("IMAGE ERROR:", e)
#             image_url = None

#     return render_template("index.html", result=result, image_url=image_url)



