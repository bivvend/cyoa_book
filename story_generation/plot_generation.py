import json
from utils import generate_text, story_structrures

def generate_plot_summary(global_lore_json, style_prompt_in,  region_lore_json, party_lore_json, enemy_lore_json, model = "gpt-4o-mini"):
    """
    Generates the first pass of the plot of the story
    """
    try:
        # Convert JSON to string
        global_lore_txt = json.dumps(global_lore_json, indent=4)
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)
        enemy_lore_txt = json.dumps(enemy_lore_json, indent=4)

        areas_to_include = [r["name"] for r in region_lore_json["starting_area"]["notable_locations"]]

        # Generate the prompt
        writing_guidelines_1 = (
            "You are a fantasy story author writing the plot for a story."
            "The story is set in the world defined in the JSON below. \n World Lore: \n"
            f"{global_lore_txt} \n"
        )

        style_prompt = (
                "You are also given a style prompt to follow below: \n"
                f"{style_prompt_in}\n"
        )

        writing_guidelines_2 = (
            "Within the world, the story should take place in the region defined by the "
            "starting region lore JSON below: \n"
            f"{region_lore_txt} \n"

            f"The notable_locations in the JSON ({areas_to_include}) MUST all be visted in turn. "
            f"The plot must explicitly justify why they move from one area to the next. E.g. they move to {areas_to_include[0]} to  {areas_to_include[1]} because..."
        )

        writing_guidelines_3 = (
            "The party lore JSON below should be used to provide a description of the adventurers. They are the main protagonists in the story : \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = ( 
            "The main enemy in the story is defined in the enemy JSON below: \n "
            f"{enemy_lore_txt} \n"
            f"The enemy's presence should be sublte in the first part of the plot (in {areas_to_include[0]}) and there should be a climatic battle in the last area ({areas_to_include[-1]})"
        )

        writing_guidelines_5 = ( 
            "The plot summary should be around 800 words long and be interesting and novel. "
            "The most important thing is that the plot makes logical sense from start to finish, without any unsolved or incomplete story elements. "
            "The summary should introduce at least one important item in the story that used to defeat the enemy or to progress. "
        )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{style_prompt} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
            f"{writing_guidelines_5} \n"
        )

        print(prompt)

        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in generate_plot_summary: {e}")
        return None
    
def critique_plot(plot_summary_text, model = "gpt-4o-mini"):
    """
    Returns a high level critique on the structure of the plot
    """

    writing_guidelines_1  = ("You are a literary critic. Your job is to critique fantasy novels. Here you are trying to make improvements on the intial plot drafts for a story."
                             "The main requirement of the plot is that is has a logical flow of events and the internal consistency. "
                             "The plot should include multiple regions and give clear indications of why the adventurers move from one area to the next. "
                             "There should be important items that are found at various points and used to defeat the enemy. "
                             "The plot should also be exciting, dramatic and well written. "
                             "You are a very brutal critic and don't try and be nice,  just say strong what is wrong. ")
    
    writing_guidelines_2 = ("Below is a some text defining a plot you are given. "
                            "How could the the story be improved based on the requirements?  : \n"
                            f"{plot_summary_text}"
                            )

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in critique_plot: {e}")
        return None
    

