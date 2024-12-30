from utils import generate_text, expected_json_structures

writing_guidelines_1 = "Write a detailed description for the centrl villain/bad guy in a fantasy story"
writing_guidelines_2 = "Use the global lore and the region lore to produce a thematically and logically consistent bad guy"


def generate_scene_lore(global_lore, area_lore, scene_name):
    """
    Generates lore for a specific scene in the game.
    """
    prompt = f"{global_lore}\n\n. {area_lore}\n\n.  {writing_guidelines_1} {scene_name}. {writing_guidelines_2}.{writing_guidelines_2}"
    return generate_text.generate_text(prompt)