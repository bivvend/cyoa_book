from lore_generation import area_lore_generation, global_lore_generation, region_lore_generation, party_generation, main_enemy_generation, map_generation, item_generation, character_generation
from story_generation import conversation_generation, event_generation, intro_generation, plot_generation
from utils import agent, conversation_structures, expected_json_structures, story_structrures, structure_verification
import os
import json

OUTPUT_DIR = "output_data"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

WORLD_LORE_FILE = "world_lore.txt"
REGION_LORE_FILE = "starting_region_lore.txt"
PARTY_LORE_FILE = "party.txt"
ALL_EVENTS_FILE = "all_events.txt"
ALL_REFINED_EVENTS_FILE = "all_refined_events.txt"
ALL_FINAL_EVENTS_FILE = "all_final_events.txt"
ALL_REFINED_FINAL_EVENTS_FILE = "all_refined_final_events.txt"
INTRO_FILE = "intro.txt"
BASIC_PLOT_FILE = "basic_plot.txt"
REFINED_PLOT_FILE = "plot.txt"
PLOT_JSON_FILE = "plot_json_file.txt"
REFINED_PLOT_JSON_FILE = "refined_plot_json_file.txt"
PLOT_CRITIQUE_FILE = "plot_critique.txt"
PLOT_STRUCTURE_CRITIQUE_FILE = "plot_structure_critique.txt"
ALL_MAPS_FILE = "all_maps.txt"
ALL_ITEMS_FILE = "all_items.txt"
ALL_CHARACTERS_FILE = "all_characters.txt"

ALL_EVENTS_CRITIQUE_FILE = "all_events_critique.txt"
CRITIQUES_BY_AREA_FILE = "critiques_by_area.txt"

SECOND_ALL_EVENTS_CRITIQUE_FILE = "second_all_events_critique.txt"
SECOND_CRITIQUES_BY_AREA_FILE = "second_critiques_by_area.txt"

FINAL_EVENTS_CRITIQUE_FILE = "final_events_logic_critique.txt"

CHARACTERS_SUB_DIR = "characters"
CONVERSATIONS_LORE_FILE = "conversations.txt"
ENEMY_LORE_FILE = "enemy.txt"
AREAS_SUB_DIR = "areas"
EVENTS_SUB_DIR = "events"
STORY_SUB_DIR = "story_chunks"
CRITIQUE_SUB_DIRECTORY = "critique"
SECOND_CRITIQUE_SUB_DIRECTORY = "second_critique"
REFINED_EVENTS_SUB_DIR = "refined_events"
FINAL_EVENTS_SUB_DIR = "final_events"
MAPS_SUB_DIRECTORY = "maps"
ITEMS_SUB_DIR = "items"

region_flavour_prompt = "A dark dungeon inspired by the Fighting fantasy books."
world_flavour_prompt = "The Fighting Fantasy books by Steven Jackson"

refresh_global_lore = False
refresh_region_lore = False
refresh_party_lore = False
refresh_enemy_lore = False
refresh_plot = False
refresh_plot_critique = False
refresh_refined_plot = False
refresh_plot_structre_file = False
refresh_critique_of_plot_structure_file = False
refresh_plot_structure_after_critique = False
refresh_area_lore = False
refresh_events = False
refresh_conversations = False
refresh_intro = False
refresh_all_events_critique = False
refresh_area_events_critique = False
refresh_refined_events = False


refresh_second_area_events_critique = False
refresh_final_events = False

refresh_final_events_critique = False
refresh_refined_final_events = False

refresh_maps = False
refresh_items = False
refresh_characters = False

#Author configuration

configure_new_assistant = False
create_new_assitant = False
create_new_thread = False
configure_new_vector_store = False
upload_new_files = False
add_new_files_to_vector_store = False

#Critic configuration

cr_configure_new_assistant = False
cr_create_new_assitant = False
cr_create_new_thread = False


#Story generation

write_intro = False
write_events = True

# Instructions for the creative writer agent
instructions = ("You are a creative writer generating beautiful, well written fantasy stories. "
                "You will be given JSON files containing the story's plot, characters, events and setting. "
                "You will create sections of the story for a given range of events in the JSON file. "
                "You will try and keep the content consistent throughout the story by analysis of the previous events. ")

# Instructions for the critic agent
critic_instructions = ("You are a critic of fantasy stories.  "
                "You have been given JSON files containing the story's plot, characters, events and setting. "
                "Your job is to suggest improvements to sections of the story you are given.  Using your knowledge of the events make sure the "
                "story sections are consistent with the plot as you know it. "
                "You also need to suggest improvements to the writing style and help the author make a more interesting and well written story. ")

#Files to upload to the author agent
files_list = [os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, CONVERSATIONS_LORE_FILE),
              os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, ENEMY_LORE_FILE), 
              os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, PARTY_LORE_FILE),  
              os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, ALL_CHARACTERS_FILE), 
              os.path.join(OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, ALL_REFINED_FINAL_EVENTS_FILE),
              os.path.join(OUTPUT_DIR, REGION_LORE_FILE), 
              os.path.join(OUTPUT_DIR, WORLD_LORE_FILE), 
              os.path.join(OUTPUT_DIR, REFINED_PLOT_JSON_FILE), 
              os.path.join(OUTPUT_DIR, MAPS_SUB_DIRECTORY, ALL_MAPS_FILE),
              os.path.join(OUTPUT_DIR, ITEMS_SUB_DIR, ALL_ITEMS_FILE),            
              ]
#Default values for the author if the agent is not to be regenerated
vector_store_id ="vs_faIZLMDu6hQyWA9LiUHKOlYD"  #
assistant_id = "asst_0zO6Lxz1oXJ8NV8zve4cYbZL" #
thread_id= "thread_896SMcVnpavikQ0AYUvZqch1" #

