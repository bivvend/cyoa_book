import json
from utils import generate_text, expected_json_structures

global_writing_guidelines_1 = (
    "It should focus on key elements that immerse the reader and provide a rich foundation for the adventure. "
    "This includes the environment, important locations, notable NPCs (non-player characters), and potential threats."
)
global_writing_guidelines_2 = "The description should be around 500 words long."

def generate_area_thematic_description(global_lore_json, region_lore_json, area_name, enemy_lore_json, threat_severity):
    """
    Generates lore for a specific area in the game.
    """

    global_lore = json.dumps(global_lore_json, indent=4)
    region_lore = json.dumps(region_lore_json, indent=4)
    enemy_lore = json.dumps(enemy_lore_json, indent=4)
    
    writing_guidelines_1 = (
        f"Write a detailed description for the area called {area_name} of a fantasy story. "
        "You can use the Starting region JSON below to get an idea of the area."
    )
    writing_guidelines_2 = (
        "Use the global lore (the lore of the wider world) defined in the global lore JSON below to expand on the details. "
        "The starting region lore is more important than the global lore"
    )

    writing_guidelines_3 = (
        "One of the main threats in the region is the main enemy. "
        "The main enemy is defined in the enemy JSON below:"  
        f"You are also told that the threat severity {threat_severity}. "
        "If the treat severity is High, the presence of the main enemy should be more overt and they are the main focus of the area. "
        "If the threat severity is Low, the main enemy should be more hidden and their presence should be hinted at subtly. "
    )

    writing_guidelines_4 = (
        "You MUST include the main enemy in the area description. "   
    )
    
    prompt = (


        f"{writing_guidelines_1}\n"
        f"Starting region lore JSON: \n {region_lore}\n\n"
        f"{writing_guidelines_2}\n"
        f"Global lore JSON: \n {global_lore}\n\n"
        f"{writing_guidelines_3}\n\n"
        f"Enemy JSON:\n{enemy_lore}\n"
        f"{writing_guidelines_4}\n"
        f"{global_writing_guidelines_1}\n"
        f"{global_writing_guidelines_2}\n"

    )
    return generate_text.generate_text(prompt)

