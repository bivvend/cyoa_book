import openai
import json



wrtiting_guidlines = "You are a creative writer generating detailed game lore."

client = openai.OpenAI()



def generate_text(prompt, max_tokens=5000, temperature=0.7):
    """
    Generic function to generate text using OpenAI's ChatGPT API.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role": "user", "content": f"{wrtiting_guidlines}\n\n. {prompt}"}
        ]
    )

    return completion.choices[0].message.content
