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
            f"Only include event from {area_name}. "
            f"Flesh out the \"minor_events_in_area\" for {area_name} to complete all the events you need."
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

            "The plot JSON tracks the staus of the main plot items.  Make sure you follow the status of this item. "
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. "
            f"Please fill the structure below with the generated data. You can and should add elements. "
            
            

            f"There should be around 15-20 events in the sequence. "
            f"Each event should id should be of the form \"event_1\", \"event_2\" etc. "
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            "No values or lists should be empty.  If you don't want to add anything just put \"NA\""
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
    
def regenerate_area_events_based_on_feedback(plot_json, region_json, party_json, enemy_json, all_events_json, threat_severity, area_number, feedback_text , model = "gpt-4o-mini"):
    """
    Regenerates a sequence of events for the story in this area. 
    """
    try:
        # Convert JSON to string
        party_json_txt = json.dumps(party_json, indent=4)
        enemy_json_txt = json.dumps(enemy_json, indent=4)
        plot_json_txt = json.dumps(plot_json, indent = 4)

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
            f"Make sure the events are in a logical order. "
            f"Make sure that all the characters are introduced and object are used in a sensible order. "
        )

        area_decription = region_json["starting_area"]["notable_locations"][area_number]["description"]


        writing_guidelines_3 = (
            f"Previously you used the plot JSON structure defined below as the prime reference for the events. \n {plot_json_txt}\n "
            f"Only include event from {area_name}. "

            f"You also used the area decription below as another reference for the events.\n" 
            f"Area Description: {area_decription}\n "
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
            "You must not change or add characters to the party. "
            f"The inventory of the party should be updated as they progress through the events using the inventory_of_story_items JSON element. "
            f"An item MUST NOT BE removed from the inventory (inventory_of_story_items) unless it is destroyed in the event."
            f"Make sure the items gained in the event are added to the inventory_of_story_items. "
            f""
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. This is the same structure you used before."
            f"Please fill the structure below with the modified events. If you think it would be better to add more events to meet the feedback, please do."
            f"There should be around 25 events in the sequence. "
            f"Each event should id should be of the form \"event_1\", \"event_2\" etc. "
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            "No values or lists should be empty.  If you don't want to add anything just put \"NA\" "
            "Always use , as a delimiter. "
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
    
    

def get_second_critique_on_area_events(all_events_json, region_json, area_number, plot_json, model = "gpt-4o-mini"):
    """
    Returns a more specific critique on the structure and contents of the events in a given area with the input from an overall critique/
    """

    area_name = region_json["starting_area"]["notable_locations"][area_number]["name"]

    previous_events_txt = json.dumps(all_events_json[area_name], indent=4)
    plot_txt = json.dumps(plot_json, indent=4)
 
    writing_guidelines_1  = ("You are a literary critic. Your job is to critique fantasy novels. "
                             "You are given story summaries in JSON format. "
                             "The main requirement of the story is that is has a logical flow of events and good internal consistency. ")
    
    writing_guidelines_2 = ("Below is a JSON stuctrure defining the events in a single area from the story. \n"
                            
                            f"{previous_events_txt} \n"

                            f"You are also given the full plot of the story as JSON that includes other areas below: \n"
                            f"{plot_txt} \n"

                            "How could the events in the story be improved to be more consistent? "
                            "Try and be very specific about improvements and mention events by id e.g. event_1 ."
                            "The critique should be very strong if items are not used properly or forgotten half way through, or if events don't make logical or temporal sense. "
                            "Don't critisise the style of the text or the dramatic content,  just focus on the logic."

                            "You should concentrate on checking if the logic of the events make sense, e.g. does a character do something if they haven't been introduced yet. "
                            "Characters mentioned in events must be introduced somewhere in that area in a previous event. "
                            "Or does an event occur in the wrong place. "
                            "Or is an item forgotten about. "
                            "Be brutal with the critisism! "
                            )
    
    structuring_prompt = (
            "Your response should be in plain text, not JSON. "
    )

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{structuring_prompt}\n"

        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in get_critique_on_single_area_events: {e}")
        return None


def check_final_events(all_events_json, model = "gpt-4o-mini"):
    """
    Returns a more specific critique on the structure and contents of the events in a given area with the input from an overall critique/
    """

    event_txt = json.dumps(all_events_json, indent=4)
 
    writing_guidelines_1  = ("You are reviewing a book plot. Your job is to critique fantasy novel story plans and find problems. "
                             "You are given story summaries listing all the events in JSON format. "
                             "The main requirement of the story is that is has a logical flow of events and good internal consistency. ")
    
    writing_guidelines_2 = ("Below is a JSON stuctrure defining the events for a whole story. The story happens in multiple areas within the same region.\n"
                            
                            f"{event_txt} \n"

                            "Please check the JSON and find logical errors, e.g. characters that are not introduced, items that are not used or repeated place names in two different areas. "
                            "You should be very critical. "
                            "Make explit instruction on what to change. "
                            "DO NOT critisise the writing style or the plot.  You are only to comment on logic errors. "
                            "Don't comment on how to make the story telling better, your comments should be about the ordering and missing or incorrect events."
                            "Deleteing events that don't fit well with the plot and are not important is encouraged. "

                            )
    
    structuring_prompt = (
            "Your response should be in plain text, not JSON, with very excplicit instructions on what to change naming the events by area and event id. "
    )

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{structuring_prompt}\n"

        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in get_critique_on_single_area_events: {e}")
        return None



def regenerate_final_events_from_logic_feedback(all_events_json, feedback_text , model = "gpt-4o-mini"):
    """
    Regenerates a sequence of events for the story.
    """
    try:
        # Convert JSON to string

        previous_events_txt = json.dumps(all_events_json, indent=4)

        writing_guidelines_1 = (
            f"You are an author of well written fantasy stories.  You have generated a set of events for a whole story in JSON format as an outline of the story. "
            f"Previously, you wrote the set of events as an outline for the story in the JSON below: \n"
            f"{previous_events_txt} \n"
        )

        writing_guidelines_2 = (
            f"After writing you received feeback on the logical ordering and content.  You take the feeback very seriously and want to make the events better. "
            f"The feeback you received is below: \n"
            f"{feedback_text}"
            
            f"Please revise the events based on the feedback."
            f"Make sure the events are in a logical order. "
            f"Make sure that all the characters are introduced and object are used in a sensible order. "
            f"Follow the feedback and make all the suggestions it asks for ."
            f"Don't change events that the feedback doesn't want you to change. "
        )

        

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. This is the same structure you used before."
            f"Please fill the structure below with the modified events. If you think it would be better to add more events to meet the feedback, please do."
            f"There should be around 25 events in the sequence. "
            f"Each event should id should be of the form \"event_1\", \"event_2\" etc. "
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            "No values or lists should be empty.  If you don't want to add anything just put \"NA\" "
            "Always use , as a delimiter. "
            f"{story_structrures.event_list_structure}\n"
        )
        
        prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{structuring_prompt}\n"
        )

        return generate_text.generate_text(prompt, max_tokens=10000, model_in= model)
    except Exception as e:
        print(f"Error in generate_area_event_sequence: {e}")
        return None