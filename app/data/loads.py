"""
Sample loads data for the carrier campaign technical challenge. 
"""

LOADS = [
  {
    "load_id": "LD-20250604-ATL-LAX",
    "origin": "Atlanta, GA",
    "destination": "Los Angeles, CA",
    "pickup_datetime": "2025-06-04T12:00:00Z",
    "delivery_datetime": "2025-06-08T01:00:00Z",
    "equipment_type": "reefer",
    "loadboard_rate": 4200,
    "notes": "Frozen poultry, requires –10 °F setpoint",
    "weight": 38500,
    "commodity_type": "food",
    "num_of_pieces": 24,
    "miles": 2181,
    "dimensions": "53' trailer"
  },
  {
    "load_id": "LD-20250605-DAL-CHI",
    "origin": "Dallas, TX",
    "destination": "Chicago, IL",
    "pickup_datetime": "2025-06-05T14:00:00Z",
    "delivery_datetime": "2025-06-07T20:00:00Z",
    "equipment_type": "dry van",
    "loadboard_rate": 1900,
    "notes": "Consumer electronics, no team required",
    "weight": 26400,
    "commodity_type": "electronics",
    "num_of_pieces": 720,
    "miles": 967,
    "dimensions": "53' trailer"
  },
  {
    "load_id": "LD-20250606-MIA-SAV",
    "origin": "Miami, FL",
    "destination": "Savannah, GA",
    "pickup_datetime": "2025-06-06T13:00:00Z",
    "delivery_datetime": "2025-06-07T10:00:00Z",
    "equipment_type": "flatbed",
    "loadboard_rate": 1400,
    "notes": "Steel rebar, tarps required",
    "weight": 45500,
    "commodity_type": "building_materials",
    "num_of_pieces": 10,
    "miles": 484,
    "dimensions": "48' flatbed"
  },
  {
    "load_id": "LD-20250607-SEA-DEN",
    "origin": "Seattle, WA",
    "destination": "Denver, CO",
    "pickup_datetime": "2025-06-07T09:00:00Z",
    "delivery_datetime": "2025-06-09T23:00:00Z",
    "equipment_type": "stepdeck",
    "loadboard_rate": 3400,
    "notes": "Compact excavator, ramps onsite",
    "weight": 31200,
    "commodity_type": "machinery",
    "num_of_pieces": 1,
    "miles": 1327,
    "dimensions": "10' L × 5' W × 8' H"
  },
  {
    "load_id": "LD-20250604-EWR-BOS",
    "origin": "Newark, NJ",
    "destination": "Boston, MA",
    "pickup_datetime": "2025-06-04T11:00:00Z",
    "delivery_datetime": "2025-06-04T23:00:00Z",
    "equipment_type": "box truck",
    "loadboard_rate": 750,
    "notes": "LTL furniture—driver assist at destination",
    "weight": 8900,
    "commodity_type": "furniture",
    "num_of_pieces": 18,
    "miles": 233,
    "dimensions": "26' box"
  }
]
 