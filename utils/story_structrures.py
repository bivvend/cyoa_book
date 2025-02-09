item_structure = {
    "items":[{
        "name": "",
        "area_found": "",
        "properties": "",
        "description": ""
    }
    ]
}

item_structure_for_test = {
    "items":[{
        "name": str,
        "area_found": str,
        "properties": str,
        "description": str
    }
    ]
}

character_structure = {
    "characters":[{
        "name": "",
        "area_found": "",
        "skills_and_abilities": ["",""],
        "description": "",
        "appearance": "",
    }
    ]
}

character_structure_for_test = {
    "characters":[{
        "name": str,
        "area_found": str,
        "skills_and_abilities": [str, str],
        "description": str,
        "appearance": str,
    }
    ]
}

map_structure = {
        "name": "",
        "locations":[{"name": "", "sub_locations":["",""]}, {"name": "", "sub_locations":["",""]},],
        "paths":[
            {
                "from":"",
                "to": "",
                "description":"",
                "threat_level":"",
                "dangers":["",""]            
            }
        ],
        
}

map_structure_for_test = {
        "name":str,
        "locations":[{"name": str, "sub_locations":[str,str]}, {"name": str, "sub_locations":[str,str]},],
        "paths":[
            {
                "from":str,
                "to": str,
                "description":str,
                "threat_level":str,
                "dangers":[str,str]            
            }
        ],
}

plot_structure = {
        "areas" : [{
                "name": "",
                "plot_events": [
                    {
                        "event_id": "",
                        "location_within_area": "",
                        "party_members_involved": ["",""],
                        "other_characters_involved": ["",""],
                        "threats": ["",""],
                        "decription_of_event":"",
                        "event_type":"",
                        "party_status_changes":[
                            {"name": "",
                             "status_change": ""
                            },  
                            {"name": "",
                             "status_change": ""
                            },
                        ],
                        "outcome":"",
                        "next_action":"",
                        "reason_for_next_action":"",
                        "items_found":["",""],
                        "items_lost":["",""],
                        "updated_party_inventory":["","","",""]
                    },
                ],
                "reason_to_move_to_next_area": "",
                "route_to_next_area": "",
        }   
        ]
}

plot_structure_for_test = {
    "areas": [{
        "name": str,
        "plot_events": [
            {
                "event_id": str,
                "location_within_area": str,
                "party_members_involved": [str, str],
                "other_characters_involved": [str, str],
                "threats": [str, str],
                "decription_of_event": str,
                "event_type": str,
                "party_status_changes": [
                    {
                        "name": str,
                        "status_change": str
                    },
                    {
                        "name": str,
                        "status_change": str
                    },
                ],
                "outcome": str,
                "next_action": str,
                "reason_for_next_action": str,
                "items_found":[str,str],
                "items_lost":[str,str],
                "updated_party_inventory":[str,str,str,str]
            },
        ],
        "reason_to_move_to_next_area": str,
        "route_to_next_area": str,
    }]
}

event_list_structure = {
    "events":[ 
            {
                "id": "",
                "type": "",
                "description": "",
                "location_within_area": "",
                "is_main_plot_event": "",
                "is_minor_event": "",
                "npcs_involved": [
                    "",""
                ],
                "party_members_involved": [
                    "",""
                ],
                "threats_involved": [
                    "",""
                ],
                "items_involved": [
                    "",""
                ],
                "inventory_of_story_items": [
                    "",""
                ],
                "outcome": "",
                "status_changes": [
                {
                    "description": "",
                    "consequence": "",
                }
                ]
            } 
    ]    
}

event_list_structure_for_test = {
    "events":[ 
            {
                "id": str,
                "type": str,
                "description": str,
                "location_within_area": str,
                "is_main_plot_event": str,
                "is_minor_event": str,
                "npcs_involved": [
                    str,str
                ],
                "party_members_involved": [
                    str,str
                ],
                "threats_involved": [
                    str,str
                ],
                "items_involved": [
                    str,str
                ],
                "inventory_of_story_items": [
                    str,str
                ],
                "outcome": str,
                "status_changes": [
                {
                    "description": str,
                    "consequence": str,
                }
                ]
            } 
    ]    
}