from story_generation import event_generation
from utils import expected_json_structures, structure_verification, story_structrures
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
    events_list_all_areas=[]     
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
            previous_events = events_list_all_areas[count-1]
        if count < len(areas) - 1:
            next_area = areas[count+1]["name"]
        else:
            next_area = None
        events_list = event_generation.generate_initial_event_sequence(region_lore_json,party_txt,enemy_txt,count,threat_severity, previous_events, next_area)
        events_list_all_areas.append(events_list)
        count += 1
        txt_file = f"{BASE_DIR}/../test_data/events/events_{count}.txt"
        with open(txt_file, 'w') as f:
            f.write(events_list)