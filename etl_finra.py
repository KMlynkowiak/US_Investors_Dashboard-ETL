import pandas as pd
import numpy as np

def transformuj_dane_2009(df_raw):
    """
    Funkcja przyjmuje surowy DataFrame z 2009 roku i zwraca
    wyczyszczony, "zdeszyfrowany" DataFrame.
    """
    
    # 1. Definiowanie mapowań (słowników)
    
    map_stateq = {
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
    map_a3 = {1: 'Male', 2: 'Female'}
    map_a3ar_w = {
        1: '18-24', 2: '25-34', 3: '35-44',
        4: '45-54', 5: '55-64', 6: '65+'
    }
    map_a3b = {
        1: 'Male 18-24', 2: 'Male 25-34', 3: 'Male 35-44',
        4: 'Male 45-54', 5: 'Male 55-64', 6: 'Male 65+',
        7: 'Female 18-24', 8: 'Female 25-34', 9: 'Female 35-44',
        10: 'Female 45-54', 11: 'Female 55-64', 12: 'Female 65+'
    }
    map_a5 = {
        1: 'Did not complete high school', 2: 'High school graduate',
        3: 'Some college', 4: 'College graduate', 5: 'Post graduate education',
        99: np.nan
    }
    map_a6 = {
        1: 'Married', 2: 'Single', 3: 'Separated',
        4: 'Divorced', 5: 'Widowed/widower', 99: np.nan
    }
    map_a7 = {
        1: 'Only adult in household',
        2: 'Live with spouse/partner',
        3: "Live in parents' home",
        4: 'Live with other family/friends',
        99: np.nan
    }
    map_a8 = {
        1: '< $15,000', 2: '$15k - $25k', 3: '$25k - $35k',
        4: '$35k - $50k', 5: '$50k - $75k', 6: '$75k - $100k',
        7: '$100k - $150k', 8: '$150k or more',
        98: np.nan, 99: np.nan
    }
    # TWOJE WŁASNE MAPOWANIE (A9)
    map_a9 = {
        1: 'Full-time', 2: 'Full-time', 3: 'Part-time',
        4: 'Homemaker', 5: 'Student', 6: 'Unemployed',
        7: 'Unemployed', 8: 'Retired', 99: np.nan
    }
    # TWOJE WŁASNE MAPOWANIE (A11)
    map_a11 = {
        1: '1', 2: '2', 3: '3 or more', 4: '3 or more',
        5: '0', 6: '0', 99: np.nan
    }
    map_j4 = {
        1: 'Very difficult', 2: 'Somewhat difficult',
        3: 'Not at all difficult', 98: np.nan, 99: np.nan
    }
    # Mapa dla pytań Tak/Nie (Boolean)
    map_boolean = {
        1: True,  # Yes
        2: False, # No
        # Wartości 98, 99 i inne błędy zostaną obsłużone przez pd.to_numeric
    }

    # 2. Tworzymy nową, czystą ramę danych
    df_clean = pd.DataFrame()
    
    # 3. Przypisanie i mapowanie kolumn
    df_clean['respondent_id'] = df_raw['NFCSID']
    df_clean['rok_ankiety'] = 2009
    
    # ---- DANE KATEGORYCZNE ----
    df_clean['stan'] = df_raw['STATEQ'].map(map_stateq)
    df_clean['plec'] = df_raw['A3'].map(map_a3)
    df_clean['grupa_wiekowa'] = df_raw['A3Ar_w'].map(map_a3ar_w)
    df_clean['plec_wiek'] = df_raw['A3B'].map(map_a3b)
    df_clean['edukacja'] = df_raw['A5'].map(map_a5)
    df_clean['stan_cywilny'] = df_raw['A6'].map(map_a6)
    df_clean['syt_mieszkaniowa'] = df_raw['A7'].map(map_a7)
    df_clean['dochod_roczny'] = df_raw['A8'].map(map_a8)
    df_clean['status_zatrudnienia'] = df_raw['A9'].map(map_a9)
    df_clean['liczba_dzieci'] = df_raw['A11'].map(map_a11)
    df_clean['trudnosc_z_rachunkami'] = df_raw['J4'].map(map_j4)

    # ---- DANE NUMERYCZNE (ze skali) ----
    # Skłonność do ryzyka (J2) - skala 1-10
    # pd.to_numeric zamieni 98, 99 i puste komórki na NaN
    df_clean['sklonnosc_do_ryzyka'] = pd.to_numeric(df_raw['J2'], errors='coerce')
    # Zamieniamy 98 i 99 na NaN, ale co z 1-10? Zostawiamy jako liczby.
    df_clean['sklonnosc_do_ryzyka'] = df_clean['sklonnosc_do_ryzyka'].replace([98, 99], np.nan)
    
    # ---- DANE LOGICZNE (Tak/Nie) - POPRAWKA ----
    # Używamy pd.to_numeric(errors='coerce') aby zamienić puste/błędne wartości na NaN,
    # a następnie mapujemy tylko liczby 1 i 2.
    
    # J5: ma_fund_awaryjny
    j5_numeric = pd.to_numeric(df_raw['J5'], errors='coerce')
    df_clean['ma_fund_awaryjny'] = j5_numeric.map(map_boolean)
    
    # J8: liczyl_oszcz_emerytalne
    j8_numeric = pd.to_numeric(df_raw['J8'], errors='coerce')
    df_clean['liczyl_oszcz_emerytalne'] = j8_numeric.map(map_boolean)
    
    # K_2: pytal_o_porade_inwest
    k2_numeric = pd.to_numeric(df_raw['K_2'], errors='coerce')
    df_clean['pytal_o_porade_inwest'] = k2_numeric.map(map_boolean)
    
    # B2: ma_konto_oszczednosciowe
    b2_numeric = pd.to_numeric(df_raw['B2'], errors='coerce')
    df_clean['ma_konto_oszczednosciowe'] = b2_numeric.map(map_boolean)
    
    # B14: inwestuje_poza_emerytura
    b14_numeric = pd.to_numeric(df_raw['B14'], errors='coerce')
    df_clean['inwestuje_poza_emerytura'] = b14_numeric.map(map_boolean)

    return df_clean

# ----- GŁÓWNY SKRYPT -----
def main():
    
    lista_plikow = [
        'NFCS 2009 State Data 220712.csv',
        # 'NFCS_2012.csv', # Odkomentujesz, jak dodasz plik 2012
        # 'NFCS_2015.csv', # Itd.
    ]
    
    lista_clean_df = [] # Lista na czyste ramki danych z każdego roku
    
    for plik_csv in lista_plikow:
        print(f"Przetwarzanie pliku: {plik_csv}...")
        try:
            df_raw = pd.read_csv(plik_csv)
            
            # TODO: Ten 'if' będziesz musiał rozbudować o resztę lat
            if '2009' in plik_csv:
                df_clean = transformuj_dane_2009(df_raw)
            # elif '2012' in plik_csv:
            #     df_clean = transformuj_dane_2012(df_raw) # Musisz napisać tę funkcję
            # elif '2015' in plik_csv:
            #     df_clean = transformuj_dane_2015(df_raw) # Musisz napisać tę funkcję
            else:
                print(f"Nie znaleziono funkcji transformującej dla {plik_csv}. Pomijam.")
                continue
                
            lista_clean_df.append(df_clean)
            print(f"Zakończono przetwarzanie: {plik_csv}.")

        except FileNotFoundError:
            print(f"BŁĄD: Nie znaleziono pliku {plik_csv}.")
        except Exception as e:
            print(f"BŁĄD podczas przetwarzania {plik_csv}: {e}")

    # ----- SCALANIE (CONCAT) -----
    if not lista_clean_df:
        print("Nie przetworzono żadnych plików. Zakończono.")
        return

    print("Scalanie wszystkich przetworzonych plików...")
    # ignore_index=True jest kluczowe, aby zresetować index po scaleniu
    df_master = pd.concat(lista_clean_df, ignore_index=True)

    # ----- LOAD (ZAPIS) -----
    nazwa_pliku_master = "NFCS_MASTER_CLEAN.csv"
    df_master.to_csv(nazwa_pliku_master, index=False, encoding='utf-8-sig')
    
    print("\n--- GOTOWE! ---")
    print(f"Stworzono jeden, scalony plik: {nazwa_pliku_master}")
    print("\nOto informacje o finalnej tabeli:")
    df_master.info()
    print("\nOto 5 pierwszych wierszy finalnej tabeli:")
    print(df_master.head())

# Ten fragment pozwala uruchomić skrypt bezpośrednio z VSC
if __name__ == "__main__":
    main()