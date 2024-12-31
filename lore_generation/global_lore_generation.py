from utils import generate_text, expected_json_structures
import os
import json

start_prompt = (
    "Write a detailed lore for a fantasy world. The world is not called Eldoria! "
    "It should be loosely based on Tolkien with the main races being essentially humanoid. "
    "Include detailed descriptions of the races and include their home area and a description of it."
    "You MUST generate at least 5 different races."
    "One of the races should be Humans, but you can add your own twist to them."
    "The races should follow the typical fantasy tropes, but you can add your own twist to them."
)

style_prompt = (
    "The writing style should be verbose and fluid. "
    "The descriptions should be around 100 words long. "
    "The writing style of Tolkien would fit well."
)

structuring_prompt = (
    f"The response MUST be in json format so that it can be read by a python program. "
    f"Please fill the structure below with the generated data. You are able to add elements "
    f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
    f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
    f"{expected_json_structures.expected_structure_world}"
)

def generate_global_lore(save=True):
    """
    Generates global lore for the game world from the given prompt.
    The prompt is asked to follow a structuring prompt to enforce json
    The writing style is guided by a style prompt
    """
    response = generate_text.generate_text(
        f"{start_prompt}\n{style_prompt}\n{structuring_prompt}"
    )
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = os.path.join(BASE_DIR, "../test_data/world_lore.txt")

        with open(txt_file, 'w') as f:
            f.write(response)

    return response

def extract_races(json_lore):
    """
    Returns races from given text based on the defined global delimiters
    """
    # Implementation of extract_races function