#Default values for the critic if the agent is not to be regenerated
critic_assistant_id = "asst_CG3rGo4zUDN5LXhnezFWFEaX" 
critic_thread_id= "thread_i2F9WCakDNd5SgB3tuFwAZ93" #

gpt_model = "gpt-4o"
author_gpt_model = "gpt-4o-mini"

def generate_global_lore():
    """
    Generates or retrieves global lore for the game world.
    """
    try:
        lore_json = None
        lore_txt = ""
        
        if refresh_global_lore:
            # Generate new global lore
            print("Generating global lore...")
            lore_txt = global_lore_generation.generate_global_lore(input_prompt=world_flavour_prompt, model=gpt_model)
            lore_json = json.loads(lore_txt)
            # Save the generated lore to a file
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, WORLD_LORE_FILE)
            with open(txt_file, 'w') as f:
                f.write(lore_txt)
        else:
            # Read existing global lore from file
            print("Loading global lore...")
            lore_file =  os.path.join(BASE_DIR, OUTPUT_DIR, WORLD_LORE_FILE)
            with open(lore_file, 'r') as f:
                lore_lines = f.readlines()
                for line in lore_lines:
                    lore_txt += line
            lore_json = json.loads(lore_txt)
        # Ensure the lore JSON is not None
        assert lore_json is not None
        # Verify the structure of the lore JSON
        structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)
        print("Global lore passed verification.")
        return lore_json
    except Exception as e:
        print(f"Error in generate_global_lore: {e}")
        return None
    
def generate_region_lore(global_lore_json):
    """
    Generates or retrieves the lore for the region within which the adventure takes place
    """
    try:
        lore_json = None
        lore_txt = ""
        
        if refresh_region_lore:
            # Generate new region lore
            print("Generating region lore...")
            lore_txt = region_lore_generation.generate_starting_region_lore(global_lore_json,  model=gpt_model)
            lore_json = json.loads(lore_txt)
            # Save the generated lore to a file
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REGION_LORE_FILE)
            with open(txt_file, 'w') as f:
                f.write(lore_txt)
        else:
            # Read existing region lore from file
            print("Loading region lore...")
            lore_file =  os.path.join(BASE_DIR, OUTPUT_DIR, REGION_LORE_FILE)
            with open(lore_file, 'r') as f:
                lore_lines = f.readlines()
                for line in lore_lines:
                    lore_txt += line
            lore_json = json.loads(lore_txt)
        # Ensure the lore JSON is not None
        assert lore_json is not None
        # Verify the structure of the lore JSON
        structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_region_for_test)
        print("Region lore passed verification.")
        return lore_json
    except Exception as e:
        print(f"Error in generate_region_lore: {e}")
        return None
    
def generate_party_lore(global_lore_json):
    """
    Generates or retrieves the lore for the adventuring party
    """
    try:
        lore_json = None
        lore_txt = ""
        
        if refresh_party_lore:
            # Generate new party
            print("Generating party...")
            lore_txt = party_generation.generate_party(global_lore_json,  model=gpt_model)
            lore_json = json.loads(lore_txt)
            # Save the generated lore to a file
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR,CHARACTERS_SUB_DIR, PARTY_LORE_FILE)
            with open(txt_file, 'w') as f:
                f.write(lore_txt)
        else:
            # Read existing region lore from file
            print("Loading party...")
            lore_file =  os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR,PARTY_LORE_FILE)
            with open(lore_file, 'r') as f:
                lore_lines = f.readlines()
                for line in lore_lines:
                    lore_txt += line
            lore_json = json.loads(lore_txt)
        # Ensure the lore JSON is not None
        assert lore_json is not None
        # Verify the structure of the lore JSON
        structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_party_for_test)
        print("Party passed verification.")
        return lore_json
    except Exception as e:
        print(f"Error in generate_party_lore: {e}")
        return None

def generate_enemy_lore(region_lore_json):
    """
    Generates or retrieves the lore for the main enemy
    """
    try:
        lore_json = None
        lore_txt = ""
        
        if refresh_enemy_lore:
            # Generate new enemy
            print("Generating enemy...")
            lore_txt = main_enemy_generation.generate_main_enemy(region_lore_json,  model=gpt_model)
            lore_json = json.loads(lore_txt)
            # Save the generated lore to a file
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR,CHARACTERS_SUB_DIR, ENEMY_LORE_FILE)
            with open(txt_file, 'w') as f:
                f.write(lore_txt)
        else:
            # Read existing region lore from file
            print("Loading enemy...")
            lore_file =  os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR,ENEMY_LORE_FILE)
            with open(lore_file, 'r') as f:
                lore_lines = f.readlines()
                for line in lore_lines:
                    lore_txt += line
            lore_json = json.loads(lore_txt)
        # Ensure the lore JSON is not None
        assert lore_json is not None
        # Verify the structure of the lore JSON
        structure_verification.verify_lore_structure(lore_json, expected_json_structures.main_enemy_structure_for_test)
        print("Enemy passed verification.")
        return lore_json
    except Exception as e:
        print(f"Error in generate_enemy_lore: {e}")
        return None

