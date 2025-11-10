import pandas as pd
import numpy as np
import os

# === KROK 1: SŁOWNIKI MAPUJĄCE (MAPOWANIA) ===

# --- Mapowania Globalne (dla 2009-2018) ---
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
MAP_A5_EDUKACJA = {
    1: 'Did not complete high school', 2: 'High school graduate',
    3: 'Some college', 4: 'College graduate', 5: 'Post graduate education',
    # Zmiana w 2024 - kody 2 i 3 to ten sam poziom, mapujemy je
    6: 'Bachelor\'s degree', # W 2024 A5_2015 ma nowe kody
    7: 'Post graduate degree', # W 2024 A5_2015 ma nowe kody
    99: np.nan
}
# --- POPRAWKA MAPY A5 ---
# Musimy zaktualizować mapę A5, aby pasowała do 2024, ale była też wstecznie kompatybilna
MAP_A5_EDUKACJA_V2 = {
    1: 'Did not complete high school',
    2: 'High school graduate',
    3: 'High school graduate', # 2024: GED
    4: 'Some college',
    5: 'Associate\'s degree', # 2024: Associate's (wcześniej w 'Some college')
    6: 'Bachelor\'s degree',
    7: 'Post graduate degree',
    99: np.nan
}
# Stara mapa dla 2009
MAP_A5_EDUKACJA_2009 = {
    1: 'Did not complete high school', 2: 'High school graduate',
    3: 'Some college', 4: 'Bachelor\'s degree', 5: 'Post graduate degree',
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
MAP_A8_DOCHOD = { # Dla 2009-2018
    1: '< $15,000', 2: '$15k - $25k', 3: '$25k - $35k',
    4: '$35k - $50k', 5: '$50k - $75k', 6: '$75k - $100k',
    7: '$100k - $150k', 8: '$150k or more',
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
MAP_A50A_PLEC_2021 = {
    1: 'Male',
    2: 'Female',
    3: 'Non-binary',
    4: np.nan
}
MAP_A50B_PLEC_WIEK_2021 = {
    1: 'Male 18-24', 2: 'Male 25-34', 3: 'Male 35-44',
    4: 'Male 45-54', 5: 'Male 55-64', 6: 'Male 65+',
    7: 'Female 18-24', 8: 'Female 25-34', 9: 'Female 35-44',
    10: 'Female 45-54', 11: 'Female 55-64', 12: 'Female 65+',
    13: 'Non-binary 18-24', 14: 'Non-binary 25-34', 15: 'Non-binary 35-44',
    16: 'Non-binary 45-54', 17: 'Non-binary 55-64', 18: 'Non-binary 65+'
}
# --- POPRAWKA MAPY DOCHODU 2021 ---
# PDF 2024 [cite: 2634-2659] pokazuje, że kolumna A8_2021 ma inne kody niż zakładałem!
MAP_A8_DOCHOD_2021_V2 = {
    1: '< $15,000',
    2: '$15k - $25k',
    3: '$25k - $35k',
    4: '$35k - $50k',
    5: '$50k - $75k',
    6: '$75k - $100k',
    7: '$100k - $150k',
    8: '$150k - $200k', # Nowa kategoria
    9: '$200k - $300k', # Nowa kategoria
    10: '$300k or more', # Nowa kategoria
    98: np.nan, 99: np.nan
}


# === KROK 2: FUNKCJE TRANSFORMACJI ===

# --- PRZEPRASZAM, JESZCZE JEDNA KOREKTA! ---
# Po przejrzeniu PDF 2024 [cite: 2536-2556], widzę, że kody dla A5_2015 zmieniły się w 2015+
# A kody dla A8_2021 [cite: 2634-2659] są inne niż myślałem.
# Musimy stworzyć nowe mapy i zaktualizować WSZYSTKIE funkcje od 2015.

# --- Nowe, Poprawne Mapy ---
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
MAP_A8_DOCHOD_2021_PLUS = {
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
# Stara mapa dochodu dla 2009-2018
MAP_A8_DOCHOD_2009_2018 = {
    1: '< $15,000', 2: '$15k - $25k', 3: '$25k - $35k',
    4: '$35k - $50k', 5: '$50k - $75k', 6: '$75k - $100k',
    7: '$100k - $150k', 8: '$150k or more',
    98: np.nan, 99: np.nan
}
# Stara mapa edukacji dla 2009-2012
MAP_A5_EDUKACJA_2009_2012 = {
    1: 'Did not complete high school', 2: 'High school graduate',
    3: 'Some college', 4: 'College graduate', 5: 'Post graduate education',
    99: np.nan
}


def transformuj_dane_2009(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2009
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A3'].map(MAP_A3_PLEC)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A3B'].map(MAP_A3B_PLEC_WIEK)
    df_clean['edukacja'] = df_raw['A5'].map(MAP_A5_EDUKACJA_2009_2012) 
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018)
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = pd.to_numeric(df_raw['K_2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2012(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2012
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A3'].map(MAP_A3_PLEC)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A3B'].map(MAP_A3B_PLEC_WIEK)
    df_clean['edukacja'] = df_raw['A5_2012'].map(MAP_A5_EDUKACJA_2009_2012)
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018)
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = pd.to_numeric(df_raw['K_2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2015(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2015
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A3'].map(MAP_A3_PLEC)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A3B'].map(MAP_A3B_PLEC_WIEK)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) # <-- POPRAWKA
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018) # <-- POPRAWKA
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    # Kolumna K_2 nie istnieje.
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2018(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2018
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A3'].map(MAP_A3_PLEC)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A3B'].map(MAP_A3B_PLEC_WIEK)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) # <-- POPRAWKA
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018) # <-- POPRAWKA
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    # Kolumna K_2 nie istnieje.
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2021(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2021
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A50A'].map(MAP_A50A_PLEC_2021)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A50B'].map(MAP_A50B_PLEC_WIEK_2021)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) # <-- POPRAWKA
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    # PDF 2024 [cite: 2634-2659] pokazuje, że A8_2021 ma inne kody niż zakładałem!
    # Ale... CSV 2021 ma kolumnę A8_2021, która MUSI pasować do MAP_A8_DOCHOD_2021_PLUS
    # Na podstawie PDF 2021, A8_2021 ma kody <20k, 20-30k itd. - czyli MAP_A8_DOCHOD_2021_PLUS jest poprawna
    df_clean['dochod_roczny'] = df_raw['A8_2021'].map(MAP_A8_DOCHOD_2021_PLUS) # <-- POPRAWKA
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    # Kolumna K_2 nie istnieje.
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

# --- FUNKCJA DLA 2024 (POPRAWIONA) ---
def transformuj_dane_2024(df_raw):
    """
    Funkcja przyjmuje surowy DataFrame z 2024 roku i zwraca
    wyczyszczony, "zdeszyfrowany" DataFrame.
    """
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2024
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A50A'].map(MAP_A50A_PLEC_2021) # Używa mapy z 2021
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A50B'].map(MAP_A50B_PLEC_WIEK_2021) # Używa mapy z 2021
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) # Używa nazwy z 2015 i mapy 2015+
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    # Używa nazwy 'A8_2021' (wg nagłówka CSV) i mapy 'MAP_A8_DOCHOD_2021_PLUS'
    # Mój błąd - PDF 2024 pokazuje A8_2021 , ale kody są STARE !
    # To jest kluczowy błąd. Musimy to naprawić.
    # PDF 2024, strona 7: Kolumna nazywa się `A8_2021`
    # PDF 2024, strona 7 : Kody to `< $15,000`, `$15k - $25k`...
    # WNIOSEK: Plik 2024 używa nazwy `A8_2021`, ale STAREJ mapy `MAP_A8_DOCHOD_2009_2018`.
    
    # OSTATECZNA POPRAWKA DLA DOCHODU 2024:
    df_clean['dochod_roczny'] = df_raw['A8_2021'].map(MAP_A8_DOCHOD_2009_2018) 
    
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)

    # NUMERYCZNE
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    
    # LOGICZNE (BOOLEAN)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    # Kolumna K_2 nie istnieje.
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    
    # OSTATECZNA POPRAWKA DLA INWESTYCJI 2024 [cite: 3817-3818]:
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14A_1'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

