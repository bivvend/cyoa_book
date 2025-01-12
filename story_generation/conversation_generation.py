import json
from utils import generate_text, conversation_structures

def generate_conversations(region_json, party_json, all_events_json):
    """
    Generates templates for conversations in the story.
    """
    try:
        # Convert JSON to string
        party_json_txt = json.dumps(party_json, indent=4)
        region_json_txt = json.dumps(region_json, indent=4)
        all_events_txt = json.dumps(all_events_json, indent=4)

        writing_guidelines_1 = (   
            "Write descriptions for conversation topics that could happen between the party members in a fantasy story. "
            "Not the full conversation, but just the topic of the conversation. "
            "Each conversation topic should only be a few sentences long. "
            "The conversations should be set in the starting region of the story but could be about any topic relevant to the background of the party members. "
            "The region JSON below should be used to provide context for the conversations. \n"
            f"{region_json_txt}\n" 
        )       
        writing_guidelines_2 = (
            "The conversation should involve at least 2 party members and should reveal information about the world, or the party members "
        )

        writing_guidelines_3 = (
            "The party members are defined in the party JSON below. \n "
            f"{party_json_txt}\n"
        )

        writing_guidelines_4 = (
            "The conversations can be about the party's past, their motivations, or their relationships with each other. " 
        )

        writing_guidelines_5 = (
            "The conversations can also be about the events that have happened in the story. "
            "The events JSON below should be used to determine what the party has experienced so far. \n"
            f"{all_events_txt}\n"
        )

        structuring_prompt = (
            f"The response MUST be in json format so that it can be read by a python program. "
            f"Please fill the structure below with the generated data. You can and should add elements. "
            f"There should be around 25 conversations in the list. \n"
            f"Do not use the ```json style flag in your response, I want to load it directly with json.loads\n"
            "All the values in the JSON should be strings enclosed with \"\". \n"
            f"{conversation_structures.conversation_structure}\n"
        )
        
        prompt = (
            f"{writing_guidelines_1}\n"
            f"{writing_guidelines_2}\n"
            f"{writing_guidelines_3}\n"
            f"{writing_guidelines_4}\n"
            f"{writing_guidelines_5}\n"
            f"{structuring_prompt}\n"
        )

        return generate_text.generate_text(prompt, max_tokens=10000)
    except Exception as e:
        print(f"Error in generate_conversations: {e}")
        return None
