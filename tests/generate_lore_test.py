from lore_generation import global_lore_generation
from lore_generation import region_lore_generation
from utils import expected_json_structures
import os
import pytest
import json

refresh_global_lore = False
refresh_region_lore = True

def test_generate_lore():
    lore_json = None
    lore = ""
    if refresh_global_lore:
        lore = global_lore_generation.generate_global_lore()
        print(lore)
        lore_json = json.loads(lore)
    else:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        lore_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
        lore_txt = ""
        with open(lore_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                lore_txt += line
        lore_json = json.loads(lore_txt)

    assert lore_json is not None
    verify_lore_structure(lore_json, expected_json_structures.expected_structure_world_for_test)
    
    #Generate the starting region
    region_lore_json = None
    region_lore_txt = ""
    if refresh_region_lore:
        region_lore_txt = region_lore_generation.generate_starting_region_lore(lore)
        region_lore_json = json.loads(region_lore_txt)
    else:
        start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
        start_region_txt = ""
        with open(start_region_file, 'r') as f:
            lore_lines = f.readlines()
            for line in lore_lines:
                start_region_txt += line
        region_lore_json = json.loads(start_region_txt)
    assert region_lore_json is not None
    verify_lore_structure(region_lore_json, expected_json_structures.expected_structure_region_for_test)
      
def verify_lore_structure(lore_json, expected_structure):
    """
    Validates that the JSON structure is properly filled.

    :param lore_json: The JSON object to validate
    :param expected_structure: the structure to validate against
    :return: None. Raises an assertion error if validation fails.
    """
    
    # Helper function to recursively validate the structure
    def validate_recursive(expected, actual, path=""):
        if isinstance(expected, dict):
            # Ensure all keys are present in the actual data
            assert isinstance(actual, dict), f"Expected dict at {path}, got {type(actual).__name__}"
            for key, value in expected.items():
                assert key in actual, f"Missing key '{key}' at {path}"
                validate_recursive(value, actual[key], f"{path}.{key}" if path else key)
        elif isinstance(expected, list) and expected:
            # Ensure actual is a list and validate each item against the list's structure
            assert isinstance(actual, list), f"Expected list at {path}, got {type(actual).__name__}"
            for item in actual:
                validate_recursive(expected[0], item, f"{path}[]")
        else:
            # Ensure the type matches and is properly filled
            assert isinstance(actual, expected), f"Expected {expected.__name__} at {path}, got {type(actual).__name__}"
            if isinstance(actual, str):
                assert actual.strip(), f"Empty string at {path}"
            elif isinstance(actual, list):
                assert actual, f"Empty list at {path}"
            elif actual is None:
                raise AssertionError(f"None value at {path}")

    # Start validation
    validate_recursive(expected_structure, lore_json)






