from lore_generation import area_lore_generation, global_lore_generation, region_lore_generation
from utils import expected_json_structures, structure_verification
import os
import json

OUTPUT_DIR = "output_data"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
WORLD_LORE_FILE = "world_lore.txt"
REGION_LORE_FILE = "starting_region_lore.txt"

region_flavour_prompt = "A dark dungeon inspired by the Fighting fantasy books."
world_flavour_prompt = "The Fighting Fantasy books by Steven Jackson"

refresh_global_lore = False
refresh_region_lore = False

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
            print(lore_txt)
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
        print(lore_json)
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
            print(lore_txt)
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
        print(lore_json)
        # Ensure the lore JSON is not None
        assert lore_json is not None
        # Verify the structure of the lore JSON
        structure_verification.verify_lore_structure(lore_json, expected_json_structures.expected_structure_region_for_test)
        print("Region lore passed verification.")
        return lore_json
    except Exception as e:
        print(f"Error in generate_region_lore: {e}")
        return None
    
if __name__ == "__main__":
    global_lore_json = generate_global_lore()
    region_lore_json = generate_region_lore(global_lore_json)
    