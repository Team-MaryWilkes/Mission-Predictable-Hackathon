def encode_county():
  """Dictionary of Florida county names, with corresponding FIPS code.  Input: None. Output:  One Hot Encoding vector encoding of county. Note:  encoded vector is 67 elements long and the 1 value is based on index of county in dictionary (not the FIPS code, for our purposes the FIPS code is irrelevant).  For example, ALACHUA is encoded as [1,0,0,0,....0], BAKER is encoded as [0,1,0,0,0,...0]. Note: There is a field for UNKNOWN county.  """

  county_dict = {
      "ALACHUA": {
        "FIPS": 1, 
        "TOTAL_POPULATION": 269043},
      "BAKER":	{
        "FIPS": 3,
        "TOTAL_POPULATION": 29210},
      "BAY": {
        "FIPS":	5,
        "TOTAL_POPULATION": 174705},
      "BRADFORD":	{
        "FIPS":	7,
        "TOTAL_POPULATION": 28201},
      "BREVARD": {
        "FIPS":	9,
        "TOTAL_POPULATION": 601942},
      "BROWARD":	{
        "FIPS":	11,
        "TOTAL_POPULATION": 1952778},
      "CALHOUN": {
        "FIPS":	13,
        "TOTAL_POPULATION": 14105},
      "CHARLOTTE": {
        "FIPS":	15,
        "TOTAL_POPULATION": 188910},
      "CITRUS":	{
        "FIPS":	17,
        "TOTAL_POPULATION": 149657},
      "CLAY":	{
        "FIPS":	19,
        "TOTAL_POPULATION": 219252},
      "COLLIER":	{
        "FIPS":	21,
        "TOTAL_POPULATION": 384902},
      "COLUMBIA":	{
        "FIPS":	23,
        "TOTAL_POPULATION": 71686},
      "DADE":	{
        "FIPS":	25,
        "TOTAL_POPULATION": 2716940},
      "DESOTO":	{
        "FIPS":	27,
        "TOTAL_POPULATION": 38001},
      "DIXIE":	{
        "FIPS":	29,
        "TOTAL_POPULATION": 16826},
      "DUVAL":	{
        "FIPS":	31,
        "TOTAL_POPULATION": 957755},
      "ESCAMBIA":	{
        "FIPS":	33,
        "TOTAL_POPULATION": 318316},
      "FLAGLER":	{
        "FIPS":	35,
        "TOTAL_POPULATION": 115081},
      "FRANKLIN":	{
        "FIPS":	37,
        "TOTAL_POPULATION": 12125},
      "GADSDEN":	{
        "FIPS":	39,
        "TOTAL_POPULATION": 45660},
      "GILCHRIST":	{
        "FIPS": 41,
        "TOTAL_POPULATION": 18582},
      "GLADES":	{
        "FIPS":	43,
        "TOTAL_POPULATION": 13811},
      "GULF":	{
        "FIPS":	45,
        "TOTAL_POPULATION": 13639},
      "HAMILTON":	{
        "FIPS":	47,
        "TOTAL_POPULATION": 14428},
      "HARDEE":	{
        "FIPS":	49,
        "TOTAL_POPULATION": 26937},
      "HENDRY":	{
        "FIPS":	51,
        "TOTAL_POPULATION": 42022},
      "HERNANDO":	{
        "FIPS":	53,
        "TOTAL_POPULATION": 193920},
      "HIGHLANDS":	{
        "FIPS":	55,
        "TOTAL_POPULATION": 106221},
      "HILLSBOROUGH":	{
        "FIPS":	57,
        "TOTAL_POPULATION": 1471968},
      "HOLMES":	{
        "FIPS":	59,
        "TOTAL_POPULATION": 19617},
      "INDIAN RIVER":	{
        "FIPS":	61,
        "TOTAL_POPULATION": 159923},
      "JACKSON":	{
        "FIPS":	63,
        "TOTAL_POPULATION": 46414},
      "JEFFERSON": {
        "FIPS":	65,
        "TOTAL_POPULATION": 14246},
      "LAFAYETTE":	{
        "FIPS":	67,
        "TOTAL_POPULATION": 8422},
      "LAKE":	{
        "FIPS":	69,
        "TOTAL_POPULATION": 367118},
      "LEE":	{
        "FIPS":	71,
        "TOTAL_POPULATION": 770577},
      "LEON":	{
        "FIPS":	73,
        "TOTAL_POPULATION": 293582},
      "LEVY":	{
        "FIPS":	75,
        "TOTAL_POPULATION": 41503},
      "LIBERTY":	{
        "FIPS":	77,
        "TOTAL_POPULATION": 8354},
      "MADISON":	{
        "FIPS":	79,
        "TOTAL_POPULATION": 18493},
      "MANATEE":	{
        "FIPS":	81,
        "TOTAL_POPULATION": 403253},
      "MARION":	{
        "FIPS":	83,
        "TOTAL_POPULATION": 365579},
      "MARTIN":	{
        "FIPS":	85,
        "TOTAL_POPULATION": 161000},
      "MONROE":	{
        "FIPS":	87,
        "TOTAL_POPULATION": 74228},
      "NASSAU":	{
        "FIPS":	89,
        "TOTAL_POPULATION": 88625},
      "OKALOOSA":	{
        "FIPS":	91,
        "TOTAL_POPULATION": 210738},
      "OKEECHOBEE":	{
        "FIPS":	93,
        "TOTAL_POPULATION": 42168},
      "ORANGE":	{
        "FIPS":	95,
        "TOTAL_POPULATION": 1393452},
      "OSCEOLA":	{
        "FIPS":	97,
        "TOTAL_POPULATION": 375751},
      "PALM BEACH":	{
        "FIPS":	99,
        "TOTAL_POPULATION": 1496770},
      "PASCO":	{
        "FIPS":	101,
        "TOTAL_POPULATION": 553947},
      "PINELLAS":	{
        "FIPS":	103,
        "TOTAL_POPULATION": 974996},
      "POLK":	{
        "FIPS":	105,
        "TOTAL_POPULATION": 724777},
      "PUTNAM":	{
        "FIPS":	107,
        "TOTAL_POPULATION": 74521},
      "SANTA ROSA":	{
        "FIPS":	113,
        "TOTAL_POPULATION": 184313},
      "SARASOTA":	{
        "FIPS":	115,
        "TOTAL_POPULATION": 433742},
      "SEMINOLE":	{
        "FIPS":	117,
        "TOTAL_POPULATION": 471826},
      "ST. JOHNS":	{
        "FIPS":	109,
        "TOTAL_POPULATION": 264672},
      "ST. LUCIE":	{
        "FIPS":	111,
        "TOTAL_POPULATION": 328297},
      "SUMTER":	{
        "FIPS":	119,
        "TOTAL_POPULATION": 132420},
      "SUWANNEE": {
        "FIPS":	121,
        "TOTAL_POPULATION": 44417},
      "TAYLOR":	{
        "FIPS":	123,
        "TOTAL_POPULATION": 21569},
      "UNION":	{
        "FIPS":	125,
        "TOTAL_POPULATION": 15237},
      "VOLUSIA":	{
        "FIPS":	127,
        "TOTAL_POPULATION": 553284},
      "WAKULLA":	{
        "FIPS":	129,
        "TOTAL_POPULATION": 33739},
      "WALTON":	{
        "FIPS":	131,
        "TOTAL_POPULATION": 74071},
      "WASHINGTON":	{
        "FIPS":	133,
        "TOTAL_POPULATION": 25473},
      "UNKNOWN": {
        "FIPS":	-1,
        "TOTAL_POPULATION": -1},
  }

  encoded_county_dict = {}
  county_vector = [0]*68
  county_keys = list(county_dict)

  for index in range(len(county_vector)):
    encoded_vector = county_vector.copy()
    encoded_vector[index] = 1
    encoded_county_dict[county_keys[index]] = encoded_vector
  
  return encoded_county_dict

def county_lookup(name_of_county, encoded_dict):
  """Look up county in encoded_county_dict and return vector encoding. Input:  String name_of_county Output:  vector encoding"""
  return encoded_dict[name_of_county]


  

#How to use these functions...
# ecd = encode_county()
# washington_code = county_lookup("WASHINGTON", ecd)
# print(washington_code)
