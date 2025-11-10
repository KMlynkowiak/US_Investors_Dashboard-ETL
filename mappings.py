import numpy as np

# === SŁOWNIKI MAPUJĄCE (KONFIGURACJA) ===

MAP_STATEQ = {
    1: 'Alabama', 2: 'Alaska', 3: 'Arizona', 4: 'Arkansas', 5: 'California',
    6: 'Colorado', 7: 'Connecticut', 8: 'Delaware', 9: 'District of Columbia',
    10: 'Florida', 11: 'Georgia', 12: 'Hawaii', 13: 'Idaho', 14: 'Illinois',
    15: 'Indiana', 16: 'Iowa', 17: 'Kansas', 18: 'Kentucky', 19: 'Louisiana',
    20: 'Maine', 21: 'Maryland', 22: 'Massachusetts', 23: 'Michigan',
    24: 'Minnesota', 25: 'Mississippi', 26: 'Missouri', 27: 'Montana',
    28: 'Nebraska', 29: 'Nevada', 30: 'New Hampshire', 31: 'New Jersey',
    32: 'New Mexico', 33: 'New York', 34: 'North Carolina', 35: 'North Dakota',
    36: 'Ohio', 37: 'Oklahoma', 38: 'Oregon', 39: 'Pennsylvania',
    40: 'Rhode Island', 41: 'South Carolina', 42: 'South Dakota', 43: 'Tennessee',
    44: 'Texas', 45: 'Utah', 46: 'Vermont', 47: 'Virginia', 48: 'Washington',
    49: 'West Virginia', 50: 'Wisconsin', 51: 'Wyoming'
}
MAP_A3_PLEC = {1: 'Male', 2: 'Female'} # Dla 2009-2018
MAP_A3AR_W_WIEK = {
    1: '18-24', 2: '25-34', 3: '35-44',
    4: '45-54', 5: '55-64', 6: '65+'
}
MAP_A3B_PLEC_WIEK = { # Dla 2009-2018
    1: 'Male 18-24', 2: 'Male 25-34', 3: 'Male 35-44',
    4: 'Male 45-54', 5: 'Male 55-64', 6: 'Male 65+',
    7: 'Female 18-24', 8: 'Female 25-34', 9: 'Female 35-44',
    10: 'Female 45-54', 11: 'Female 55-64', 12: 'Female 65+'
}
# Mapa edukacji dla 2009-2012
MAP_A5_EDUKACJA_2009_2012 = {
    1: 'Did not complete high school', 2: 'High school graduate',
    3: 'Some college', 4: 'College graduate', 5: 'Post graduate education',
    99: np.nan
}
# Mapa edukacji dla 2015+
MAP_A5_EDUKACJA_2015_PLUS = {
    1: 'Did not complete high school',
    2: 'High school graduate',
    3: 'High school graduate', # GED
    4: 'Some college',
    5: 'Associate\'s degree',
    6: 'Bachelor\'s degree',
    7: 'Post graduate degree',
    99: np.nan
}
MAP_A6_STAN_CYWILNY = {
    1: 'Married', 2: 'Single', 3: 'Separated',
    4: 'Divorced', 5: 'Widowed/widower', 99: np.nan
}
MAP_A7_SYT_MIESZKANIOWA = {
    1: 'Only adult in household',
    2: 'Live with spouse/partner',
    3: "Live in parents' home",
    4: 'Live with other family/friends',
    99: np.nan
}
# Mapa dochodu dla 2009-2018 ORAZ 2024
MAP_A8_DOCHOD_2009_2018_2024 = {
    1: '< $15,000', 2: '$15k - $25k', 3: '$25k - $35k',
    4: '$35k - $50k', 5: '$50k - $75k', 6: '$75k - $100k',
    7: '$100k - $150k', 
    8: '$150k or more', # Scalamy 8, 9, 10 z 2024
    9: '$150k or more',
    10: '$150k or more',
    98: np.nan, 99: np.nan
}
# Mapa dochodu TYLKO dla 2021
MAP_A8_DOCHOD_2021 = {
    1: '< $20,000',
    2: '$20k - $30k',
    3: '$30k - $40k',
    4: '$40k - $50k',
    5: '$50k - $60k',
    6: '$60k - $75k',
    7: '$75k - $100k',
    8: '$100k - $125k',
    9: '$125k - $150k',
    10: '$150k or more',
    98: np.nan, 99: np.nan
}
MAP_A9_ZATRUDNIENIE = {
    1: 'Full-time', 2: 'Full-time', 3: 'Part-time',
    4: 'Homemaker', 5: 'Student', 6: 'Unemployed',
    7: 'Unemployed', 8: 'Retired', 99: np.nan
}
MAP_A11_DZIECI = {
    1: '1', 2: '2', 3: '3+', 4: '3+',
    5: '0', 6: '0', 99: np.nan
}
MAP_J4_RACHUNKI = {
    1: 'Very difficult', 2: 'Somewhat difficult',
    3: 'Not at all difficult', 98: np.nan, 99: np.nan
}
MAP_BOOLEAN = {
    1: True,
    2: False,
}

# --- Mapowania Specyficzne (dla 2021+) ---
MAP_A50A_PLEC_2021_PLUS = {
    1: 'Male',
    2: 'Female',
    3: 'Non-binary',
    4: np.nan
}
MAP_A50B_PLEC_WIEK_2021_PLUS = {
    1: 'Male 18-24', 2: 'Male 25-34', 3: 'Male 35-44',
    4: 'Male 45-54', 5: 'Male 55-64', 6: 'Male 65+',
    7: 'Female 18-24', 8: 'Female 25-34', 9: 'Female 35-44',
    10: 'Female 45-54', 11: 'Female 55-64', 12: 'Female 65+',
    13: 'Non-binary 18-24', 14: 'Non-binary 25-34', 15: 'Non-binary 35-44',
    16: 'Non-binary 45-54', 17: 'Non-binary 55-64', 18: 'Non-binary 65+'
}