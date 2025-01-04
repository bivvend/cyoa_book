from lore_generation import global_lore_generation, region_lore_generation, area_lore_generation, party_generation, main_enemy_generation
from utils import expected_json_structures, structure_verification
import os
import pytest
import json

refresh_global_lore = True  #Generate new global lore
refresh_region_lore = True #Generate new region lore
refresh_area_lore = True #Generate new area lore
refresh_party_lore = True #Generate new party lore
refresh_enemy_lore = True #Generate

def test_generate_lore():
    lore_json = None
    lore_txt = ""
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    if refresh_global_lore:
        lore_txt = global_lore_generation.generate_global_lore()
        print(lore_txt)
        lore_json = json.loads(lore_txt)
        #Save the lore to file
        txt_file = f"{BASE_DIR}/../test_data/world_lore.txt"
        with open(txt_file, 'w') as f:
            f.write(lore_txt)

    else:
        lore_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
        with open(lore_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                lore_txt += line
        lore_json = json.loads(lore_txt)

    assert lore_json is not None
    structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)
    
    #Generate the starting region
    region_lore_json = None
    region_lore_txt = ""
    if refresh_region_lore:
        region_lore_txt = region_lore_generation.generate_starting_region_lore(lore_json)
        region_lore_json = json.loads(region_lore_txt)
    else:
        start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
        with open(start_region_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                region_lore_txt += line
        region_lore_json = json.loads(region_lore_txt)
    assert region_lore_json is not None
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)
      
    #Generate the areas in the starting region
def test_generate_areas():
    #Test runs after the world and starting regions are written to file
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    lore_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
    lore_txt = ""
    with open(lore_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            lore_txt += line
    lore_json = json.loads(lore_txt)

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
    
    structure_verification.verify_lore_structure(enemy_json, expected_json_structures.main_enemy_structure_for_test)
    structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    #We now start using the start region data to create new areas.
    areas = region_lore_json["starting_area"]["notable_locations"]
    print(areas)
    
    area_description_list = []
    if refresh_area_lore:
        #Delete all the previous areas
        dir = "{}/../test_data/areas".format(BASE_DIR)
        files = os.listdir(dir)
        files = [f for f in files if ".txt" in f]
        for f in files:
            file_path = f"{BASE_DIR}/../test_data/areas/{f}"
            os.remove(file_path)
        count =0
        
        for area in areas:
            count += 1
            #Must pass the text versions!
            if count < len(areas):
                threat_severity = "Low"
            else:
                threat_severity = "High"
            print(f"Generating fuller description of area {area["name"]} with threat severity {threat_severity}")
            description = area_lore_generation.generate_area_thematic_description(lore_json, region_lore_json, area["name"], enemy_json, threat_severity)
            area_description_list.append(description)
            BASE_DIR = os.path.dirname(os.path.realpath(__file__))
            txt_file = f"{BASE_DIR}/../test_data/areas/area_{count}.txt"
            with open(txt_file, 'w') as f:
                f.write(description)
    else:
        #Load all the descriptions from file
        dir = "{}/../test_data/areas".format(BASE_DIR)
        files = os.listdir(dir)
        files = [f for f in files if ".txt" in f and "area" in f]
        for f in files:
            file_path = f"{BASE_DIR}/../test_data/areas/{f}"
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
    #Check structure still holds
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    #Write back the updated region lore
    with open(start_region_file, 'w') as f:
        f.write(json.dumps(region_lore_json, indent=4)) 


def test_generate_party():
    lore_json = None
    lore_txt = ""
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    if refresh_global_lore:
        lore_txt = global_lore_generation.generate_global_lore()
        print(lore_txt)
        lore_json = json.loads(lore_txt)
    else:

        lore_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
        with open(lore_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                lore_txt += line
        lore_json = json.loads(lore_txt)
    assert lore_json is not None

    if refresh_party_lore:
        party_lore = party_generation.generate_party(lore_json)
        print(party_lore)
        party_json = json.loads(party_lore)
        assert party_json is not None

        structure_verification.verify_lore_structure(party_json, expected_json_structures.expected_structure_party_for_test)
        txt_file = f"{BASE_DIR}/../test_data/characters/party.txt"
        with open(txt_file, 'w') as f:
            f.write(party_lore)
    else:
        party_file = "{}/../test_data/characters/party.txt".format(BASE_DIR)
        party_txt = ""
        with open(party_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                party_txt += line
        party_json = json.loads(party_txt)
        assert party_json is not None
        structure_verification.verify_lore_structure(party_json, expected_json_structures.expected_structure_party_for_test)

def test_generate_enemy():
    #Open the region lore
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    start_region_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            start_region_txt += line
    region_lore_json = json.loads(start_region_txt)
    structure_verification.verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)

    #Generate the enemy
    if refresh_enemy_lore:
        enemy_lore = main_enemy_generation.generate_main_enemy(region_lore_json)
        print(enemy_lore)
        enemy_json = json.loads(enemy_lore)
        assert enemy_json is not None

        structure_verification.verify_lore_structure(enemy_json, expected_json_structures.main_enemy_structure_for_test)
        txt_file = f"{BASE_DIR}/../test_data/characters/enemy.txt"
        with open(txt_file, 'w') as f:
            f.write(enemy_lore)
    else:
        enemy_file = "{}/../test_data/characters/enemy.txt".format(BASE_DIR)
        enemy_txt = ""
        with open(enemy_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                enemy_txt += line
        enemy_json = json.loads(enemy_txt)
        assert enemy_json is not None
        structure_verification.verify_lore_structure(enemy_json, expected_json_structures.main_enemy_structure_for_test)