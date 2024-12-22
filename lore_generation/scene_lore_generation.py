from utils import generate_text

writing_guidelines_1 = "Write detailed lore for an scene in the game called "
writing_guidelines_2 = "Use the global lore and the area lore  to produce a thematically and logically consistent scene"
writing_guidelines_3 = "Remember that the scene takes place within the area and the area is within the world.  Try very hard to keep consistency."

def generate_scene_lore(global_lore, area_lore, scene_name):
    """
    Generates lore for a specific scene in the game.
    """
    prompt = f"{global_lore}\n\n. {area_lore}\n\n.  {writing_guidelines_1} {scene_name}. {writing_guidelines_2}.{writing_guidelines_2}"
    return generate_text.generate_text(prompt)