def generate_refined_plot(global_lore_json,style_prompt_in, region_lore_json, party_lore_json, enemy_lore_json, previous_plot_text, critique_text, model = "gpt-4o-mini"):
    """
    Generates the first pass of the plot of the story
    """
    try:
        # Convert JSON to string
        global_lore_txt = json.dumps(global_lore_json, indent=4)
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)
        enemy_lore_txt = json.dumps(enemy_lore_json, indent=4)

        areas_to_include = [r["name"] for r in region_lore_json["starting_area"]["notable_locations"]]

        # Generate the prompt
        writing_guidelines_1 = (
            "You are a fantasy story author writing the plot for a story."
            "The story is set in the world defined in the JSON below. \n World Lore: \n"
            f"{global_lore_txt} \n"
        )

        style_prompt = (
                "You are also given a style prompt to follow below: \n"
                f"{style_prompt_in}\n"
        )

        writing_guidelines_2 = (
            "Within the world, the story should take place in the region defined by the "
            "starting region lore JSON below: \n"
            f"{region_lore_txt} \n"

            f"The notable_locations in the JSON ({areas_to_include}) MUST all be visted in turn. "
            f"The plot must explicitly justify why they move from one area to the next. E.g. they move to {areas_to_include[0]} to  {areas_to_include[1]} because..."
        )

        writing_guidelines_3 = (
            "The party lore JSON below should be used to provide a description of the adventurers. They are the main protagonists in the story : \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = ( 
            "The main enemy in the story is defined in the enemy JSON below: \n "
            f"{enemy_lore_txt} \n"
            f"The enemy's presence should be subtle in the first part of the plot (in {areas_to_include[0]}) and there should be a climatic battle in the last area ({areas_to_include[-1]})"
        )

        writing_guidelines_5 = ( 
            "You previously wrote the plot summary below:  \n"
            f"{previous_plot_text} \n"
            "A critic gave you feedback on the plot and wrote this about it: \n"
            f"{critique_text} \n"
        )

        writing_guidelines_6 = (
            "Please rewrite the plot addressing ALL the concerns raised in the feedback. "
            "Your new plot should be around 1000 words long and be much better written than the original. "
            )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{style_prompt} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
            f"{writing_guidelines_5} \n"
            f"{writing_guidelines_6} \n"
        )


        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in generate_plot_summary: {e}")
        return None
    
def convert_plot_to_json_and_fill(region_lore_json, party_lore_json, enemy_lore_json, plot_text,  model = "gpt-4o-mini"):
    """
    Fills the plot structure with events based on the overall plot
    """
    try:
        # Convert JSON to string
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)
        enemy_lore_txt = json.dumps(enemy_lore_json, indent=4)

        areas_to_include = [r["name"] for r in region_lore_json["starting_area"]["notable_locations"]]
        numberof_area = len(areas_to_include)

        


        writing_guidelines_1 = (
            "Below is the plot outline for an fantsy story: \n"
            f"{plot_text} \n"
        )

        writing_guidelines_2 = (
            "Within the world, the story takes place in the region defined by the "
            "starting region lore JSON below: \n"
            f"{region_lore_txt} \n"
        )

        writing_guidelines_3 = (
            "The party lore JSON below should be used to provide a description of the adventurers who are taking part in the plot. They are the main protagonists in the story and are described in the plot outline too : \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = ( 
            "The main enemy in the story is defined in the enemy JSON below: \n "
            f"{enemy_lore_txt} \n"
            f"The enemy's presence should be subtle in the first part of the plot (in {areas_to_include[0]}) and there should be a climatic battle in the last area ({areas_to_include[-1]})"
        )

        writing_guidelines_4 = ( 
            "You need convert the plot outline into a JSON structure. "
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. "
            f"Please fill the structure below with the generated data. You can and should add elements. "
            f"All the events, enemies and action within the plot should be stored in this structure."

            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            f"{story_structrures.plot_structure}\n"
        )

        writing_guidelines_5 = (
            "For each area please fill the \"minor_events_in_area\" with at least 10 less significant events that are thematically relevant and develop the characters and fill out the plot.  "
            "These extra events should be assiciated with the enemies, areas visited and characters in the area. "

            f"The story has 4 areas (explitily {areas_to_include}). Each area should be its own \"area\" within the structure. "
                
            "There should be one or more main plot item, the status of which is tracked through all the areas. "
            "Don't forget to include this item in all areas. If the party hasn't found it yet, label it as not found."
            "Track any major changes to the status of the party members too, and update this as the story goes on. "
            "Don't remove status changes unless the effect has expired. "
            "The list in the next area should generally have all the status changes from the previous area. "
        )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
            f"{structuring_prompt}\n"
            f"{writing_guidelines_5}"

        )

        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in convert_plot_to_json_and_fill: {e}")
        return None
    
