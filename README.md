# Dream Interpreter Jungian AI Web App

This project is a web-based dream interpretation tool built with Flask and the OpenAI API. The application allows users to submit written dreams and receive symbolic analysis informed by basic Jungian psychology. The goal of the project is not to provide literal meanings, but to explore how artificial intelligence can simulate interpretive, reflective, and poetic thinking around subconscious imagery.

## Jungian Prompt Design

The main way that I decided to make the prompt is to try to integrate the ideas from Carl Jung’s theory of the unconscious. The system prompt teaches the model to treat dreams as symbolic narratives rather than factual stories. The AI is instructed to recognize elements such as figures, actions, emotions, and environments as archetypal or psychological symbols.

For example, the prompt encourages the model to interpret characters as aspects of the self, locations as mental states, and recurring objects as symbolic motifs. Instead of giving direct advice, the analysis focuses on reflection: tension, desire, fear, transformation, and inner conflict. This aligns with Jung’s idea that dreams communicate through metaphor rather than logic.

In addition, the language style is shaped to be mystical, soft, and surreal. This supports the idea that dream analysis should feel interpretive rather than mechanical, allowing ambiguity and poetic resonance to remain part of the experience.


## Web App User Guide
1. Open the deployed web app in your browser.

2. Enter a dream description into the text area.

3. Click the submit button.

4. The app sends your dream to the OpenAI API using Flask.

5. The AI returns a symbolic Jungian-style interpretation.

6. The response appears below the input area for reflection.


The interface is designed with a soft, shadowy, and mystical aesthetic to reflect the emotional atmosphere of dreams. Users are encouraged to experiment with different dream fragments, memories, or imagined scenarios to see how symbolism shifts across interpretations.


## Reflection and Future Improvements

I had a lot of problems with my actual Flask and Python, after the class, when I tried to make changes in my app.py. My flask disappeared, it couldn't recognize any of my imports, from flask, openai,dotenv and os. It was working in class, so I had to not fully reinstall, but I had to uninstall and reinstall. I discovered that I could not use the go-live in VS Code just to see if it works and make changes before adding it in render, so I added to use p  instead of the one that VS Code uses.  Another thing I discovered is that with my system, if I made changes or there was an error in my code before I fixed it, it could completely break my Flask connection in the terminal. I had to make sur its fully disconnected and then reconnect it, which was confusing in the beginning. 

One insight that I got from this project is how much meaning can emerge purely from prompt design. I could change a bit, but still have a similar vocabulary used. Could just add or reduce, and I could get completely different structured phrases, which is interesting. By changing how the AI is instructed, the system moves from being a calculator-like responder to something closer to a reflective interpreter. This highlights how AI behaviour is shaped less by intelligence and more by narrative framing.

another problem was that i didnt realise how heavy the images generated where it ended up taking all of my 5 dollars and i had no idea. anyway I still dont know if thats why i am receiving errors the moment i put it render. 

Another takeaway is the tension between structure and ambiguity. Jungian interpretation benefits from openness, yet users often expect concrete answers. Balancing poetic uncertainty with helpful guidance became an important design challenge.
Future improvements could include image-based dream input, memory between sessions, multiple interpretive styles, or visual symbol mapping. The interface could also become more immersive, using animation or sound to deepen the dream-like experience. I would love to have something like moving mist in the background, something that immerses the users more. I already like that my container moves a bit up and down like a very, very subtle breathing, but for me its kidn of calming and feels like a good implementation. 

I would like to be able to allow users to download the images automatically instead of clicking and doing Save As. For me, all images are downloaded automatically in my static folder in my repo, but I didnt fully know how to do it another way, so i would like to edit that in the future. Overall, the project demonstrates how AI can become a creative partner in exploring inner worlds rather than just solving problems.
