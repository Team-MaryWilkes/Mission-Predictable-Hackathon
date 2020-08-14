def encode_weekday():
  """Input: None Output:  Dictionary of one hot encoding vector for each weekday.  For example:  Monday : [1,0,0,0,0,0,0], Sunday: [0,0,0,0,0,0,1]."""
  weekday_dict = {
    "Monday": [1,0,0,0,0,0,0],
    "Tuesday":[0,1,0,0,0,0,0],
    "Wednesday":[0,0,1,0,0,0,0],
    "Thursday":[0,0,0,1,0,0,0],
    "Friday":[0,0,0,0,1,0,0],
    "Saturday":[0,0,0,0,0,1,0],
    "Sunday":[0,0,0,0,0,0,1],
  }

  return weekday_dict

def weekday_encoding_lookup(weekday, weekday_encoded_dict):
  """Input:  String Weekday, weekday_encoded_dict. Output: Vector encoding for that weekday."""
  return weekday_encoded_dict[weekday]  