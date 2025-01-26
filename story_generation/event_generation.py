import json
from utils import generate_text, story_structrures

def generate_area_event_sequence(plot_json, region_json, party_json, enemy_json, area_number, threat_severity,  model = "gpt-4o-mini"):
    """
    Generates a sequence of events for the story in this area. 
    """
    try:
        # Convert JSON to string
        party_json_txt = json.dumps(party_json, indent=4)
        enemy_json_txt = json.dumps(enemy_json, indent=4)
        plot_json_txt = json.dumps(plot_json, indent=4)

        area_name = region_json["starting_area"]["notable_locations"][area_number]["name"]

        #generate other areas to exclude
        areas_to_exclude = [r["name"] for r in region_json["starting_area"]["notable_locations"] if area_name not in r["name"]]

        writing_guidelines_1 = (
            f"Based on the fanatasy area called {area_name} in a fantasy story, you are to write a sequence of events that will happen to the adventuring party in the area. "
            f"All the events must occur in {area_name}.  If you are aware of other areas in the story, don't use them here."
            f"Do not set any of the events in the other areas below: \n"
            f"{areas_to_exclude} \n"
        )

        writing_guidelines_2 = (
            f"Use the plot JSON structure defined below as the prime reference for the events. \n {plot_json_txt}\n "
            f"Don't include any plot events not in {area_name}. "
            f"Flesh out the \"minor_events_in_area\" to complete all the events you need."
        )

        writing_guidelines_3 = (
            f"You are also told that the threat severity in the area is {threat_severity}. "
        )

        writing_guidelines_4 = ("The main enemy of the story is defined in the enemy JSON below. ")

        if(threat_severity == "Low"):
            writing_guidelines_5 = (
                "The presence of the main enemy should be more hidden and their presence should be hinted at subtly. "
                "Events should be more focused on the party and the environment."
                f"Some of the final events should set up the reason why the party moves to the next area. The reasons for this are covered in the plot you are given. "
                f"However, DO NOT set any of the events in the next area. "
                f"Don't set any of the events in the lair of the enemy (\"lair\" in the enemy JSON). "
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
            f"The inventory of the party should be updated as they progress through the events using the inventory_of_story_items JSON element. "
            f"An item MUST NOT BE removed from the inventory (inventory_of_story_items) unless it is destroyed in the event."
            f"Make sure the items gained in the event are added to the inventory_of_story_items. "
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. "
            f"Please fill the structure below with the generated data. You can and should add elements. "
            
            

            f"There should be around 15-20 events in the sequence. "
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

        print(prompt)

        return generate_text.generate_text(prompt, max_tokens=10000, model_in= model)
    except Exception as e:
        print(f"Error in generate_area_event_sequence: {e}")
        return None

def get_critique_on_events(all_events_json, model = "gpt-4o-mini"):
    """
    Returns a high level critique on the structure and contents of all the generated events. 
    """
    writing_guidelines_1  = ("You are a literary critic. Your job is to critique fantasy novels. "
                             "You are given story summaries in JSON format. "
                             "The main requirement of the story is that is has a logical flow of events and the internal consistency. ")
    writing_guidelines_2 = ("Below is a JSON stuctrure defining the events in a story. "
                            "How could the events in the story be improved to be more dramatic and consistent? "
                            )

    events_txt = json.dumps(all_events_json, indent=4)

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{events_txt}"
        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in get_critique_on_events: {e}")
        return None

def get_critique_on_single_area_events(events_json, overall_critique_txt ,model = "gpt-4o-mini"):
    """
    Returns a more specific critique on the structure and contents of the events in a given area with the input from an overall critique/
    """
    writing_guidelines_1  = ("You are a literary critic. Your job is to critique fantasy novels. "
                             "You are given story summaries in JSON format. "
                             "The main requirement of the story is that is has a logical flow of events and good internal consistency. ")
    writing_guidelines_2 = ("Below is a JSON stuctrure defining the events in a single area from the story. \n"
                            "How could the events in the story be improved to be more dramatic and consistent? "
                            "Try and be very specific about improvements and mention events by id e.g. event_1 ."
                            "The critique should be very strondg if items are not used properly or forgotten half way through, or if events don't make logical or temporal sense. "
                            "Be brutal with the critisism! "
                            )
    
    writing_guidelines_3 = ("To help, you are also given some additional feedback on all the events in the story. "
                            "Use this feedback also to suggest improvements to the events for this area."
                            )

    events_txt = json.dumps(events_json, indent=4)

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{events_txt}"
            f"{writing_guidelines_3}\n"
            f"{overall_critique_txt}"
        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in get_critique_on_single_area_events: {e}")
        return None
    
def regenerate_area_events_based_on_feedback(region_json, party_json, enemy_json, all_events_json, threat_severity, area_number, feedback_text , model = "gpt-4o-mini"):
    """
    Regenerates a sequence of events for the story in this area. 
    """
    try:
        # Convert JSON to string
        party_json_txt = json.dumps(party_json, indent=4)
        enemy_json_txt = json.dumps(enemy_json, indent=4)

        area_name = region_json["starting_area"]["notable_locations"][area_number]["name"]

        previous_events_txt = json.dumps(all_events_json[area_name], indent=4)

        writing_guidelines_1 = (
            f"You are an author of well written fantasy stories.  You have generated a set of events for the area known as {area_name} in the story. "
            f"Previously, you wrote a set of events as an outline for the story in the JSON below: \n"
            f"{previous_events_txt} \n"
        )

        writing_guidelines_2 = (
            f"After writing you received feeback on the events.  You take the feeback very seriously and want to make the events better. "
            f"The feeback you received is below: \n"
            f"{feedback_text} \n"

            f"Please revise the events based on the feedback. You should make the description of the events longer, more detailed and better based on the feedback.\n"
        )

        area_decription = region_json["starting_area"]["notable_locations"][area_number]["description"]

        writing_guidelines_3 = (
            f"Previously you used the area decription below as the prime reference for the events. " 
            f"Keep this as a prime reference, but you can make modifications based on the feedback.  \n Area Description: {area_decription}\n "
        )

        writing_guidelines_4 = (
            f"You are also told that the threat severity in the area is {threat_severity}. "
        )

        writing_guidelines_5 = ("Previously you were told that the main enemy of the story is defined in the enemy JSON below. ")

        if(threat_severity == "Low"):
            writing_guidelines_6 = (
                "The presence of the main enemy should be more hidden and their presence should be hinted at subtly. "
                "Events should be more focused on the party and the environment."
            )
        else:
            writing_guidelines_6 = (
                "The presence of the main enemy should be more overt and they are the main focus of the area. "
                "You should reveal the main enemy in the events."
                "Events should be more focused on the party and the main enemy."
                "The party should be in direct conflict with the main enemy in the final events."
                "The main enemy should be defeated in the final events."
            )

        writing_guidelines_7 = (
            "The party is a group of adventurers that are exploring the area. They are defined in the JSON structure below: \n "
        )

        writing_guidelines_8 = (
            "The party should remain the main focus of the events. "
            "The events should be dangerous and challenging, but the party should be able to overcome them. "
            "You must not change or add characters to the party. "
            f"The inventory of the party should be updated as they progress through the events using the inventory_of_story_items JSON element. "
            f"An item MUST NOT BE removed from the inventory (inventory_of_story_items) unless it is destroyed in the event."
            f"Make sure the items gained in the event are added to the inventory_of_story_items. "
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. This is the same structure you used before."
            f"Please fill the structure below with the modified events. If you think it would be better to add more events to meet the feedback, please do."
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
            f"{writing_guidelines_5}\n"
            f"{enemy_json_txt}\n"
            f"{writing_guidelines_6}\n"
            f"{writing_guidelines_7}\n"
            f"{party_json_txt}\n"
            f"{writing_guidelines_8}\n"
            f"{structuring_prompt}\n"
        )

        return generate_text.generate_text(prompt, max_tokens=10000, model_in= model)
    except Exception as e:
        print(f"Error in generate_area_event_sequence: {e}")
        return None