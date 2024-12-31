from utils import generate_text, expected_json_structures

global_writing_guidelines_1 = (
    "It should focus on key elements that immerse the reader and provide a rich foundation for the adventure. "
    "This includes the party's composition, their backgrounds, motivations, and potential conflicts."
)
global_writing_guidelines_2 = "The description should be around 500 words long."

def generate_party_description(global_lore_json, region_lore_json, party_name):
    """
    Generates lore for a specific party in the game.
    """
    writing_guidelines_1 = (
        f"Write a detailed description for the party called {party_name} of a fantasy story. "
        "You can use the Starting region JSON below to get an idea of the setting."
    )
    writing_guidelines_2 = (
        "Use the global lore and the starting region lore defined in the two JSON structures below. "
        "Don't drift from these, but expand on the details. The starting region lore is more important than the global."
    )
    
    prompt = (
        f"{global_lore_json}\n\n"
        f"{writing_guidelines_1}\n"
        f"{global_writing_guidelines_1}\n"
        f"{global_writing_guidelines_2}\n"
        f"{writing_guidelines_2}\n\n"
        f"Global lore:\n{global_lore_json}\n"
        f"Starting region lore:\n{region_lore_json}"
    )
    return generate_text.generate_text(prompt)
