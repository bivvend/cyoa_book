import json
from utils import generate_text, story_structrures


def generate_map_json( plot_json, events_json, region_lore_json, area_number, model = "gpt-4o-mini"):
    """
    Fills a JSON structure to define the map of an area beased on the location of events.
    """
    area_name = region_lore_json["starting_area"]["notable_locations"][area_number]["name"]
    events_text = json.dumps(events_json[area_name], indent=4)
    plot_txt = json.dumps(plot_json["areas"][area_number], indent=4)

    area_description = region_lore_json["starting_area"]["notable_locations"][area_number]["description"]

    writing_guidelines_1 = (
        f"You are generating a map for an area in a fantasy story called {area_name}. "
        f"The area is decribed below: \n"
        f"{area_description} \n"
        "The events in the story in this area are defined in the events JSON below. \n"
        f"{events_text}. \n" 
    )
    writing_guidelines_2 = (
        "The area is part of story. The plot of the story for this area is given below in JSON format. \n "
        f"{plot_txt} \n"

        "You need to fill a JSON structure that defines all the locations mentioned and all the paths between them. "
        "Each event has a \"location_within_area\" value.  You need to collect together a unique set of locations and the paths between them. "
        "The idea is that the paths can be inserted between the events every time the story changes location ."

        "The description of the path should be fairly long (say 50 words) so that it can be used for flavour during story generation. "
    )

    writing_guidelines_3 = (
    f"The response MUST be in json format so that it can be read by a python program. "
    f"Please fill the structure below with the generated data. You can and should add elements "
    f"to the lists and modify their contents, but the hierarchical structure must be preserved. "
    f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
    f"{story_structrures.map_structure}"

    )
    
    prompt = (
        f"{writing_guidelines_1}\n"
        f"{writing_guidelines_2}\n"
        f"{writing_guidelines_3}\n"
    )

    return generate_text.generate_text(prompt, model_in=model)

