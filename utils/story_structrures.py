plot_structure = {
        "areas" : [{
                "name": "",
                "plot_actions_in_area": ["",""],
                "minor_events_in_area":["", ""],
                "reason_to_move_on": "",
                "route_to_next_area": "",
                "threat_severity": "",
                "important_items_in_area": ["",""],
                "important_people_in_area":["",""],
                "areas_visited" :["",""],
                "enemies_in_area":["",""]
        }   
        ]
}

plot_structure_for_test = {
        "areas" : [{
                "name": str,
                "plot_actions_in_area": [str,str],
                "minor_events_in_area":[str, str],
                "reason_to_move_on": str,
                "route_to_next_area": str,
                "threat_severity": str,
                "important_items_in_area": [str,str],
                "important_people_in_area":[str,str],
                "areas_visited" :[str,str],
                "enemies_in_area":[str,str]
        }   
        ]
}

event_list_structure = {
    "events":[ 
            {
                "id": "",
                "type": "",
                "description": "",
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