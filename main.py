import pandas as pd
import os
# Importuje wszystkie funkcje transformujące z pliku obok
from transformations import *

def main():
    
    data_raw_dir = "data_raw"
    output_dir = "output"

    # Lista plików CSV w folderze data_raw
    lista_plikow = [
        f"{data_raw_dir}/NFCS 2009 State Data 220712.csv",
        f"{data_raw_dir}/NFCS 2012 State Data 130503.csv",
        f"{data_raw_dir}/NFCS 2015 State Data 160619.csv",
        f"{data_raw_dir}/NFCS 2018 State Data 190603.csv",
        f"{data_raw_dir}/NFCS 2021 State Data 220627.csv",
        f"{data_raw_dir}/NFCS 2024 State Data 250623.csv", 
    ]
    
    lista_clean_df = [] # Lista na gotowe DataFrames
    
    for plik_csv in lista_plikow:
        print(f"Przetwarzanie pliku: {plik_csv}...")
        try:
            df_raw = pd.read_csv(plik_csv, low_memory=False) 
            
            # "Router" - decyduje, którą funkcję transformującą wywołać
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
            print("Sprawdź, czy nazwy kolumn w funkcjach transformujących są poprawne dla tego roku.")
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

# Uruchamia funkcję main() tylko wtedy, gdy plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()