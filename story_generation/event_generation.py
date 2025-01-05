import json
from utils import generate_text, story_structrures


def generate_area_event_sequence(region_json, party_json, enemy_json, area_number, threat_severity, previous_events_json=None, next_area=None):
    """
    Generates a sequence of events for the story in this area. 
    Pass the actual json objects for the region
    Pass the string version of the party json and enemy json
    """
    # Convert JSON to string
    party_json_txt = json.dumps(party_json, indent=4)
    enemy_json_txt = json.dumps(enemy_json, indent=4)
    if previous_events_json is not None:
        previous_events_txt = json.dumps(previous_events_json, indent=4)
    else:
        previous_events_txt = ""

    area_name = region_json["starting_area"]["notable_locations"][area_number]["name"]
    writing_guidelines_1 = (
        f"Based on the fanatasy area called {area_name} in a fantasy story, you are to write a sequence of events that will happen to the adventuring party in the area. "

    )

    if previous_events_json is not None:
        writing_guidelines_1 += (
            f"The events should be a continuation of the previous events defined in the JSON below. "
            f"Previous events: {previous_events_txt}\n\n"
        )

    area_decription = region_json["starting_area"]["notable_locations"][area_number]["description"]
    writing_guidelines_2 = (
        f"Use the area decription below as the prime reference for the events. \n {area_decription}\n "
    )

    writing_guidelines_3 = (
        f"You are also told that the threat severity in the area is {threat_severity}. "
    )

    writing_guidelines_4 = ("The main enemy of the story is defined in the enemy JSON below. ")

    if(threat_severity == "Low"):
        writing_guidelines_5 = (
            "The presence of the main enemy should be more hidden and their presence should be hinted at subtly. "
            "Events should be more focused on the party and the environment."
            f"The events for the area should be finished with the party leaving the area to go to {next_area}."
        )
    else:
        writing_guidelines_5 = (
            "The presence of the main enemy should be more overt and they are the main focus of the area. "
            "You should reveal the main enemy in the events."
            "Events should be more focused on the party and the main enemy."
            "The party should be in direct conflict with the main enemy in the final events."
            "The main enemy should be defeated in the final events."
        )


    
    writing_guidelines_6 = (
        "The party is a group of adventurers that are exploring the area. They are defined in the JSON structure below. "

    )

    writing_guidelines_7 = (
        "The party should be the main focus of the events. "
        "The events should be dangerous and challenging, but the party should be able to overcome them. "
        "You must not change or add characters to the party. "
    )

    structuring_prompt = (
        f"The response MUST be in json format so that it can be read by a python program. "
        f"Please fill the structure below with the generated data. You can and should add elements. "
        f"The inventory of the party should be updated as they progress through the events using the inventory_of_story_items JSON element."
        f"An item cannot be removed from the inventory unless it is used in the event."
        f"There should be around 25 events in the sequence. "
        f"Each event should id should be of the form \"event_1\", \"event_2\" etc. "
        f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
        "All the values in the JSON should be strings enclosed with \"\". \n"
        f"{story_structrures.event_list_structure}\n"
    )
    
    prompt = (


        f"{writing_guidelines_1}\n"
        f"{writing_guidelines_2}\n"
        f"{writing_guidelines_3}\n"
        f"{writing_guidelines_4}\n"
        f"{enemy_json_txt}\n"
        f"{writing_guidelines_5}\n"
        f"{writing_guidelines_6}\n"
        f"{party_json_txt}\n"
        f"{writing_guidelines_7}\n"
        f"{structuring_prompt}\n"

    )

    return generate_text.generate_text(prompt,max_tokens=10000)


def generate_start_scene_events(global_lore_json, region_lore_json, party_lore_json, first_area_events_json):
    """
    Generates lore for the start scene in the game.
    """
    # Convert JSON to string
    global_lore_txt = json.dumps(global_lore_json, indent=4)
    region_lore_txt = json.dumps(region_lore_json, indent=4)
    party_lore_txt = json.dumps(party_lore_json, indent=4)
    first_area_events_txt = json.dumps(first_area_events_json, indent=4)

    # Generate the prompt

    writing_guidelines_1 = (
    "Write a detailed description for the starting scene of a fantasy story. "
    "The scene should describe the starting point of the adventure. "
    "The world lore JSON below should be used to provide context for the scene. \n"
    f"{global_lore_txt} \n"
    )

    writing_guidelines_2 = (
        "Within the world, the scene should take place in the starting region. "
        "The starting region lore JSON below should be used to provide context for the scene. \n"
        f"{region_lore_txt} \n"
    
    )
    writing_guidelines_3 = (
        "The scene should introduce the party of adventurers and hint at why they are embarking on the adventure. "
        "The party lore JSON below should be used to provide context for the scene. \n"
        f"{party_lore_txt} \n"
    )
    writing_guidelines_4 = (
        "The scene should set the stage for the events that will unfold in the first area. "
        "The events JSON below should be used to provide details of what the party is about to do, the new events"
        " you are about to generate should lead up to these. "
        "The new events describe the party's got to this area. \n"
        f"{first_area_events_txt} \n"
    )

    structuring_prompt = (
        f"The response MUST be in json format so that it can be read by a python program. "
        f"Please fill the structure below with the generated data. You can and should add elements. "
        f"There should be around 5 events in the sequence. "
        f"Each event should id should be of the form \"event_1\", \"event_2\" etc. "
        f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
        "All the values in the JSON should be strings enclosed with \"\". \n"
        f"{story_structrures.event_list_structure}\n"
    )

    prompt = (
        f"{writing_guidelines_1} \n"
        f"{writing_guidelines_2} \n"
        f"{writing_guidelines_3} \n"
        f"{writing_guidelines_4} \n"
        f"{structuring_prompt} \n"

    )
    return generate_text.generate_text(prompt)