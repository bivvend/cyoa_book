import json
from utils import generate_text, expected_json_structures

def generate_main_enemy(region_lore_json, model = "gpt-4o-mini"):
    """
    Generates lore for the main enemy in the story.
    """
    try:
        region_lore = json.dumps(region_lore_json, indent=4)
        region_name = region_lore_json["starting_area"]["name"]
        lair_location = region_lore_json["starting_area"]["notable_locations"][-1]["name"]
        
        writing_guidelines_1 = (
            f"Write a detailed description for the main enemy in a fantasy novel. "
            "You MUST use the lore describing the region below (in JSON format) in which the adventures take place in the JSON below to get an idea of the setting. "
            "The enemy MUST be an extremely powerful being that is a threat to the region. "
            "The enemy should be unique and have a detailed background. "
            "The enemy should be characteristic of the region in which the adventures take place. "
            f"The enemy must live and come from {region_name}. No other places can be mentioned." 
            f"The enemies lair must be in {lair_location}. "
            f"All the places mentiond in the description must be mentioned in the region lore. "
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
        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in generate_main_enemy: {e}")
        return None
