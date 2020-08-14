import json

def read_all_covid_data(covid_data_filename):
  """Reads the entire json file into a list. Input:  a json file.  Output: a list of dictionaries."""
  with open('covid_data_filename', 'r') as f:
      covid_data_list = json.load(f)
  return covid_data_list