story_progression_structure = {
    "story": {
        "title": "",
        "description": "",
        "current_area": "",
        "notable_areas": [
            {
                "id": "",
                "name": "",
                "description": "",
                "related_area": "",
                "location": "",
                "events": [
                    {
                        "id": "",
                        "type": "",
                        "description": "",
                        "characters_involved": [
                            ""
                        ],
                        "trigger": "",
                        "outcome": {
                            "success": "",
                            "failure": ""
                        },
                        "choices": [
                            {
                                "description": "",
                                "consequence": "",
                                "next_event_id": ""
                            }
                        ]
                    }
                ],
                "area_state": {
                    "status": "",
                    "changes": [
                        {
                            "description": "",
                            "trigger": ""
                        }
                    ]
                },
                "notable_features": [
                    {
                        "name": "",
                        "type": "",
                        "description": "",
                        "related_event": ""
                    }
                ],
                "factions_present": [
                    {
                        "faction_id": "",
                        "status": ""
                    }
                ]
            }
        ],
        "progression": {
            "visited_areas": [""],
            "current_area": "",
        }
    }
}

story_progression_structure_for_test = {
    "story": {
        "title": str,
        "description": str,
        "current_area": str,
        "notable_areas": [
            {
                "id": str,
                "name": str,
                "description": str,
                "related_area": str,
                "location": str,
                "events": [
                    {
                        "id": str,
                        "type": str,
                        "description": str,
                        "characters_involved": [
                            str,str
                        ],
                        "trigger": str,
                        "outcome": {
                            "success": str,
                            "failure": str
                        },
                        "choices": [
                            {
                                "description": str,
                                "consequence": str,
                                "next_event_id": str
                            }
                        ]
                    }
                ],
                "area_state": {
                    "status": str,
                    "changes": [
                        {
                            "description": str,
                            "trigger": str
                        }
                    ]
                },
                "notable_features": [
                    {
                        "name": str,
                        "type": str,
                        "description": str,
                        "related_event": str
                    }
                ],
                "factions_present": [
                    {
                        "faction_id": str,
                        "status": str
                    }
                ]
            }
        ],
        "progression": {
            "visited_areas": [str, str],
            "current_area": str,
        }
    }
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