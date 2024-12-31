
expected_structure_world = {
    "world": {
        "name": "",
        "description": "",
        "creation": {
            "origin_story": "",
            "primary_gods": [
                {
                    "name": "",
                    "domain": "",
                    "symbol": "",
                    "description": ""
                }
            ]
        },
        "geography": {
            "continents": [
                {
                    "name": "",
                    "description": "",
                    "notable_locations": [
                        {
                            "name": "",
                            "description": ""
                        }
                    ]
                }
            ]
        },
        "notable_locations": [
          {
            "name": "",
            "type": "",
            "description": "",
            "points_of_interest": [
              {
                "name": "",
                "type": "",
                "description": "",
                "owner": ""
              }
            ]
          }
        ],
        "races": [
            {
                "name": "",
                "description": "",
                "homeland": ""
            }
        ],
        "magic": {
            "source": "",
            "description": "",
            "schools": [
                {
                    "name": "",
                    "description": ""
                }
            ]
        },
        "history": {
            "eras": [
                {
                    "name": "",
                    "timeline": "",
                    "events": [
                        {
                            "name": "",
                            "description": ""
                        }
                    ]
                }
            ]
        }
    }
}



expected_structure_world_for_test =  {
    "world": {
        "name": str,
        "description": str,
        "creation": {
            "origin_story": str,
            "primary_gods": [
                {
                    "name": str,
                    "domain": str,
                    "symbol": str,
                    "description": str
                }
            ]
        },
        "geography": {
            "continents": [
                {
                    "name": str,
                    "description": str,
                    "notable_locations": [
                        {
                            "name": str,
                            "description": str
                        }
                    ]
                }
            ]
        },
        "notable_locations": [
          {
            "name": str,
            "type": str,
            "description": str,
            "points_of_interest": [
              {
                "name": str,
                "type": str,
                "description": str,
                "owner": str
              }
            ]
          }
        ],
        "races": [
            {
                "name": str,
                "description": str,
                "homeland": str
            }
        ],
        "magic": {
            "source": str,
            "description": str,
            "schools": [
                {
                    "name": str,
                    "description": str
                }
            ]
        },
        "history": {
            "eras": [
                {
                    "name": str,
                    "timeline": str,
                    "events": [
                        {
                            "name": str,
                            "description": str
                        }
                    ]
                }
            ]
        }
    }
}

expected_structure_region = {
  "starting_area": {
    "name": "",
    "description": "",
    "environment": {
      "terrain": "",
      "climate": "",
      "flora": [
        {
          "name": "",
          "description": "",
          "rarity": ""
        },
        {
          "name": "",
          "description": "",
          "rarity": ""
        }
      ],
      "fauna": [
        {
          "name": "",
          "description": "",
          "behavior": "",
          "danger_level": ""
        },
        {
          "name": "",
          "description": "",
          "behavior": "",
          "danger_level": ""
        }
      ]
    },
    "notable_locations": [
      {
        "name": "",
        "type": "",
        "description": "",
        "points_of_interest": [
          {
            "name": "",
            "type": "",
            "description": "",
            "owner": ""
          }
        ],
        "threats": [
          {
            "name": "",
            "description": "",
            "danger_level": "",
            "behavior": ""
          }
        ]
      }
    ],
    "factions": [
      {
        "name": "",
        "type": "",
        "description": "",
        "alignment": "",
        "leader": ""
      }
    ],
    "notable_npcs": [
      {
        "name": "",
        "role": "",
        "description": "",
        "alignment": "",
        "backstory": "",
        "secrets": ""
      }
    ],
    "quests": [
      {
        "name": "",
        "type": "",
        "description": "",
        "objectives": [
          {
            "description": "",
            "status": ""
          },
          {
            "description": "",
            "status": ""
          }
        ],
        "rewards": [
          {
            "name": "",
            "type": "",
            "description": ""
          },
          {
            "name": "",
            "type": "",
            "description": ""
          }
        ]
      }
    ],
    "threats": [
      {
        "name": "",
        "description": "",
        "danger_level": "",
        "behavior": ""
      }
    ]
  }
}

