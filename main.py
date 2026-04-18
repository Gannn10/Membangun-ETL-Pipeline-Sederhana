import pandas as pd
from utils.extract import scrape_page
from utils.transform import transform_data
import time

def run_etl():
    print("=== Memulai Pipeline ETL Retail Competitor ===")
    
    all_raw_data = []
    base_url = "https://fashion-studio.dicoding.dev"
    
    # --- TAHAP 1: EXTRACT ---
    print(f"\n[1/3] Tahap Extraction: Mengambil data dari 50 halaman...")
    
    for i in range(1, 51):
        # Format URL sesuai pola: https://fashion-studio.dicoding.dev/page/1.html
        url = f"{base_url}/index.html?page={i}" if i > 1 else f"{base_url}/index.html"
        
        try:
            page_data = scrape_page(url)
            if page_data:
                all_raw_data.extend(page_data)
                print(f" Berhasil: Halaman {i} ({len(page_data)} produk)")
            else:
                print(f" Peringatan: Halaman {i} kosong.")
                
            # Beri jeda sedikit agar tidak membebani server (good practice)
            time.sleep(0.1) 
            
        except Exception as e:
            print(f" Error di halaman {i}: {e}")
            continue

    if not all_raw_data:
        print("Gagal mendapatkan data sama sekali. Program dihentikan.")
        return
    # Di dalam main.py, setelah loop extraction selesai
    print(f"Contoh 5 data mentah pertama: {all_raw_data[:5]}")

    print(f"Total data mentah terkumpul: {len(all_raw_data)} baris.")

    # --- TAHAP 2: TRANSFORM ---
    print(f"\n[2/3] Tahap Transformation: Membersihkan data...")
    try:
        clean_df = transform_data(all_raw_data)
        print(f" Data berhasil dibersihkan. Sisa data: {len(clean_df)} baris.")
    except Exception as e:
        print(f" Gagal saat transformasi: {e}")
        return

    # --- TAHAP 3: LOAD ---
    print(f"\n[3/3] Tahap Loading: Menyimpan ke CSV...")
    try:
        # Nama file wajib products.csv sesuai kriteria
        output_file = 'products.csv'
        clean_df.to_csv(output_file, index=False)
        print(f" Sukses! Data disimpan di: {output_file}")
    except Exception as e:
        print(f" Gagal menyimpan file: {e}")

    print("\n=== ETL Selesai dengan Aman! ===")

if __name__ == "__main__":
    run_etl()