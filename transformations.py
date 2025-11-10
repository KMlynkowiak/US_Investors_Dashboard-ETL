import pandas as pd
import numpy as np
# Importuje wszystkie słowniki z pliku obok
from etl.mappings import *

# === FUNKCJE TRANSFORMACJI ===

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
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018_2024)
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
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018_2024)
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
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) 
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018_2024) 
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
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS) 
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8'].map(MAP_A8_DOCHOD_2009_2018_2024) 
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
    df_clean['plec'] = df_raw['A50A'].map(MAP_A50A_PLEC_2021_PLUS)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A50B'].map(MAP_A50B_PLEC_WIEK_2021_PLUS)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS)
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8_2021'].map(MAP_A8_DOCHOD_2021) # Używa mapy 2021
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

def transformuj_dane_2024(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2024
    
    # KATEGORYCZNE
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A50A'].map(MAP_A50A_PLEC_2021_PLUS)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A50B'].map(MAP_A50B_PLEC_WIEK_2021_PLUS)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS)
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8_2021'].map(MAP_A8_DOCHOD_2009_2018_2024) 
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
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14A_1'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean