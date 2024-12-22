from utils import generate_text

writing_guidelines_1 = "Write detailed lore for an area called "
writing_guidelines_2 = "Use the global lore and the name of the area to produce a thematically and logically consistent area"

def generate_area_lore(global_lore, area_name):
    """
    Generates lore for a specific area in the game.
    """
    prompt = f"{global_lore}\n\n. {writing_guidelines_1} {area_name}. {writing_guidelines_2}"
    return generate_text.generate_text(prompt)
