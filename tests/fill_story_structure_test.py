from story_generation import conversation_generation, event_generation, intro_generation
from utils import expected_json_structures, structure_verification, story_structrures, conversation_structures
import os
import pytest
import json

def test_generate_events():
    #Test runs after the world and starting regions are written to file
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    region_lore_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            region_lore_txt += line
    region_lore_json = json.loads(region_lore_txt)

    #Want to include the enemy in all the descriptions as they
    #are the main threat in the region and their presence should grow more overt as the party gets closer to them.

    enemy_file = "{}/../test_data/characters/enemy.txt".format(BASE_DIR)
    enemy_txt = ""
    with open(enemy_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            enemy_txt += line
    enemy_json = json.loads(enemy_txt)
    assert enemy_json is not None

    #And the party
    party_file = "{}/../test_data/characters/party.txt".format(BASE_DIR)
    party_txt = ""
    with open(party_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            party_txt += line
    party_json = json.loads(party_txt)
    assert party_json is not None
    
    structure_verification.verify_lore_structure(enemy_json, expected_json_structures.main_enemy_structure_for_test)
    structure_verification.verify_lore_structure(party_json, expected_json_structures.expected_structure_party_for_test)
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    #We now start using the start region data to create new areas.
    areas = region_lore_json["starting_area"]["notable_locations"]   
    count = 0  
    events_json_list_all_areas=[] 
    all_events = {}    

    #Delete the previous events files

    dir = "{}/../test_data/events".format(BASE_DIR)
    files = os.listdir(dir)
    files = [f for f in files if ".txt" in f and "events" in f]
    for f in files:
        file_path = f"{BASE_DIR}/../test_data/events/{f}"
        os.remove(file_path)

    for area in areas:
        if count < len(areas) - 1:
            threat_severity = "Low"
        else:
            threat_severity = "High"
        print(f"Generating events for area {area["name"]} with threat severity {threat_severity}")
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
        events_list = event_generation.generate_area_event_sequence(region_lore_json,party_json,enemy_json,count,threat_severity, previous_events, next_area)
        events_json = json.loads(events_list)
        structure_verification.verify_lore_structure(events_json, story_structrures.event_list_structure_for_test)
        events_json_list_all_areas.append(events_json)        
        count += 1
        txt_file = f"{BASE_DIR}/../test_data/events/events_{count}.txt"
        with open(txt_file, 'w') as f:
            f.write(events_list)
        all_events[area["name"]] = events_json
    txt_file = f"{BASE_DIR}/../test_data/events/all_events.txt"
    with open(txt_file, 'w') as f:
         f.write(json.dumps(all_events, indent=4))

# Generate the introductory events for the story
def test_generate_starting_events():
    #Test runs after the world and starting regions are written to file
    #Load the world lore
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    world_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
    world_lore_txt = ""
    with open(world_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            world_lore_txt += line
    lore_json = json.loads(world_lore_txt)
    structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)

    #Load the region lore
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    region_lore_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            region_lore_txt += line
    region_lore_json = json.loads(region_lore_txt)


    enemy_file = "{}/../test_data/characters/enemy.txt".format(BASE_DIR)
    enemy_txt = ""
    with open(enemy_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            enemy_txt += line
    enemy_json = json.loads(enemy_txt)
    assert enemy_json is not None

    #And the party
    party_file = "{}/../test_data/characters/party.txt".format(BASE_DIR)
    party_txt = ""
    with open(party_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            party_txt += line
    party_json = json.loads(party_txt)
    assert party_json is not None
    
    structure_verification.verify_lore_structure(enemy_json, expected_json_structures.main_enemy_structure_for_test)
    structure_verification.verify_lore_structure(party_json, expected_json_structures.expected_structure_party_for_test)
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    print(f"Generating starting events for the story")
    upcoming_events = None
    next_area = None

    #Load the previous events
    events_file = "{}/../test_data/events/events_1.txt".format(BASE_DIR)
    events_txt = ""
    with open(events_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            events_txt += line

    upcoming_events = json.loads(events_txt)
    #validate the structure of the events
    structure_verification.verify_lore_structure(upcoming_events, story_structrures.event_list_structure_for_test)

    intro_text = intro_generation.generate_start_scene_text(lore_json, region_lore_json, party_json, upcoming_events)
    
 
    txt_file = f"{BASE_DIR}/../test_data/events/intro.txt"
    with open(txt_file, 'w') as f:
         f.write(intro_text)

def test_generate_conversations():
    #Test runs after the world and starting regions are written to file
    #Load the world lore
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    world_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
    world_lore_txt = ""
    with open(world_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            world_lore_txt += line
    lore_json = json.loads(world_lore_txt)
    structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)

    #Load the region lore
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    region_lore_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            region_lore_txt += line
    region_lore_json = json.loads(region_lore_txt)


    #And the party
    party_file = "{}/../test_data/characters/party.txt".format(BASE_DIR)
    party_txt = ""
    with open(party_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            party_txt += line
    party_json = json.loads(party_txt)
    assert party_json is not None
    
    
    structure_verification.verify_lore_structure(party_json, expected_json_structures.expected_structure_party_for_test)
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    print(f"Generating general conversations for the story")
    upcoming_events = None
    next_area = None

    #Load all the events from the directory
    dir = "{}/../test_data/events".format(BASE_DIR)
    files = os.listdir(dir)
    files = [f for f in files if ".txt" in f and "events" in f and "all" not in f]
    all_events = {}
    count = 0
    for f in files:      
        area_name= region_lore_json["starting_area"]["notable_locations"][count]["name"]
        events_txt = ""
        with open(f"{dir}/{f}", 'r') as f:
            lines = f.readlines()
            for line in lines:
                events_txt += line
        events_json = json.loads(events_txt)
        all_events[area_name] = events_json
        count += 1
    all_events_json = json.dumps(all_events, indent=4)

    conversations = conversation_generation.generate_conversations(region_lore_json, party_json, all_events_json)
    txt_file = f"{BASE_DIR}/../test_data/characters/conversations.txt"
    with open(txt_file, 'w') as f:
         f.write(conversations)
         
    conversations_json = json.loads(conversations)
    #validate the structure of the events
    structure_verification.verify_lore_structure(conversations_json, conversation_structures.conversation_structure_for_test)

    