def generate_areas(refined_plot_text, region_lore_json, enemy_lore_json):
    """
    Generates detailed descriptions for areas in the starting region.
    """
    try:
        # We now start using the start region data to create new areas.
        areas = region_lore_json["starting_area"]["notable_locations"]    
        area_description_list = []
        if refresh_area_lore:
            # Delete all the previous areas
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, AREAS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, AREAS_SUB_DIR, f)
                os.remove(file_path)
            count = 0
            
            for area in areas:
                count += 1
                if count < len(areas):
                    threat_severity = "Low"
                else:
                    threat_severity = "High"
                print(f"Generating fuller description of area {area['name']} with threat severity {threat_severity}")
                description = area_lore_generation.generate_area_thematic_description(refined_plot_text, region_lore_json, area["name"], enemy_lore_json, threat_severity)
                area_description_list.append(description)
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, AREAS_SUB_DIR, f"area_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(description)
        else:
            # Load all the area descriptions from file
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, AREAS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "area" in f]
            expected_number = len(files)
            for i in range(0, expected_number):
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, AREAS_SUB_DIR, f"area_{i+1}.txt")
                with open(file_path, 'r') as f:
                    lore_lines = f.readlines()
                    area_description = ""
                    for line in lore_lines:
                        area_description += line
                    area_description_list.append(area_description)
        
        count = 0
        for area_description in area_description_list:
            region_lore_json["starting_area"]["notable_locations"][count]["description"] = area_description
            count += 1
        
        # Check structure still holds
        structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

        # Write back the updated region lore
        file_path = os.path.join(BASE_DIR, OUTPUT_DIR, REGION_LORE_FILE)
        with open(file_path, 'w') as f:
            f.write(json.dumps(region_lore_json, indent=4)) 

        return region_lore_json
    except Exception as e:
        print(f"Error in generate_areas: {e}")
        return None
    
def generate_events(plot_json, region_lore_json, party_json, enemy_json):
    """
    Generates events for the areas in the starting region.
    """
    try:
        # We now start using the start region data to create events
        areas = region_lore_json["starting_area"]["notable_locations"]   

        events_json_list_all_areas = [] 
        all_events = {}    
   
        if refresh_events:
            count = 0  
            # Delete the previous events files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "events" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, f)
                os.remove(file_path)

            for area in areas:
                if count < len(areas) - 1:
                    threat_severity = "Low"
                else:
                    threat_severity = "High"
                print(f"Generating events for area {area['name']} with threat severity {threat_severity}")
                events_list = event_generation.generate_area_event_sequence(plot_json["areas"][count], region_lore_json, party_json, enemy_json, count, threat_severity)
                events_json = json.loads(events_list)
                structure_verification.verify_lore_structure(events_json, story_structrures.event_list_structure_for_test)
                events_json_list_all_areas.append(events_json)        
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, f"events_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(events_list)
                all_events[area["name"]] = events_json
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, ALL_EVENTS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_events, indent=4))
            return all_events
        else:
            # Read existing region lore from file
            print("Loading all events dictionary")
            events_file = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, ALL_EVENTS_FILE)
            events_txt = ""
            with open(events_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    events_txt += line
            all_events = json.loads(events_txt)
            return all_events
    except Exception as e:
        print(f"Error in generate_events: {e}")
        return None
    
def generate_conversations(region_lore_json, party_json, all_events_json):
    """
    Generates or retrieves conversations for the characters in the story.
    """
    try:
        if refresh_conversations:
            print("Generating conversations...")
            conversations = conversation_generation.generate_conversations(region_lore_json, party_json, all_events_json)
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, CONVERSATIONS_LORE_FILE)
            with open(txt_file, 'w') as f:
                f.write(conversations)
            
            conversations_json = json.loads(conversations)
        
        else:
            print("Loading conversations..")
            conv_file = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, CONVERSATIONS_LORE_FILE)
            conv_txt = ""
            with open(conv_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    conv_txt += line
            conversations_json = json.loads(conv_txt)
        
        # Validate the structure of the conversations
        structure_verification.verify_lore_structure(conversations_json, conversation_structures.conversation_structure_for_test) 
        print("Conversations passed verification.")   
        return conversations_json
    except Exception as e:
        print(f"Error in generate_conversations: {e}")
        return None

def generate_introduction(global_lore_json, region_lore_json, party_json, all_events_json):
    """
    Generates or retrieves the introduction text for the story.
    """
    try:
        intro_text = None
        if refresh_intro:
            print(f"Generating introduction...")
            intro_text = intro_generation.generate_start_scene_text(global_lore_json, region_lore_json, party_json)
            assert intro_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, INTRO_FILE)
            with open(txt_file, 'w') as f:
                f.write(intro_text)
        else:
            print("Loading intro text..")
            intro_file = os.path.join(BASE_DIR, OUTPUT_DIR, EVENTS_SUB_DIR, INTRO_FILE)
            intro_text = ""
            with open(intro_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    intro_text += line
        return intro_text
    except Exception as e:
        print(f"Error in generate_introduction: {e}")
        return None

def create_vector_store():
    '''
    Create a new vector store.
    '''
    vector_store_id = agent.create_vector_store("Fantasy story vector store").id
    assert vector_store_id is not None
    return vector_store_id

def check_vector_store(store_id):
    '''
    Checks the vetor store exists
    '''
    vector_store = agent.retrieve_vector_store(store_id)
    assert vector_store is not None
    print(f" Vector store {vector_store.id} found.")

def upload_new_files_to_api(files):
    '''
    Upload files
    '''
    pass

def critique_all_events(all_events_json):
    """
    Generates critique on first pass at events
    """
    try:
        critic_text = None
        
        if refresh_all_events_critique:
            print(f"Generating events critique...")
            critic_text = event_generation.get_critique_on_events(all_events_json, model=gpt_model)
            assert critic_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, ALL_EVENTS_CRITIQUE_FILE)
            with open(txt_file, 'w') as f:
                f.write(critic_text)
        else:
            print("Loading events critique text..")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, ALL_EVENTS_CRITIQUE_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
        return critic_text
    except Exception as e:
        print(f"Error in critique_events: {e}")
        return None
    
