from utils import generate_text

writing_guidelines_1 = (
    "Write detailed lore for a scene in the game called "
)
writing_guidelines_2 = (
    "Use the global lore and the area lore to produce a thematically and logically consistent scene."
)
writing_guidelines_3 = (
    "Remember that the scene takes place within the area and the area is within the world. "
    "Try very hard to keep consistency."
)

def generate_scene_lore(global_lore, area_lore, scene_name):
    """
    Generates lore for a specific scene in the game.

    Args:
        global_lore (str): The global lore to be used for generating the scene lore.
        area_lore (str): The area lore to be used for generating the scene lore.
        scene_name (str): The name of the scene.

    Returns:
        str: The generated lore for the scene.
    """
    prompt = (
        f"{global_lore}\n\n"
        f"{area_lore}\n\n"
        f"{writing_guidelines_1} {scene_name}. "
        f"{writing_guidelines_2} "
        f"{writing_guidelines_3}"
    )
    return generate_text.generate_text(prompt)