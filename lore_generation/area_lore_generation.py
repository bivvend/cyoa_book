from utils import generate_text, expected_json_structures



global_writing_guidelines_1 = f"It should focus on key elements that immerse the reader and provide a rich foundation for the adventure. This includes the setting’s environment, important locations, notable NPCs (non-player characters), and potential threats."
global_writing_guidelines_2 = "The description should be around 500 words long."

def generate_area_thematic_description(global_lore_json, region_lore_json, area_name):
    """
    Generates lore for a specific area in the game.
    """
    writing_guidelines_1 = f"Write a detailed description for the area called {area_name} of a fantasy story.  You can use the Starting region JSON below to get an idea of the area."
    writing_guidelines_2 = f"Use the global lore and the starting region lore defined in the two JSON structures below.  Don't drift from these, but expand on the details. The starting region lore is more important that the global."
    
    prompt = f"{global_lore_json}\n\n. {writing_guidelines_1}\n {global_writing_guidelines_2}\n {global_writing_guidelines_2} \n {writing_guidelines_2} \n\n Global lore:\n {global_lore_json} \n Starting region lore: \n {region_lore_json}"
    return generate_text.generate_text(prompt)


def refine_thematic_description(curent_item, previous_areas):
    """
    Once the areas are initially defined,  this repass over the data improves the consistency between areas to remove repeats.  By this point we can start ditching the initial lore and just improve internal consistency
    """

    writing_guidelines_1 = f"Below is a detailed description for an area in a fantasy story."

    all_areas_text = "\n".join(previous_areas)
    writing_guidelines_2 = f"Please refine the description. By considering the other areas already defined below:"     
    writing_guidelines_3 = "If you find duplication of NPC or threats between the description and the previous ones, invent new thematically relevant ones rather than reuse. DO NOT USE THE SAME THREAT IF YOU HAVE SEEN IT APPEAR BEFORE"
    writing_guidelines_4 = "Each new description should focus on key elements that immerse the reader and provide a rich foundation for the adventure. This includes the setting’s environment, important locations, notable NPCs (non-player characters), and potential threats."

    prompt = f"{writing_guidelines_1}\n {curent_item} \n {writing_guidelines_2}\n {all_areas_text} {writing_guidelines_3}\n {writing_guidelines_4} {global_writing_guidelines_2}" 
    return generate_text.generate_text(prompt)