def critique_plot_json(plot_summary_json, plot_summary_text, model = "gpt-4o-mini"):
    """
    Returns a high level critique on the structure of the plot json file. Used to sort the order and check consitency
    """
    plot_json_txt = json.dumps(plot_summary_json, indent=4)

    writing_guidelines_1  = ("You are a literary critic. Your job is to critique fantasy novels. Here you are trying to make improvements on a JSOM structure that defines the plot."
                             "The main requirement of the plot is that is has a logical flow of events and the internal consistency. "
                             "You are a very brutal critic and don't try and be nice,  just say strongly what is wrong. ")
    
    writing_guidelines_2 = ("Below is a some text defining the plot you are given. \n "
                            f"{plot_summary_text}"
                            )
    
    writing_guidelines_2 = ("You are also given a JSON file below describing the plot that also includes many minor events. Please make suggestion (in plain text) on how to improve the structure to make it fit the plot well.  "
                            "Feedback on the ordering of events would be useful. \n"
                            f"{plot_json_txt}"
                            )

    prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
        )
    
    try:
        response = generate_text.critique_text(prompt=prompt, model_in= model)
        return response

    except Exception as e:
        print(f"Error in critique_plot: {e}")
        return None
    
def improve_plot_json_based_on_feedback(plot_json, feedback_txt, region_lore_json, party_lore_json, enemy_lore_json,  model = "gpt-4o-mini"):
    """
    Improves the plot JSON based on feedback 
    """
    try:
        # Convert JSON to string
        region_lore_txt = json.dumps(region_lore_json, indent=4)
        party_lore_txt = json.dumps(party_lore_json, indent=4)
        enemy_lore_txt = json.dumps(enemy_lore_json, indent=4)
        plot_json_txt = json.dumps(plot_json, indent=4)

        areas_to_include = [r["name"] for r in region_lore_json["starting_area"]["notable_locations"]]
        number_of_areas = len(areas_to_include)

        writing_guidelines_1 = (
            "You are a fantasy book author.  Previously you wrote a JSON structure defining the plot of a story. "
            "The JSON you wrote is below: \n"
            f"{plot_json_txt} \n"

        )

        writing_guidelines_2 = (
            "Within the world, the story takes place in the region defined by the "
            "starting region lore JSON below: \n"
            f"{region_lore_txt} \n"
        )

        writing_guidelines_3 = (
            "The party lore JSON below should be used to provide a description of the adventurers who are taking part in the plot. They are the main protagonists in the story and are described in the plot outline too : \n"
            f"{party_lore_txt} \n"
        )

        writing_guidelines_4 = ( 
            "The main enemy in the story is defined in the enemy JSON below: \n "
            f"{enemy_lore_txt} \n"
            f"The enemy's presence should be subtle in the first part of the plot (in {areas_to_include[0]}) and there should be a climatic battle in the last area ({areas_to_include[-1]})"
        )

        writing_guidelines_5 = ( 
            "After writing the JSON you received the feedback on the structure below: \n"
            f"{feedback_txt}"
            "You need modify the data in your JSON structure to fully addess all the feedback and improve the structure. "

            "There should still be at least one main plot item, the status of which is tracked through all the areas. "
            "Don't forget to include this item in all areas. If the party hasn't found it yet, label it as not found."
            "Don't remove status changes unless the effect has expired. "
            "The list in the next area should generally have all the status changes from the previous area. "
        )

        structuring_prompt = (
            f"The response MUST be in the same JSON format that you origionally used (as shown below) so that it can be read by a python program. "
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            f"{story_structrures.plot_structure}\n"
        )


        prompt = (
            f"{writing_guidelines_1} \n"
            f"{writing_guidelines_2} \n"
            f"{writing_guidelines_3} \n"
            f"{writing_guidelines_4} \n"
            f"{writing_guidelines_5} \n"
            f"{structuring_prompt}\n"

        )

        return generate_text.generate_text(prompt, model_in= model)
    except Exception as e:
        print(f"Error in improve_plot_json_based_on_feedback: {e}")
        return None