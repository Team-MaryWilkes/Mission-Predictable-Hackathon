import re
import datetime

# POSSIBLE ISSUE: ...PROCESS FILE LINE BY LINE RATHER THAN ALL AT ONCE...OR BY CHUNKS
def extract_data(filename):
  """Opens and reads a txt file line by line and extracts #record_num, county, age, gender, month,day, year in to two lists of dictionaries, one for female data, one for male data.  Returns the two lists."""
  female_data_regex = re.compile(r"\D*(\d*[,]*\d*[,]*\d+)(\D+)(\d+)(Female)\D+(\d\d)/(\d\d)/(\d\d)")
  male_data_regex = re.compile(r"\D*(\d*[,]*\d*[,]*\d+)(\D+)(\d+)(Male)\D+(\d\d)/(\d\d)/(\d\d)")

  female_list = []
  female_case = {}
  male_list = []
  male_case = {}
  
  with open (filename, "r") as f:
    for line in f:
      try:
        female_result = female_data_regex.match(line)
        female_case['CASE'] = ''.join(s for s in female_result.group(1) if s.isdigit())
        female_case['COUNTY'] = female_result.group(2)
        female_case['AGE'] = female_result.group(3)
        female_case['GENDER'] = female_result.group(4)
        female_case['DATE'] = {
          'MONTH': female_result.group(5),
          'DAY': female_result.group(6),
          'YEAR': '20' + female_result.group(7),
          "WEEKDAY" : (datetime.date(int('20' + female_result.group(7)),int(female_result.group(5)), int(female_result.group(6)))).strftime("%A"),}
        
        new_case = female_case.copy()
        female_list.append(new_case)
      
      except AttributeError:
        pass
    
        
      try:
        male_result = male_data_regex.match(line)
        male_case['CASE'] = ''.join(s for s in male_result.group(1) if s.isdigit())
        male_case['COUNTY'] = male_result.group(2)
        male_case['AGE'] = male_result.group(3)
        male_case['GENDER'] = male_result.group(4)
        male_case['DATE'] = {
          'MONTH': male_result.group(5),
          'DAY': male_result.group(6),
          'YEAR': '20' + male_result.group(7),
          'WEEKDAY': (datetime.date(int('20' + male_result.group(7)),int(male_result.group(5)), int(male_result.group(6)))).strftime("%A"),}
        new_case = male_case.copy()
        male_list.append(new_case)
      except AttributeError:
        pass


  return female_list, male_list
 


