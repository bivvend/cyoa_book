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