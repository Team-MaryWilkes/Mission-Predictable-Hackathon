def encode_gender(gender):
  """Encode Female as [1,0].  Encode Male as [0,1]."""
  if gender == "Female":
    return [1,0]
  elif gender == "Male":
    return [0,1]
  else:
    return None