import json
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
    "starting area for the adventure in one of the notable_locations in the JSON. "
    "Where possible pick an area that is not a forest.  "
)

writing_guidelines_3 = (
    "There MUST be more than 4 notable locations in the area. Each notable location should have 3 or more threats. "
)

writing_guidelines_4 = (
    "The notable_locations you generate are very important and will be used as areas for the adventure. "
    "One area should be a dungeon or tower,  and one should be a town or village. "

    "The sense of peril and danger should increase through the list of notable locations. "
    "The threats in the locations should also increase. The first should be mild and gentle "
    "(but with an ominous presence of danger). The last should be dangerous and terrifying, "
    "suitable for an end-of-story grand confrontation!"

    "All the notable locations MUST be contistent with theme inspired by the name of the area. E.g. if it mountainous all the notable locations should be in and around mountains etc. "


)

def generate_starting_region_lore(global_lore_json, model = "gpt-4o-mini"):
    """
    Generates lore for the region in which the adventure happens.

    Args:
        global_lore (json): The global lore to be used for generating the starting region lore.
        save (bool): Whether to save the generated lore to a file. Default is True.

    Returns:
        str: The generated lore in JSON format.
    """
    try:
        global_lore = json.dumps(global_lore_json, indent=4)
        
        prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n\n"
            f"{global_lore}\n\n"
            f"{writing_guidelines_3}\n"
            f"{writing_guidelines_4}\n"
            f"{structuring_prompt}\n\n"
        )

        response = generate_text.generate_text(prompt, model_in=model)

        return response
    except Exception as e:
        print(f"Error in generate_starting_region_lore: {e}")
        return None