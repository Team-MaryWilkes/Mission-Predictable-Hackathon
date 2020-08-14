import encode_county as ec
import encode_weekday as ew
import encode_gender as eg
import json



def read_file(input_filename):
  """Reads List of Dictionaries from inputfilename into memory. Input:  TXT file with List of Dicts. Output:  List of Dicts."""
  with open(input_filename) as f:
    fd = json.load(f)
  return fd



def encode_data(encode_covid_data):
  """Encodes the data in the dictionary. Input:  List of dicts which have string representations for County, Gender and Weekday among other data. Output:  List of dicts with one hot encoded representations for County, Gender, and Weekday.  Other data in dict is not changed."""
  
  ecd = ec.encode_county()
  
  enc_wk = ew.encode_weekday()

  for item in encode_covid_data:
    item['COUNTY'] = ec.county_lookup(item['COUNTY'].upper(), ecd)
    item['DATE']['WEEKDAY'] = ew.weekday_encoding_lookup(item['DATE']['WEEKDAY'], enc_wk)
    item['GENDER'] = eg.encode_gender(item['GENDER'])
  return encode_covid_data

def print_data(output_filename, encoded_data_output):
  """Prints the list of dicts with one hot encoded values to a file."""
  with open(output_filename, 'w') as f:
    json.dump(encoded_data_output, f)
  