def critique_plot(plot_text):
    """
    Generates critique on first pass at plot
    """
    try:
        critic_text = None
        
        if refresh_plot_critique:
            print(f"Generating plot critique...")
            critic_text = plot_generation.critique_plot(plot_text, model=gpt_model)
            assert critic_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, PLOT_CRITIQUE_FILE)
            with open(txt_file, 'w') as f:
                f.write(critic_text)
        else:
            print("Loading plot critique text..")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, PLOT_CRITIQUE_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
        return critic_text
    except Exception as e:
        print(f"Error in critique_plot: {e}")
        return None



def critique_area_events(region_lore_json, all_events_json, all_events_critique_txt):
    """
    Generates critique on an all areas events with feedback from the overall critique.
    """
    try:
        critic_text = None
        all_critiques = {} 
        count = 0
        if refresh_area_events_critique:
            # Delete the previous critique files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "area" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, f)
                os.remove(file_path)
            areas = region_lore_json["starting_area"]["notable_locations"]  
            for area in areas:
                count += 1
                print(f"Generating events critique for {area["name"]}")
                critic_text = event_generation.get_critique_on_single_area_events(all_events_json[area["name"]], all_events_critique_txt, model=gpt_model)
                assert critic_text is not None
            
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, f"area_{count}_critique.txt")
                with open(txt_file, 'w') as f:
                    f.write(critic_text)
                all_critiques[area["name"]] = critic_text
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, CRITIQUES_BY_AREA_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_critiques, indent=4))
            return all_critiques
        else:
            pass
            print("Loading area by area events critique file")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, CRITIQUES_BY_AREA_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
            return json.loads(critic_text)
    except Exception as e:
        print(f"Error in critique_events: {e}")
        return None

def second_critique_area_events(region_lore_json, all_events_json, plot_json):
    """
    Generates a second critique on refined events with more focus on logic.
    """
    try:
        critic_text = None
        all_critiques = {} 
        count = 0
        if refresh_second_area_events_critique:
            # Delete the previous critique files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "area" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, f)
                os.remove(file_path)
            areas = region_lore_json["starting_area"]["notable_locations"]  
            for area in areas: 
                print(f"Generating second events critique for {area["name"]}")
                critic_text = event_generation.get_second_critique_on_area_events(all_events_json, region_lore_json, count, plot_json, model = 'o1-mini') #Reasoning model
                assert critic_text is not None
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, f"second_area_{count}_critique.txt")
                with open(txt_file, 'w') as f:
                    f.write(critic_text)
                all_critiques[area["name"]] = critic_text
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, SECOND_CRITIQUES_BY_AREA_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_critiques, indent=4))
            return all_critiques
        else:
            pass
            print("Loading second area by area events critique file")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, SECOND_CRITIQUES_BY_AREA_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
            return json.loads(critic_text)
    except Exception as e:
        print(f"Error in second_critique_area_events: {e}")
        return None
    



def regenerate_events_from_feedback(plot_json, region_lore_json, party_json, enemy_json, all_events_json, area_by_area_feedback_json, is_final=False):
    """
    Regenerates events for the areas based on the critique
    """
    try:
        # We now start using the start region data to create events
        areas = region_lore_json["starting_area"]["notable_locations"]   

        events_json_list_all_areas = [] 
        all_events = {}    

        if is_final:
            model_to_use = "o1-mini"
        else:
            model_to_use = gpt_model
   
        if (is_final and refresh_final_events) or  (is_final==False and refresh_refined_events):
            count = 0  
            # Delete the previous events files
            if is_final:
                dir = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR)
            else:
                dir = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_EVENTS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "events" in f]
            for f in files:
                if is_final:
                    file_path = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, f)
                else:
                    file_path = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_EVENTS_SUB_DIR, f)
                os.remove(file_path)

            for area in areas:
                if count < len(areas) - 1:
                    threat_severity = "Low"
                else:
                    threat_severity = "High"
                print(f"Regenerating events for area {area['name']} with threat severity {threat_severity}")
                events_list = event_generation.regenerate_area_events_based_on_feedback(plot_json, region_lore_json, party_json, enemy_json, all_events_json, threat_severity, count, area_by_area_feedback_json[area['name']] , model = model_to_use)
                events_json = json.loads(events_list)
                structure_verification.verify_lore_structure(events_json, story_structrures.event_list_structure_for_test)
                events_json_list_all_areas.append(events_json)        
                count += 1
                if is_final:
                    txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, f"final_events_{count}.txt")
                else:
                    txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_EVENTS_SUB_DIR, f"refined_events_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(events_list)
                all_events[area["name"]] = events_json
            if is_final:
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, ALL_FINAL_EVENTS_FILE)
            else:
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_EVENTS_SUB_DIR, ALL_REFINED_EVENTS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_events, indent=4))
            return all_events
        else:
            # Read existing region lore from file
            print("Loading all refined events dictionary")
            if is_final:
                events_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, ALL_FINAL_EVENTS_FILE)
            else:
                events_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_EVENTS_SUB_DIR, ALL_REFINED_EVENTS_FILE)
            events_txt = ""
            with open(events_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    events_txt += line
            all_events = json.loads(events_txt)
            return all_events
    except Exception as e:
        print(f"Error in regenerate_events_from_feedback: {e}")
        return None

def generate_plot(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json):
    """
    Generates a first pass at the plot
    """
    try:
        plot_text = None
        
        if refresh_plot:
            print(f"Generating basic plot...")
            plot_text = plot_generation.generate_plot_summary(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json)
            assert plot_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, BASIC_PLOT_FILE)
            with open(txt_file, 'w') as f:
                f.write(plot_text)
        else:
            print("Loading basic plot text..")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, BASIC_PLOT_FILE)
            plot_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    plot_text += line
        return plot_text
    except Exception as e:
        print(f"Error in generate_plot: {e}")
        return None 

