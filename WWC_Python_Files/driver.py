import sys
sys.path.append("C:\\Anaconda3\\envs\\my_ml_project\\my_files\\")

#from . import read_pdf as rp #DO NOT DELETE
# Note:  Pylance complains about the import cannot be resolved but functions still run.
import extract_data as ed
import print_covid_data as pd
import encode_data as edata
#Filenames

#pdf file input to read_pdf.py and entire output txt file
input_pdfName = r'C:\Users\Public\Documents\Python\MachineLearning\WomenWhoCode\FloridaCovidDataJuly15_2020\july_16_2020.pdf'
#txt file output from read_pdf.py
output_pdf_to_txt_filename = "florida_covid_july_16_2020.txt"

#manually split read_pdf output file into cases and deaths
#these files used as input to extract_data.py
input_cases_filename = "florida_covid_july_16_2020_cases.txt"
input_deaths_filename = "florida_covid_july_16_2020_deaths.txt"

output_female_cases = "florida_covid_july_16_2020_female_cases.txt"
output_female_deaths = "florida_covid_july_16_2020_female_deaths.txt"

output_male_cases = "florida_covid_july_16_2020_male_cases.txt"
output_male_deaths = "florida_covid_july_16_2020_male_deaths.txt"

#DRIVER FUNCTIONS
# Use this function to read pdf from web file saved on local disk. Don't forget to Uncomment import statement.    
# rp.read_forida_dept_health_pdf(input_pdfName, output_pdf_to_txt_filename)

#USE THESE FUNCTIONS TO EXTRACT DATA FROM FLORIDA DEPT OF HEALTH TXT FILES
#OUTPUT IS 4 TXT FILES CONTAINING JSON LIST OF DICTS
# female_list, male_list = ed.extract_data(input_cases_filename) 
# pd.print_covid_data(female_list, output_female_cases)
# pd.print_covid_data(male_list, output_male_cases)

# female_list, male_list = ed.extract_data(input_deaths_filename) 
# pd.print_covid_data(female_list, output_female_deaths)
# pd.print_covid_data(male_list, output_male_deaths)

#USE THESE FUNCTIONS TO CONVERT DATA TO ONE HOT ENCODED VECTORS
# Note:  UNKNOWN Counties are also encoded.

input_filelist = [output_female_cases, output_female_deaths, output_male_cases, output_male_deaths]

for input_filename in input_filelist:
  data_to_encode = edata.read_file(input_filename)
  data_is_encoded = edata.encode_data(data_to_encode)
  output_filename = "encoded_" + input_filename
  edata.print_data(output_filename, data_is_encoded)
