import json
from utils import generate_text, story_structrures

def generate_start_scene_text(global_lore_json, region_lore_json, party_lore_json, model = "gpt-4o-mini"):
    """
    Generates lore for the start scene in the game.
    """
    try:
        # Convert JSON to string
        global_lore_txt = json.dumps(global_lore_json, indent=4)
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)

        #Extract the name of the first area
        area_name =  region_lore_json["starting_area"]["notable_locations"][0]["name"]


        # Generate the prompt
        writing_guidelines_1 = (
            "Write a detailed introduction scene of a fantasy story. "
            "The scene should describe the starting point of the adventure and how the party got there. "
            "The world lore JSON below should be used to provide context for the scene. \n"
            f"{global_lore_txt} \n"
        )

        writing_guidelines_2 = (
            "Within the world, the scene should take place in the starting region. "
            "The starting region lore JSON below should be used to provide context for the scene. \n"
            f"{region_lore_txt} \n"
        )

        writing_guidelines_3 = (
            "The scene should introduce the party of adventurers and decribe why they are embarking on the adventure. "
            "The text MUST introduce the main characters in the party and provide a sense of the world they inhabit. "
            "Don't make the party introduction a simple list of the characters one by one, you must introduce them subtly, via events or conversations. "
            "The party lore JSON below should be used to provide a description of the adventurers. \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = ( 
            f"The scene should describe the party's physical and mental journey to the starting region and why they are going to {area_name}. "
            f"It MUST end as they arrive at {area_name}, not describe any actions in {area_name}. " 
            "The introduction should be around 500 words long. "
        )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
        )

        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in generate_start_scene_text: {e}")
        return None