def generate_refined_plot(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json, previous_plot_text, critique_text ):
    """
    Generates a refined plot
    """
    try:
        plot_text = None
        
        if refresh_refined_plot:
            print(f"Generating refined plot...")
            plot_text = plot_generation.generate_refined_plot(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json, previous_plot_text, critique_text, model = gpt_model)
            assert plot_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_PLOT_FILE)
            with open(txt_file, 'w') as f:
                f.write(plot_text)
        else:
            print("Loading refined plot text..")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_PLOT_FILE)
            plot_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    plot_text += line
        return plot_text
    except Exception as e:
        print(f"Error in generate_refined_plot: {e}")
        return None 
       
def generate_plot_structure(region_lore_json, party_lore_json, enemy_lore_json, plot_text):
    """
    Fills the plot structure based on the plot text
    """
    try:
        if refresh_plot_structre_file:
            print("Generating plot structure file...")
            plot_json_txt = plot_generation.convert_plot_to_json_and_fill(region_lore_json, party_lore_json, enemy_lore_json, plot_text,  model = gpt_model)
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, PLOT_JSON_FILE)
            with open(txt_file, 'w') as f:
                f.write(plot_json_txt)
            
            plot_json = json.loads(plot_json_txt)

        else:
            print("Loading plot structure..")
            plot_file = os.path.join(BASE_DIR, OUTPUT_DIR, PLOT_JSON_FILE)
            plot_json_txt = ""
            with open(plot_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    plot_json_txt += line
            plot_json = json.loads(plot_json_txt)
        
        # Validate the structure of the conversations
        structure_verification.verify_lore_structure(plot_json, story_structrures.plot_structure_for_test) 
        print("Plot structure passed verification.")   
        return plot_json
    except Exception as e:
        print(f"Error in generate_plot_structure: {e}")
        return None
    
def generate_refined_plot_structure(region_lore_json, party_lore_json, enemy_lore_json, plot_json, feedback_txt):
    """
    Refines the plot json structure
    """
    try:
        if refresh_plot_structure_after_critique:
            print("Regenerating plot structure file...")
            plot_json_txt = plot_generation.improve_plot_json_based_on_feedback(plot_json, feedback_txt, region_lore_json, party_lore_json, enemy_lore_json,  model = gpt_model)
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_PLOT_JSON_FILE)
            with open(txt_file, 'w') as f:
                f.write(plot_json_txt)
            
            plot_json = json.loads(plot_json_txt)

        else:
            print("Loading refined plot structure..")
            plot_file = os.path.join(BASE_DIR, OUTPUT_DIR, REFINED_PLOT_JSON_FILE)
            plot_json_txt = ""
            with open(plot_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    plot_json_txt += line
            plot_json = json.loads(plot_json_txt)
        
        # Validate the structure of the conversations
        structure_verification.verify_lore_structure(plot_json, story_structrures.plot_structure_for_test) 
        print("Refined plot structure passed verification.")   
        return plot_json
    except Exception as e:
        print(f"Error in generate_refined_plot_structure: {e}")
        return None

def generate_map_json(refined_plot_json, refined_events_json, region_lore_json):
    """
    Generates maps
    """
    try:
        # Using the story structures we try and build "maps" for the story
        areas = region_lore_json["starting_area"]["notable_locations"]   

        maps_json_list_all_areas = [] 
        all_maps = {}    
   
        if refresh_maps:
            count = 0  
            # Delete the previous map files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, MAPS_SUB_DIRECTORY)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "map_area" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, MAPS_SUB_DIRECTORY, f)
                os.remove(file_path)
            count = 0
            for area in areas:
                print(f"Generating map for area {area['name']}")
                map = map_generation.generate_map_json(refined_plot_json, refined_events_json, region_lore_json, count, model=gpt_model)
                map_json = json.loads(map)
                structure_verification.verify_lore_structure(map_json, story_structrures.map_structure_for_test)
                maps_json_list_all_areas.append(map_json)        
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, MAPS_SUB_DIRECTORY, f"map_area_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(map)
                all_maps[area["name"]] = map_json
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, MAPS_SUB_DIRECTORY, ALL_MAPS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_maps, indent=4))
            return all_maps
        else:
            # Read existing region lore from file
            print("Loading all maps")
            maps_file = os.path.join(BASE_DIR, OUTPUT_DIR, MAPS_SUB_DIRECTORY, ALL_MAPS_FILE)
            maps_txt = ""
            with open(maps_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    maps_txt += line
            all_maps = json.loads(maps_txt)
            return all_maps
    except Exception as e:
        print(f"Error in generate_map_json: {e}")
        return None

def generate_items_json(refined_plot_json, refined_events_json, region_lore_json):
    """
    Generates item descriptions
    """
    try:
        # Using the story structures we try and build a list of items for the story
        areas = region_lore_json["starting_area"]["notable_locations"]   

        items_json_list_all_areas = [] 
        all_items = {}    
   
        if refresh_items:
            count = 0  
            # Delete the previous map files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, ITEMS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "items_area" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, ITEMS_SUB_DIR, f)
                os.remove(file_path)
            count = 0
            for area in areas:
                print(f"Generating items for area {area['name']}")
                items = item_generation.generate_item_json(refined_plot_json, refined_events_json, region_lore_json, count, model=gpt_model)
                items_json = json.loads(items)
                structure_verification.verify_lore_structure(items_json, story_structrures.item_structure_for_test)
                items_json_list_all_areas.append(items_json)        
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, ITEMS_SUB_DIR, f"items_area_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(items)
                all_items[area["name"]] = items_json
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, ITEMS_SUB_DIR, ALL_ITEMS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_items, indent=4))
            return all_items
        else:
            # Read existing region lore from file
            print("Loading all items")
            items_file = os.path.join(BASE_DIR, OUTPUT_DIR, ITEMS_SUB_DIR, ALL_ITEMS_FILE)
            items_txt = ""
            with open(items_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    items_txt += line
            all_items = json.loads(items_txt)
            return all_items
    except Exception as e:
        print(f"Error in generate_item_json: {e}")
        return None
    
def generate_characters_json(refined_plot_json, refined_events_json, region_lore_json):
    """
    Generates character descriptions
    """
    try:
        # Using the story structures we try and build a list of characters from the story
        areas = region_lore_json["starting_area"]["notable_locations"]   

        characters_json_list_all_areas = [] 
        all_characters = {}    
   
        if refresh_characters:
            count = 0  
            # Delete the previous map files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "characters_area" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, f)
                os.remove(file_path)
            count = 0
            for area in areas:
                print(f"Generating characters for area {area['name']}")
                characters = character_generation.generate_character_json(refined_plot_json, refined_events_json, region_lore_json, count, model=gpt_model)
                characters_json = json.loads(characters)
                structure_verification.verify_lore_structure(characters_json, story_structrures.character_structure_for_test)
                characters_json_list_all_areas.append(characters_json)        
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, f"characters_area_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(characters)
                all_characters[area["name"]] = characters_json
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, ALL_CHARACTERS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_characters, indent=4))
            return all_characters
        else:
            # Read existing region lore from file
            print("Loading all characters")
            characters_file = os.path.join(BASE_DIR, OUTPUT_DIR, CHARACTERS_SUB_DIR, ALL_CHARACTERS_FILE)
            characters_txt = ""
            with open(characters_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    characters_txt += line
            all_characters = json.loads(characters_txt)
            return all_characters
    except Exception as e:
        print(f"Error in generate_characters_json: {e}")
        return None
    
def critique_plot_structure(plot_structure_json, plot_text):
    """
    Generates critique on first pass at plot
    """
    try:
        critic_text = None
        
        if refresh_critique_of_plot_structure_file:
            print(f"Generating plot structre critique...")
            critic_text = plot_generation.critique_plot_json(plot_structure_json, plot_text, model=gpt_model)
            assert critic_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, PLOT_STRUCTURE_CRITIQUE_FILE)
            with open(txt_file, 'w') as f:
                f.write(critic_text)
        else:
            print("Loading plot structre critique..")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, CRITIQUE_SUB_DIRECTORY, PLOT_STRUCTURE_CRITIQUE_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
        return critic_text
    except Exception as e:
        print(f"Error in critique_plot_structure: {e}")
        return None
    
    
