json_format = {
  "type": "object",
  "properties": {
    "cost_matrix_data": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "0": {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "required": ["data"]
    },
    "task_data": {
      "type": "object",
      "properties": {
        "task_locations": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "demand": {
          "type": "array",
          "items": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          }
        },
        "task_time_windows": {
          "type": "array",
          "items": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          }
        },
        "service_times": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        }
      },
      "required": ["task_locations", "demand", "task_time_windows", "service_times"]
    },
    "fleet_data": {
      "type": "object",
      "properties": {
        "vehicle_locations": {
          "type": "array",
          "items": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          }
        },
        "capacities": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "vehicle_time_windows": {
          "type": "array",
          "items": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          }
        }
      },
      "required": ["vehicle_locations", "capacities", "vehicle_time_windows"]
    },
    "solver_config": {
      "type": "object",
      "properties": {
        "time_limit": {
          "type": "integer"
        }
      },
      "required": ["time_limit"]
    }
  },
  "required": ["cost_matrix_data", "task_data", "fleet_data", "solver_config"]
}