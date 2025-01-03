from utils import generate_text, expected_json_structures
import os

# Region is the starting area for the quests
# Only one exists

writing_guidelines_1 = (
    "Write a detailed description/lore for an area of a fantasy story, "
    "it should focus on key elements that immerse the reader and provide "
    "a rich foundation for the adventure. This includes the setting’s environment, "
    "important locations, notable NPCs (non-player characters), factions, quests, "
    "and potential threats."
)

structuring_prompt = (
    f"The response MUST be in json format so that it can be read by a python program. "
    f"Please fill the structure below with the generated data. You can and should add elements "
    f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
    f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
    f"{expected_json_structures.expected_structure_region}"
)

writing_guidelines_2 = (
    "Also use the global lore below to produce a thematically and logically consistent "
    "starting area for the adventure in one of the home regions of the races mentioned in the lore. "
)

writing_guidelines_3 = (
    "There MUST be more than 6 notable locations in the area. Each notable location should have 3 or more threats. "
)

writing_guidelines_4 = (
    "The sense of peril and danger should increase through the list of notable locations. "
    "The threats in the locations should also increase. The first should be mild and gentle "
    "(but with an ominous presence of danger). The last should be dangerous and terrifying, "
    "suitable for an end-of-story grand confrontation!"
)

def generate_starting_region_lore(global_lore, save=True):
    """
    Generates lore for the region in which the adventure happens.

    Args:
        global_lore (str): The global lore to be used for generating the starting region lore.
        save (bool): Whether to save the generated lore to a file. Default is True.

    Returns:
        str: The generated lore in JSON format.
    """
    prompt = (
        f"{writing_guidelines_1}\n"
        f"{writing_guidelines_2}\n\n"
        f"{global_lore}\n\n"
        f"{writing_guidelines_3}\n"
        f"{writing_guidelines_4}\n"
        f"{structuring_prompt}\n\n"

    )

    response = generate_text.generate_text(prompt)
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = os.path.join(BASE_DIR, "../test_data/starting_region_lore.txt")

        with open(txt_file, 'w') as f:
            f.write(response)

    return response