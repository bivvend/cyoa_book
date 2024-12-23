from utils import generate_text, expected_json_structures
import os
import json



start_prompt = "Write a detailed lore for a fantasy world. The world is not called Eldoria!It should be loosely based on Tolkien with the main races being essentially humanoid. Include detailed descriptions of the races and include their home area and a decription of it."
style_prompt = "The writing style should be verbose and fluid.  The descriptions should be around 100 words long.  The writing style of Tolkien would fit well."
structuring_prompt = f"""The response MUST be in json format so that it can be read by a python program.  Please fill the structure below with the generated data.  You are able to add elements to the lists and modify their contents,  but the heirachical structure must be preserved. Do not use the ```json style flag in your response,  I want to load it directly with json.loads\n
{expected_json_structures.expected_structure_world}
"""


def generate_global_lore(save=True):
    """
    Generates global lore for the game world from the given prompt.
    The prompt is asked to follow a structuring prompt to enforce json
    The writing style is guided by a style prompt
    """
    response = generate_text.generate_text(f"{start_prompt}\n. {style_prompt}\n {structuring_prompt}")
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)

        with open(txt_file, 'w') as f:
            f.write(response)

    return response

def extract_races(json_lore):
    '''
    Returns races from given text based on the defined global delimiters
    '''
   
    

