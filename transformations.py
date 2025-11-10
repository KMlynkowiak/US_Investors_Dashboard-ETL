import pandas as pd
import numpy as np
# Importuje wszystkie słowniki z pliku mappings.py
from mappings import *

# === FUNKCJE TRANSFORMACJI ===

def transformuj_dane_2009(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2009
    
    # --- Rdzeń (Core) ---
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
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = pd.to_numeric(df_raw['K_2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" ---
    df_clean['ma_kredyt_studencki'] = np.nan
    df_clean['inwestuje_w_krypto'] = np.nan
    df_clean['uczestniczyl_w_edukacji_fin'] = np.nan
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = np.nan
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = np.nan
    df_clean['ma_prace_dodatkowa'] = np.nan

    return df_clean

# W pliku transformations.py ZASTĄP TĘ FUNKCJĘ:

def transformuj_dane_2012(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2012
    
    # --- Rdzeń (Core) ---
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
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = pd.to_numeric(df_raw['K_2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" (Z POPRAWKĄ) ---
    # POPRAWKA: Prawidłowa kolumna to 'G20', a nie 'F1_2012'
    df_clean['ma_kredyt_studencki'] = pd.to_numeric(df_raw['G20'], errors='coerce').map(MAP_BOOLEAN)
    
    df_clean['inwestuje_w_krypto'] = np.nan
    df_clean['uczestniczyl_w_edukacji_fin'] = np.nan
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = np.nan
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = np.nan
    df_clean['ma_prace_dodatkowa'] = np.nan

    return df_clean

def transformuj_dane_2015(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2015
    
    # --- Rdzeń (Core) ---
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
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = np.nan # Zniknęła
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" ---
    df_clean['ma_kredyt_studencki'] = pd.to_numeric(df_raw['G20'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_w_krypto'] = np.nan
    df_clean['uczestniczyl_w_edukacji_fin'] = np.nan
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = np.nan
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = pd.to_numeric(df_raw['J20'], errors='coerce').map(MAP_FUNDUSZ_PEWNOSC)
    df_clean['ma_prace_dodatkowa'] = np.nan

    return df_clean

def transformuj_dane_2018(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2018
    
    # --- Rdzeń (Core) ---
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
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = np.nan # Zniknęła
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" ---
    df_clean['ma_kredyt_studencki'] = pd.to_numeric(df_raw['G20'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_w_krypto'] = pd.to_numeric(df_raw['C40'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['uczestniczyl_w_edukacji_fin'] = pd.to_numeric(df_raw['M20'], errors='coerce').map(MAP_EDUKACJA_FIN)
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = pd.to_numeric(df_raw['J42_1'], errors='coerce').map(MAP_KONIEC_MIESIACA)
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = pd.to_numeric(df_raw['J20'], errors='coerce').map(MAP_FUNDUSZ_PEWNOSC)
    df_clean['ma_prace_dodatkowa'] = pd.to_numeric(df_raw['A40'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2021(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2021
    
    # --- Rdzeń (Core) ---
    df_clean['stan'] = df_raw['STATEQ'].map(MAP_STATEQ)
    df_clean['plec'] = df_raw['A50A'].map(MAP_A50A_PLEC_2021_PLUS)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(MAP_A3AR_W_WIEK)
    df_clean['plec_wiek'] = df_raw['A50B'].map(MAP_A50B_PLEC_WIEK_2021_PLUS)
    df_clean['edukacja'] = df_raw['A5_2015'].map(MAP_A5_EDUKACJA_2015_PLUS)
    df_clean['stan_cywilny'] = df_raw['A6'].map(MAP_A6_STAN_CYWILNY)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(MAP_A7_SYT_MIESZKANIOWA)
    df_clean['dochod_roczny'] = df_raw['A8_2021'].map(MAP_A8_DOCHOD_2021) 
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(MAP_A9_ZATRUDNIENIE)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(MAP_A11_DZIECI)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(MAP_J4_RACHUNKI)
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = np.nan # Zniknęła
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" ---
    df_clean['ma_kredyt_studencki'] = pd.to_numeric(df_raw['G20'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_w_krypto'] = pd.to_numeric(df_raw['P50'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['uczestniczyl_w_edukacji_fin'] = pd.to_numeric(df_raw['M20'], errors='coerce').map(MAP_EDUKACJA_FIN)
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = pd.to_numeric(df_raw['J42_1'], errors='coerce').map(MAP_KONIEC_MIESIACA)
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = pd.to_numeric(df_raw['J20'], errors='coerce').map(MAP_FUNDUSZ_PEWNOSC)
    df_clean['ma_prace_dodatkowa'] = pd.to_numeric(df_raw['A40'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean

def transformuj_dane_2024(df_raw):
    df_clean = pd.DataFrame()
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2024
    
    # --- Rdzeń (Core) ---
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
    j2_numeric = pd.to_numeric(df_raw['J2'], errors='coerce')
    df_clean['sklonnosc_do_ryzyka'] = j2_numeric.replace([98, 99], np.nan)
    df_clean['ma_fund_awaryjny'] = pd.to_numeric(df_raw['J5'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['liczyl_oszcz_emerytalne'] = pd.to_numeric(df_raw['J8'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['pytal_o_porade_inwest'] = np.nan # Zniknęła
    df_clean['ma_konto_oszczednosciowe'] = pd.to_numeric(df_raw['B2'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['inwestuje_poza_emerytura'] = pd.to_numeric(df_raw['B14A_1'], errors='coerce').map(MAP_BOOLEAN)

    # --- NOWE KOLUMNY "V2" ---
    df_clean['ma_kredyt_studencki'] = pd.to_numeric(df_raw['G30_97'], errors='coerce').map(MAP_KREDYT_STUDENCKI_2024)
    df_clean['inwestuje_w_krypto'] = pd.to_numeric(df_raw['B14A_60'], errors='coerce').map(MAP_BOOLEAN)
    df_clean['uczestniczyl_w_edukacji_fin'] = pd.to_numeric(df_raw['M20'], errors='coerce').map(MAP_EDUKACJA_FIN)
    df_clean['ma_pieniadze_na_koniec_miesiaca'] = pd.to_numeric(df_raw['J42_1'], errors='coerce').map(MAP_KONIEC_MIESIACA)
    df_clean['pewnosc_funduszu_awaryjnego_2k'] = pd.to_numeric(df_raw['J20'], errors='coerce').map(MAP_FUNDUSZ_PEWNOSC)
    df_clean['ma_prace_dodatkowa'] = pd.to_numeric(df_raw['A40'], errors='coerce').map(MAP_BOOLEAN)

    return df_clean