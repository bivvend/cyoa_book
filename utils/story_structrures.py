map_structure = {
        "name": "",
        "locations":["", ""],
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
        "locations":[str, str],
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
                "plot_actions_in_area": ["",""],
                "minor_events_in_area":["", ""],
                "reason_to_move_to_next_area": "",
                "route_to_next_area": "",
                "threat_severity": "",
                "important_items_in_area": ["",""],
                "important_people_in_area":["",""],
                "main_plot_items_status_tracking":[
                    {
                        "name": "",
                        "status":"",
                        "found_yet": ""    
                    },
                ],
                "party_member_status_tracking":[
                    {
                        "name": "",
                        "status_changes":["",""],  
                    },
                ],
                "areas_to_visit" :["",""],
                "enemies_in_area":["",""],
                "party_status_changes" : ["",""]
        }   
        ]
}

plot_structure_for_test = {
        "areas" : [{
                "name": str,
                "plot_actions_in_area": [str,str],
                "minor_events_in_area":[str, str],
                "reason_to_move_to_next_area": str,
                "route_to_next_area": str,
                "threat_severity": str,
                "important_items_in_area": [str,str],
                "important_people_in_area":[str,str],
                "main_plot_items_status_tracking":[
                    {
                        "name": str,
                        "status":str,
                        "found_yet": str    
                    },
                ],
                "party_member_status_tracking":[
                    {
                        "name": str,
                        "status_changes":[str,str],  
                    },
                ],
                "areas_to_visit" :[str,str],
                "enemies_in_area":[str,str],
                "party_status_changes" : [str,str]
        }   
        ]
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