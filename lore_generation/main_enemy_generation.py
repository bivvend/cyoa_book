import json
from utils import generate_text, expected_json_structures

def generate_main_enemy(region_lore_json):
    """
    Generates lore for the main enemy in the story.
    """

    region_lore = json.dumps(region_lore_json, indent=4)
    
    writing_guidelines_1 = (
        f"Write a detailed description for the main enemy in a fantasy novel."
        "You MUST use the lore describing the region below (in JSON format) in which the adventures take place in the JSON below to get an idea of the setting. "
        "The enemy MUST be a extremely powerful being that is a threat to the region. "
        "The enemy should be unique and have a detailed background."
        "The enemy should be characteristic of the region in which the adventures take place."
    )


    structuring_prompt = (
    f"The response MUST be in json format so that it can be read by a python program. "
    f"Please fill the structure below (the main_enemy JSON) with the generated data. You are able to add elements "
    f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
    f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n\n"
    f"{expected_json_structures.main_enemy_structure}"
)
    
    prompt = (
        f"{writing_guidelines_1}\n\n"
        f"Lore of the region:\n{region_lore}\n\n"
        f"{structuring_prompt}"      
    )
    return generate_text.generate_text(prompt)