expected_structure_region_for_test = {
  "starting_area": {
    "name": str,
    "description": str,
    "environment": {
      "terrain": str,
      "climate": str,
      "flora": [
        {
          "name": str,
          "description": str,
          "rarity": str
        },
        {
          "name": str,
          "description": str,
          "rarity": str
        }
      ],
      "fauna": [
        {
          "name": str,
          "description": str,
          "behavior": str,
          "danger_level": str
        },
        {
          "name": str,
          "description": str,
          "behavior": str,
          "danger_level": str
        }
      ]
    },
    "notable_locations": [
      {
        "name": str,
        "type": str,
        "description": str,
        "points_of_interest": [
          {
            "name": str,
            "type": str,
            "description": str,
            "owner": str
          }
        ],
        "threats": [
          {
            "name": str,
            "description": str,
            "danger_level": str,
            "behavior": str
          }
        ]
      }
    ],
    "factions": [
      {
        "name": str,
        "type": str,
        "description": str,
        "alignment": str,
        "leader": str
      }
    ],
    "notable_npcs": [
      {
        "name": str,
        "role": str,
        "description": str,
        "alignment": str,
        "backstory": str,
        "secrets": str
      }
    ],
    "quests": [
      {
        "name": str,
        "type": str,
        "description": str,
        "objectives": [
          {
            "description": str,
            "status": str
          },
          {
            "description": str,
            "status": str
          }
        ],
        "rewards": [
          {
            "name": str,
            "type": str,
            "description": str
          },
          {
            "name": str,
            "type": str,
            "description": str
          }
        ]
      }
    ],
    "threats": [
      {
        "name": str,
        "description": str,
        "danger_level": str,
        "behavior": str
      }
    ]
  }
}


expected_structure_party ={
    "party": {
        "name": "",
        "description": "",
        "members": [
            {
                "name": "",
                "race": "",
                "class": "",
                "role": "",
                "alignment": "",
                "backstory": "",
                "abilities": {
                    "strengths": ["", ""],
                    "weaknesses": ["", ""]
                },
                "equipment": [
                    {
                        "name": "",
                        "type": "",
                        "description": "",
                        "magical_properties": [""]
                    }
                ],
                "goals": "",
                "secrets": "",
                "relationships": {
                    "allies": ["", ""],
                    "rivals": ["", ""],
                    "other_party_connections": ["", ""]
                }
            }
        ],
        "shared_goals": "",
        "shared_backstory": "",
        "base_of_operations": {
            "name": "",
            "location": "",
            "description": ""
        },
        "notable_achievements": [
            {
                "name": "",
                "description": "",
                "impact": ""
            }
        ],
        "current_quest": {
            "name": "",
            "description": "",
            "objectives": ["", ""]
        }
    }
}

expected_structure_party_for_test ={
    "party": {
        "name": str,
        "description": str,
        "members": [
            {
                "name": str,
                "race": str,
                "class": str,
                "role": str,
                "alignment": str,
                "backstory": str,
                "abilities": {
                    "strengths": [str, str],
                    "weaknesses": [str, str]
                },
                "equipment": [
                    {
                        "name": str,
                        "type": str,
                        "description": str,
                        "magical_properties": [str]
                    }
                ],
                "goals": str,
                "secrets": str,
                "relationships": {
                    "allies": [str, str],
                    "rivals": [str, str],
                    "other_party_connections": [str, str]
                }
            }
        ],
        "shared_goals": str,
        "shared_backstory": str,
        "base_of_operations": {
            "name": str,
            "location": str,
            "description": str
        },
        "notable_achievements": [
            {
                "name": str,
                "description": str,
                "impact": str
            }
        ],
        "current_quest": {
            "name": str,
            "description": str,
            "objectives": [str, str]
        }
    }
}

main_enemy_structure = {
    "main_enemy": {
        "name": "",
        "title": "",
        "description": "",
        "race": "",
        "role": "",
        "alignment": "",
        "backstory": "",
        "motives": "",
        "goals": "",
        "appearance": {
            "physical_traits": "",
            "notable_features": ""
        },
        "abilities": {
            "strengths": ["", ""],
            "weaknesses": ["", ""]
        },
        "equipment": [
            {
                "name": "",
                "type": "",
                "description": "",
                "magical_properties": [""]
            }
        ],
        "lair": {
            "name": "",
            "location": "",
            "description": "",
            "defenses": ["", ""],
            "traps": ["", ""]
        },
        "minions": [
            {
                "name": "",
                "type": "",
                "role": "",
                "description": ""
            }
        ],
        "secrets": "",
        "threat_level": "",
        "notable_acts": [
            {
                "name": "",
                "description": "",
                "impact": ""
            }
        ],
    }
}

main_enemy_structure_for_test = {
    "main_enemy": {
        "name": str,
        "title": str,
        "description": str,
        "race": str,
        "role": str,
        "alignment": str,
        "backstory": str,
        "motives": str,
        "goals": str,
        "appearance": {
            "physical_traits": str,
            "notable_features": str
        },
        "abilities": {
            "strengths": [str, str],
            "weaknesses": [str, str]
        },
        "equipment": [
            {
                "name": str,
                "type": str,
                "description": str,
                "magical_properties": [str]
            }
        ],
        "lair": {
            "name": str,
            "location": str,
            "description": str,
            "defenses": [str, str],
            "traps": [str, str]
        },
        "minions": [
            {
                "name": str,
                "type": str,
                "role": str,
                "description": str
            }
        ],
        "secrets": str,
        "threat_level": str,
        "notable_acts": [
            {
                "name": str,
                "description": str,
                "impact": str
            }
        ]
    }
}

