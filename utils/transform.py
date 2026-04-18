import pandas as pd
import re

def transform_data(raw_list):
    try:
        df = pd.DataFrame(raw_list)
        if df.empty: return df

        # --- 1. HARGA ---
        def clean_price(price_str):
            try:
                # Ambil angka saja. Jika "Price Unavailable", balikkan 0.0
                nums = re.findall(r"(\d+\.\d+|\d+)", str(price_str))
                if nums:
                    return float(nums[0]) * 16000
                return 0.0
            except:
                return 0.0
        df['price'] = df['price'].apply(clean_price)

        # --- 2. RATING ---
        def clean_rating(rating_str):
            try:
                # Ambil angka saja. Jika "Invalid Rating", balikkan 0.0
                nums = re.findall(r"(\d+\.\d+|\d+)", str(rating_str))
                if nums:
                    return float(nums[0])
                return 0.0
            except:
                return 0.0
        df['rating'] = df['rating'].apply(clean_rating)

        # --- 3. COLORS, SIZE, GENDER ---
        df['colors'] = df['colors'].str.extract('(\d+)').fillna(0).astype(int)
        df['size'] = df['size'].str.replace('Size:', '', case=False).str.strip()
        df['gender'] = df['gender'].str.replace('Gender:', '', case=False).str.strip()

        # --- 4. FILTERING (KITA LONGGARKAN TOTAL) ---
        # Syarat wajib Dicoding cuma hapus "Unknown Product"
        df = df[df['title'].str.lower() != 'unknown product']
        
        # Hapus duplikat
        df = df.drop_duplicates()

        return df
    except Exception as e:
        print(f"Error fatal di transformasi: {e}")
        return pd.DataFrame()