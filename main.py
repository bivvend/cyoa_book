from lore_generation import area_lore_generation, global_lore_generation, region_lore_generation, party_generation, main_enemy_generation
from story_generation import conversation_generation, event_generation, intro_generation
from utils import agent, conversation_structures, expected_json_structures, story_structrures, structure_verification
import os
import json

OUTPUT_DIR = "output_data"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

WORLD_LORE_FILE = "world_lore.txt"
REGION_LORE_FILE = "starting_region_lore.txt"
PARTY_LORE_FILE = "party.txt"
ALL_EVENTS_FILE = "all_events.txt"
INTRO_FILE = "intro.txt"

CHARACTERS_SUB_DIR = "characters"
CONVERSATIONS_LORE_FILE = "conversations.txt"
ENEMY_LORE_FILE = "enemy.txt"
AREAS_SUB_DIR = "areas"
EVENTS_SUB_DIR = "events"
STORY_SUB_DIR = "story_chunks"

region_flavour_prompt = "A dark dungeon inspired by the Fighting fantasy books."
world_flavour_prompt = "The Fighting Fantasy books by Steven Jackson"

refresh_global_lore = False
refresh_region_lore = False
refresh_party_lore = False
refresh_enemy_lore = False
refresh_area_lore = False
refresh_events = False
refresh_conversations = False
refresh_intro = False

configure_new_assistant = True
configure_new_thread = True
configure_new_vector_store = False
upload_new_files = True


# Instructions for the creative writer agent
instructions = ("You are a creative writer generating beautiful, well written fantasy stories. "
                "You will be given JSON files containing the story's plot, characters, events and setting. "
                "You will create sections of the story for a given range of events in the JSON file. "
                "You will try and keep the content consistent throughout the story by analysis of the previous events. ")
#Files to upload to the author agent
files_list = [os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, CONVERSATIONS_LORE_FILE),
              os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, ENEMY_LORE_FILE), 
              os.path.join(OUTPUT_DIR, CHARACTERS_SUB_DIR, PARTY_LORE_FILE),  
              os.path.join(OUTPUT_DIR, EVENTS_SUB_DIR, ALL_EVENTS_FILE),
              os.path.join(OUTPUT_DIR, REGION_LORE_FILE), 
              os.path.join(OUTPUT_DIR, WORLD_LORE_FILE),           
              ]
#Default values if the agent is not to be regenerated
vector_store_id ="vs_faIZLMDu6hQyWA9LiUHKOlYD"  #
assistant_id = "asst_rLhqNkUB77vU3Pfavd3HeChr"
thread_id= "thread_nvJfWjlC7RFFuUNiUZDTY45G"

gpt_model = "gpt-4o"

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

def generate_areas(global_lore_json, region_lore_json, enemy_lore_json):
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
                description = area_lore_generation.generate_area_thematic_description(global_lore_json, region_lore_json, area["name"], enemy_lore_json, threat_severity)
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
    
def generate_events(region_lore_json, party_json, enemy_json):
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
                previous_events = None
                next_area = None
                if count == 0:
                    previous_events = None
                else:   
                    previous_events = events_json_list_all_areas[count-1]
                if count < len(areas) - 1:
                    next_area = areas[count+1]["name"]
                else:
                    next_area = None
                events_list = event_generation.generate_area_event_sequence(region_lore_json, party_json, enemy_json, count, threat_severity, previous_events, next_area)
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
    print(vector_store_id)


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

    #Generate areas and then modify the region_lore to contain the new descriptions
    region_lore_json = generate_areas(global_lore_json, region_lore_json, enemy_lore_json)
    assert region_lore_json is not None
    #Generate events from region lore
    all_events_json = generate_events(region_lore_json, party_lore_json, enemy_lore_json)
    assert all_events_json is not None

    #Generate conversations
    conversation_json = generate_conversations(region_lore_json, party_lore_json, all_events_json)
    assert conversation_json is not None

    intro_text = generate_introduction(global_lore_json, region_lore_json, party_lore_json, all_events_json)
    assert intro_text is not None

    

