import json
from utils import generate_text, expected_json_structures

def generate_party(global_lore_json, style_prompt_in, model = "gpt-4o-mini"):
    """
    Generates lore for a specific party in the game.
    """
    try:
        global_lore = json.dumps(global_lore_json, indent=4)
        
        writing_guidelines_1 = (
            f"Write a detailed description for the party of adventurers for a fantasy novel."
            "You can use the lore of the world in the JSON below to get an idea of the setting. "
            "The races of the party members MUST only be taken from the lore of the world. Use the list of "
            "races in the lore of the world JSON below to create the party members."
        )

        style_prompt = (
            "You should also use the prompt below that was used to generate the world JSON to give a thematic style to the party. \n"
            f"{style_prompt_in}\n"

        )
        writing_guidelines_2 = (
            "The description should include the party's composition, their backgrounds, motivations, and potential conflicts."
            "The party should be composed of at least 3 members, but you can add more if you want."
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. "
            f"Please fill the structure below (the party JSON) with the generated data. You are able to add elements "
            f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n\n"
            f"{expected_json_structures.expected_structure_party}"
        )
        
        prompt = (
            f"{writing_guidelines_1}\n\n"
            f"Lore of the world:\n{global_lore}\n\n"
            f"{style_prompt} \n"
            f"{writing_guidelines_2}\n\n"
            f"{structuring_prompt}"      
        )
        return generate_text.generate_text(prompt, model_in=model)
    except Exception as e:
        print(f"Error in generate_party: {e}")
        return None
