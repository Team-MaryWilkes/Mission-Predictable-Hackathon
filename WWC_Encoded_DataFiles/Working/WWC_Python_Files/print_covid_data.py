import json

def print_covid_data(data_list, data_filename):
  """Input:  A list of dictionaries.  Output:  A csv file with the list of dictionaries."""
  with open(data_filename, 'w') as f:
    json.dump(data_list, f, indent=4)
 