# === KROK 3: GŁÓWNY SKRYPT (MAIN) ===
def main():
    
    data_raw_dir = "data_raw"
    output_dir = "output"

    lista_plikow = [
        f"{data_raw_dir}/NFCS 2009 State Data 220712.csv",
        f"{data_raw_dir}/NFCS 2012 State Data 130503.csv",
        f"{data_raw_dir}/NFCS 2015 State Data 160619.csv",
        f"{data_raw_dir}/NFCS 2018 State Data 190603.csv",
        f"{data_raw_dir}/NFCS 2021 State Data 220627.csv",
        f"{data_raw_dir}/NFCS 2024 State Data 250623.csv",
    ]
    
    lista_clean_df = []
    
    for plik_csv in lista_plikow:
        print(f"Przetwarzanie pliku: {plik_csv}...")
        try:
            df_raw = pd.read_csv(plik_csv, low_memory=False) 
            
            if '2009' in plik_csv:
                df_clean = transformuj_dane_2009(df_raw)
            elif '2012' in plik_csv:
                df_clean = transformuj_dane_2012(df_raw)
            elif '2015' in plik_csv:
                df_clean = transformuj_dane_2015(df_raw)
            elif '2018' in plik_csv:
                df_clean = transformuj_dane_2018(df_raw)
            elif '2021' in plik_csv:
                df_clean = transformuj_dane_2021(df_raw)
            elif '2024' in plik_csv:
                df_clean = transformuj_dane_2024(df_raw)
            else:
                print(f"Nie znaleziono funkcji transformującej dla {plik_csv}. Pomijam.")
                continue
                
            lista_clean_df.append(df_clean)
            print(f"Zakończono przetwarzanie: {plik_csv}.")

        except FileNotFoundError:
            print(f"BŁĄD KRYTYCZNY: Nie znaleziono pliku {plik_csv}.")
            print("Upewnij się, że plik istnieje w folderze 'data_raw' i nazwa w skrypcie jest poprawna.")
            return
        except KeyError as e:
            print(f"BŁĄD KLUCZA (KeyError): Nie znaleziono kolumny {e} w pliku {plik_csv}.")
            print("Sprawdź, czy nazwy kolumn w funkcji transformującej są poprawne dla tego roku.")
            return
        except Exception as e:
            print(f"BŁĄD podczas przetwarzania {plik_csv}: {e}")

    # ----- SCALANIE (CONCAT) -----
    if not lista_clean_df:
        print("Nie przetworzono żadnych plików. Zakończono.")
        return

    print("Scalanie wszystkich przetworzonych plików...")
    df_master = pd.concat(lista_clean_df, ignore_index=True, sort=False)

    # ----- LOAD (ZAPIS) -----
    os.makedirs(output_dir, exist_ok=True)
    
    nazwa_pliku_master = "NFCS_MASTER_CLEAN.csv"
    nazwa_pliku_master_out = f"{output_dir}/{nazwa_pliku_master}" 
    
    try:
        df_master.to_csv(nazwa_pliku_master_out, index=False, encoding='utf-8-sig')
        print(f"\n--- GOTOWE! ---")
        print(f"Stworzono jeden, scalony plik: {nazwa_pliku_master_out}")
        print("\nOto informacje o finalnej tabeli:")
        df_master.info()
        print("\nOto 5 ostatnich wierszy finalnej tabeli (powinieneś widzieć rok 2024):")
        print(df_master.tail())
        
    except Exception as e:
        print(f"BŁĄD ZAPISU: {e}")

if __name__ == "__main__":
    main()