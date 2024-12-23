
expected_structure_world = {
  "region": {
    "name": "",
    "description": "",
    "environment": {
      "terrain": "",
      "climate": "",
      "flora": [],
      "fauna": []
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
        "objectives": [],
        "rewards": []
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


