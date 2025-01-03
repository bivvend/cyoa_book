from utils import generate_text, story_structrures


def generate_initial_event_sequence(region_json, party_json_txt, enemy_json_txt, area_number, threat_severity):
    """
    Generates a sequence of events for the story in this area. 
    Pass the actual json objects for the region
    Pass the string version of the party json and enemy json
    """

    area_name = region_json["starting_area"]["notable_locations"][area_number]["name"]
    writing_guidelines_1 = (
        f"Based on the fanatasy area called {area_name} in a fantasy story, you are to write a sequence of events that will happen to the adventuring party in the area. "

    )

    area_decription = region_json["starting_area"]["notable_locations"][area_number]["description"]
    writing_guidelines_2 = (
        f"Use the area decription below as the prime reference for the events. \n {area_decription}\n "
    )

    writing_guidelines_3 = (
        f"You are also told that the threat severity in the area is {threat_severity}. "
    )

    writing_guidelines_4 = ("The main enemy of the story defined in the enemy JSON below. ")

    if(threat_severity == "Low"):
        writing_guidelines_5 = (
            "The presence of the main enemy should be more hidden and their presence should be hinted at subtly. "
            "You must not reveal the main enemy in the events."
            "Events should be more focused on the party and the environment."
        )
    else:
        writing_guidelines_5 = (
            "The presence of the main enemy should be more overt and they are the main focus of the area. "
            "You should reveal the main enemy in the events."
            "Events should be more focused on the party and the main enemy."
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
        f"Please fill the structure below with the generated data. You can and should add elements "
        f"There should be around 20 events in the sequence. "
        f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
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