def check_final_events_logic(final_events_json):
    """
    Generates critique on final events for logic errors only
    """
    try:
        critic_text = None
        
        if refresh_final_events_critique:
            print(f"Checking logic of final events...")
            critic_text = event_generation.check_final_events(final_events_json)
            assert critic_text is not None
        
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, FINAL_EVENTS_CRITIQUE_FILE)
            with open(txt_file, 'w') as f:
                f.write(critic_text)
        else:
            print("Loading check on final logic")
            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, SECOND_CRITIQUE_SUB_DIRECTORY, FINAL_EVENTS_CRITIQUE_FILE)
            critic_text = ""
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    critic_text += line
        return critic_text
    except Exception as e:
        print(f"Error in check_final_events_logic: {e}")
        return None


def regenerate_final_events_from_logic_feedback(region_lore_json, all_events_json, logic_feedback_txt, use_o1=False):
    """
    Regenerates events for the areas based on the logic critique
    """
    try:
        # We now start using the start region data to create events
        areas = region_lore_json["starting_area"]["notable_locations"]   

        events_json_list_all_areas = [] 
        all_events = {}    

        if use_o1:
            model_to_use = "o1-mini"
        else:
            model_to_use = gpt_model
   
        if refresh_refined_final_events:
            count = 0  
            # Delete the previous events files
            dir = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR)
            files = os.listdir(dir)
            files = [f for f in files if ".txt" in f and "refined" in f]
            for f in files:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, f)
                os.remove(file_path)

            for area in areas:
                
                print(f"Regenerating refined final events for area {area['name']}")
                events_list = event_generation.regenerate_final_events_from_logic_feedback(all_events_json, area['name'], logic_feedback_txt, model_to_use)
                events_json = json.loads(events_list)
                structure_verification.verify_lore_structure(events_json, story_structrures.event_list_structure_for_test)
                events_json_list_all_areas.append(events_json)        
                count += 1
                txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, f"refined_final_events_{count}.txt")
                with open(txt_file, 'w') as f:
                    f.write(events_list)
                all_events[area["name"]] = events_json

            txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, ALL_REFINED_FINAL_EVENTS_FILE)
            with open(txt_file, 'w') as f:
                f.write(json.dumps(all_events, indent=4))
            return all_events
        else:
            # Read existing region lore from file
            print("Loading all refined final events dictionary")

            events_file = os.path.join(BASE_DIR, OUTPUT_DIR, FINAL_EVENTS_SUB_DIR, ALL_REFINED_FINAL_EVENTS_FILE)
            events_txt = ""
            with open(events_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    events_txt += line
            all_events = json.loads(events_txt)
            return all_events
    except Exception as e:
        print(f"Error in regenerate_final_events_from_logic_feedback: {e}")
        return None

def list_files():
    files = agent.list_files()
    return files.data

if __name__ == "__main__":

    #Create the directories if they don't exist

    global_lore_json = generate_global_lore()
    assert global_lore_json is not None
    region_lore_json = generate_region_lore(global_lore_json)
    assert region_lore_json is not None
    party_lore_json = generate_party_lore(global_lore_json)
    assert party_lore_json is not None
    enemy_lore_json = generate_enemy_lore(region_lore_json)
    assert enemy_lore_json is not None

    #With the bones of the world fleshed out we generate the most important document, the plot!

    plot_text = generate_plot(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json)
    #Generate a critique of the plot
    plot_critique_text = critique_plot(plot_text)
    #Use the critique to improve the plot
    refined_plot_text = generate_refined_plot(global_lore_json, region_lore_json, party_lore_json, enemy_lore_json, plot_text, plot_critique_text)


    #Convert the plot text into a structure
    plot_json = generate_plot_structure(region_lore_json, party_lore_json, enemy_lore_json, refined_plot_text)
    assert plot_json is not None

    #Critique the plot structure
    plot_structure_critique_txt = critique_plot_structure(plot_json, refined_plot_text)

    refined_plot_json = generate_refined_plot_structure(region_lore_json, party_lore_json, enemy_lore_json, plot_json, plot_structure_critique_txt)

    #Generate areas and then modify the region_lore to contain the new descriptions
    region_lore_json = generate_areas(refined_plot_text, region_lore_json, enemy_lore_json)
    assert region_lore_json is not None


    #Generate events from region lore and plot
    all_events_json = generate_events(refined_plot_json, region_lore_json, party_lore_json, enemy_lore_json)
    assert all_events_json is not None


    #Refine structure based on feedback 

    critique_prompt = critique_all_events(all_events_json)

    #Based on the overall feedback critique the events area by area.
    area_by_area_critiques = critique_area_events(region_lore_json, all_events_json, critique_prompt)
    assert area_by_area_critiques is not None

    refined_events_json = regenerate_events_from_feedback(refined_plot_json,region_lore_json, party_lore_json, enemy_lore_json, all_events_json, area_by_area_critiques)
    assert refined_events_json is not None

    #Try and improve event logic again.
    second_critique_all_areas_txt = second_critique_area_events(region_lore_json, refined_events_json, refined_plot_json)

    final_events_json = regenerate_events_from_feedback(refined_plot_json,region_lore_json, party_lore_json, enemy_lore_json, refined_events_json, second_critique_all_areas_txt, is_final=True)

    logic_critique_final_events_txt = check_final_events_logic(final_events_json)

    #Build the final set of events (finally!)
    refined_final_events_json = regenerate_final_events_from_logic_feedback(region_lore_json, final_events_json, logic_critique_final_events_txt, False)



    #PLOT AND EVENTS NOW FIXED
    #generate stores of the maps, items and characters for the region

    all_maps_json = generate_map_json(refined_plot_json, refined_final_events_json, region_lore_json)
    all_items_json = generate_items_json(refined_plot_json, refined_final_events_json, region_lore_json)
    all_characters_json = generate_characters_json(refined_plot_json, refined_final_events_json, region_lore_json)

    #Generate conversations
    conversation_json = generate_conversations(region_lore_json, party_lore_json, refined_final_events_json)
    assert conversation_json is not None

    intro_text = generate_introduction(global_lore_json, region_lore_json, party_lore_json, refined_final_events_json)
    assert intro_text is not None

    author = None
    thread = None
    critic = None
    thread_critic = None
    #If needed we should build a new assistant 
    if configure_new_assistant:
        if configure_new_vector_store:
            vector_store_id = create_vector_store()
        else:
            check_vector_store(vector_store_id)
        if upload_new_files:
            #Check if files are uploaded 
            files = list_files()
            print("Current files:")
            print("---------------")
            for f in files:
                print(f"{f.id} : {f.filename}")
            print("---------------")
            if(len(files) > 0):
                print("Deleteing old files....")
                for f in files:
                    agent.delete_file(f.id)
                    print(f"Deleteing {f.filename}")
                files = list_files()
                assert len(files) == 0
            print("Uploading new files...")
            for f in files_list:
                print(f"Uploading {f}")
                agent.upload_file(f)
            files = list_files()
            assert len(files) == len(files_list)    
            #Just upload to API
        if add_new_files_to_vector_store:
            files = list_files()
            v_files = agent.list_files_in_vector_store(vector_store_id)
            #Remove all the files in the vector store
            print("Current files in vector store:")
            print("---------------")
            for f in v_files:
                print(f"File: {f.id}")
            print("---------------")
            if(len(v_files) > 0):
                print("Removing old vector store files....")
                for f in v_files:
                    agent.remove_file_from_vector_store(vector_store_id, f.id)
                    print(f"Removing {f.id}")
                v_files = agent.list_files_in_vector_store(vector_store_id)
                assert len(v_files) == 0
            print("Adding new files...")
            for f in files:
                print(f"Adding file {f.id} : {f.filename} to vector store {vector_store_id} ")
                agent.add_file_to_vector_store(vector_store_id, f.id)
            v_files = agent.list_files_in_vector_store(vector_store_id)
            assert len(v_files) == len(files_list)
        if create_new_assitant:
            #Create the new assistant
            author = agent.create_author("Fantasy author", instructions, vector_store_id)
            assistant_id = author.id
            print(assistant_id)
        else:
            author = agent.retrieve_author(assistant_id)
            print(f"Author (assistant) id = {assistant_id}")
        assert author is not None
        if create_new_thread:
            print("Creating new thread...")
            thread = agent.create_thread()
            assert thread is not None
            thread_id = thread.id
            print(f"New thread = {thread_id}")
        else:
            thread = agent.retrieve_thread(thread_id)
            assert thread is not None
            print(f"Thread {thread_id} found.")
        #Set model 
        print(f"Setting author {assistant_id} to model {author_gpt_model}")
        agent.set_author_model(assistant_id,author_gpt_model)
    else:
        author = agent.retrieve_author(assistant_id)
        assert author is not None
        print(f"Author (assistant) id = {assistant_id} found.")
        thread = agent.retrieve_thread(thread_id)
        assert thread is not None
        print(f"Thread {thread_id} found.")


    #If needed we should build a new critic
    if cr_configure_new_assistant:
        if cr_create_new_assitant:
            #Create the new assistant
            critic = agent.create_author("Fantasy critic", critic_instructions, vector_store_id)
            critic_assistant_id = critic.id
            print(critic_assistant_id)
        else:
            critic = agent.retrieve_author(critic_assistant_id)
            print(f"Critic (assistant) id = {critic_assistant_id}")
        assert critic is not None
        if cr_create_new_thread:
            print("Creating new critic thread...")
            thread_critic = agent.create_thread()
            assert thread_critic is not None
            critic_thread_id = thread_critic.id
            print(f"New critic thread = {critic_thread_id}")
        else:
            thread_critic = agent.retrieve_thread(critic_thread_id)
            assert thread_critic is not None
            print(f"Thread {critic_thread_id} found.")
        #Set model 
        print(f"Setting critic {critic_assistant_id} to model {author_gpt_model}")
        agent.set_author_model(critic_assistant_id,author_gpt_model)
    else:
        critic = agent.retrieve_author(critic_assistant_id)
        assert critic is not None
        print(f"Critic (assistant) id = {critic_assistant_id} found.")
        thread_critic = agent.retrieve_thread(critic_thread_id)
        assert thread_critic is not None
        print(f"Thread {thread_critic.id} found.")

    #Write the intro
    if write_intro:
        #Extract the name of the first area
        area_name =  region_lore_json["starting_area"]["notable_locations"][0]["name"]


        #Use the critic to comment on the intro we already have.
        critic_guidlines_1 = (
            "You are given the text below to write a critisim of: \n"
            f"{intro_text} \n "

            "Your response should include ways in which the writing quality could be improved. "
        )

        critic_guidlines_2 = ( 
            "Your response should also comment on the time line based on the following important points: \n"
            f"The events in the text should lead up to \"event_1\" for {area_name} as described in \"all_events.txt\". "
            f"The party have never met any of the other characters described in \"all_characters.txt\" so the text mustn't mention any of them. "
            f"The party have not heard of any of the items in \"all_items.txt\" so it mustn't mention them. "
            f"The party have never visited any of the locations in \"all_maps.txt\" so the text shouldn't mention them. "
        )

        message = agent.create_message(critic_guidlines_1 + critic_guidlines_2, critic_thread_id)
        assert message is not None
        response_2 = agent.start_run(critic_thread_id, critic_assistant_id)
        assert response_2 is not None
        print(response_2)

        # Generate the prompt
        writing_guidelines_1 = (
            "You wrote a detailed introduction scene for the story below:\n  "
            f"{intro_text}\n"

            "Based on this you received the feedback below from a critic: \n"
            f"{response_2} \n"

        )


        writing_guidelines_2 = (
            "You must rewrite your scene based on the feeback. "
            "Try and address all the points raised."
            "You should increase the length of the text to around 600-1000 words by adding much more description of the scenery and more conversation. "
        )

        prompt = (
            f"{writing_guidelines_1} \n"
            f"{writing_guidelines_2} \n"
        )

        message = agent.create_message(prompt, thread_id)
        assert message is not None
        response_3 = agent.start_run(thread_id, assistant_id)
        assert response_3 is not None
        print(response_3)

        txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, STORY_SUB_DIR, "intro.txt")
        with open(txt_file, 'w') as f:
            f.write(response_3)
        intro_text = response_3
    else: 
        intro_text = ""
        txt_file = os.path.join(BASE_DIR, OUTPUT_DIR, STORY_SUB_DIR, "intro.txt")
        with open(txt_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                intro_text += line 
        print("Intro text reloaded.")
    if write_events:
        response = intro_text
        print("Writing events...")
        area_count = 0
    
        areas = region_lore_json["starting_area"]["notable_locations"]
        for area in areas[0:1]:
            event_count = 0
            
            for event in  refined_final_events_json[areas[area_count]["name"]]["events"][0:10]:
                file_path = os.path.join(BASE_DIR, OUTPUT_DIR, STORY_SUB_DIR, f"area_{area_count+1}_event_{event_count+1}.txt")
                print(file_path)

                print(f"Writing event {event_count+1}...")

                writing_guide_line_1 = (
                    "The previous scene in the story is given below: \n\n"
                    f"{response} \n\n"

                    "Now write a scene for the next event in the series described by the JSON below: \n\n"
                    f"{event} \n\n"
                    "You must not add anything other than what is described in the event JSON. "
                    "In the new scence link directly with the previous scene by continuing from the last sentence. " 
                    "If the two locations for the previous scene and the new event are different, describe how the party got to the new location. "
                    f"\"all_maps.txt \" describes the paths between different locations.  Use this to add detail to the transitions.  "      

                )

                writing_guide_line_2 = (
                    f"Where possible add a converstion from \"conversations.txt\" during the event. \n"
                    f"The description should not be too dramatic and does not need to end with a heroic line of what may come next.  It is a description in the middle of a story."
                    f"Only include utf-8 characters in the response. \n"
                    f"The events in \"all_events.txt\" are in JSON format. The order of events in the lists for each area are in chronological order. "
                    f"You must not describe any events or objects or NPCs that have not happend yet in the order defined in \"all_events.txt.\" "
                    f"Don't rely on objects not listed in the \"all_items.txt\" listed in the event JSON."
                )

                print(writing_guide_line_1 + "\n" + writing_guide_line_2)

                message = agent.create_message(writing_guide_line_1 + "\n" + writing_guide_line_2, thread_id)
                assert message is not None
                response = agent.start_run(thread_id, assistant_id)
                assert response is not None
                #print(response)

                with open(file_path, 'w', encoding="utf-8") as f:
                    f.write(response)

                agent.delete_messages(thread_id)

                event_count += 1
            area_count += 1 
        
            
            

            
    

