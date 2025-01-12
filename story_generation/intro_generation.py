import json
from utils import generate_text, story_structrures

def generate_start_scene_text(global_lore_json, region_lore_json, party_lore_json, first_area_events_json):
    """
    Generates lore for the start scene in the game.
    """
    try:
        # Convert JSON to string
        global_lore_txt = json.dumps(global_lore_json, indent=4)
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)
        first_area_events_txt = json.dumps(first_area_events_json, indent=4)

        # Generate the prompt
        writing_guidelines_1 = (
            "Write a detailed description for the introduction scene of a fantasy story. "
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
            "The party lore JSON below should be used to provide a description of the adventurers. \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = (
            "The scene should set the stage for the events that will unfold in the first area. "
            "The events JSON below should be used to provide details of what the party is about to do "
            "the introduction should lead up to these but not include any of them directly. \n "
            f"{first_area_events_txt} \n"
        )

        writing_guidelines_5 = ( 
            "The scene should describe the party's journey to the starting region. "       
            "The introduction should be around 500 words long. "
        )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
            f"{writing_guidelines_5} \n"
        )

        return generate_text.generate_text(prompt)
    except Exception as e:
        print(f"Error in generate_start_scene_text: {e}")
        return None