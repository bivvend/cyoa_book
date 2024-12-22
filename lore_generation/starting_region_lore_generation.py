from utils import generate_text
import os

writing_guidelines_1 = "Write a detailed lore for the starting area for a fantasy adventure story"
writing_guidelines_2 = "Use the global lore below to produce a thematically and logically consistent starting area for the adventure in one of the home regions of the races mentioned in the lore."

def generate_starting_region_lore(global_lore, save = True):
    """
    Generates lore for a the region in which the adventure happens.
    """
    prompt = f"{writing_guidelines_1} \n. {writing_guidelines_2} \n\n. {global_lore}"

    response = generate_text.generate_text(prompt)
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)

        with open(txt_file, 'w') as f:
            f.write(response)

    return response
    