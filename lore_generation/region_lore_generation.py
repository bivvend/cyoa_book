from utils import generate_text
from utils import expected_json_structures
import os

#Region is the starting area for the quests
#Only one exists

writing_guidelines_1 = "Write a detailed description/lore for an area of a fantasy story, it should focus on key elements that immerse the reader and provide a rich foundation for the adventure. This includes the setting’s environment, important locations, notable NPCs (non-player characters), factions, quests, and potential threats."
structuring_prompt = f"""The response MUST be in json format so that it can be read by a python program.  Please fill the structure below with the generated data.  You can and should add elements to the lists and modify their contents,  but the heirachical structure must be preserved. Do not use the ```json style flag in your response,  I want to load it directly with json.loads\n
{expected_json_structures.expected_structure_region}"""
writing_guidelines_2 = "Also use the global lore below to produce a thematically and logically consistent starting area for the adventure in one of the home regions of the races mentioned in the lore."
writing_guidelines_3 = "There MUST be more than 6 notable locations and more than 6 quests and more than 10 fauna"
writing_guidelines_4 = "The sense of peril and danger should increase through the list of notable locations. The treats in the locations should alse increase. The first should be mild and gentle (but with a ominous presence of danger). The last should be dangerous and terrifing suitable for an end of story grand confrontation!"

def generate_starting_region_lore(global_lore, save = True):
    """
    Generates lore for a the region in which the adventure happens.
    """
    prompt = f"{writing_guidelines_1}\n.{writing_guidelines_2}\n.{writing_guidelines_3}\n. {writing_guidelines_4}\n {structuring_prompt} \n\n. {global_lore}"

    response = generate_text.generate_text(prompt)
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)

        with open(txt_file, 'w') as f:
            f.write(response)

    return response


    