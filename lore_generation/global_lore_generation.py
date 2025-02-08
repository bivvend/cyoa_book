from utils import generate_text, expected_json_structures
import os
import json

default_start_prompt = (
    "Write a detailed lore for a fantasy world. The world is not called Eldoria! "
    "The writing style of Tolkien would fit well."
)

start_prompt = (
    
    "The main races in the world should be essentially humanoid. "
    "Include detailed descriptions of the races and include their home area and a description of it."
    "You MUST generate at least 5 different races."
    "One of the races should be Humans, but you can add your own twist to them."
)

style_prompt = (
    "The writing style should be verbose and fluid. "
    "The descriptions should be around 100 words long. "

)

structuring_prompt = (
    f"The response MUST be in json format so that it can be read by a python program. "
    f"Please fill the structure below with the generated data. You are able to add elements "
    f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
    f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
    f"{expected_json_structures.expected_structure_world}"
)

def generate_global_lore(input_prompt=None, model = "gpt-4o-mini"):
    """
    Generates global lore for the game world from the given prompt.
    The prompt is asked to follow a structuring prompt to enforce json
    The writing style is guided by a input prompt
    """
    if input_prompt is None:
        input_prompt = default_start_prompt

    response = generate_text.generate_text(
        f"{input_prompt}{start_prompt}\n{style_prompt}\n{structuring_prompt}", model_in=model
    )

    return response


