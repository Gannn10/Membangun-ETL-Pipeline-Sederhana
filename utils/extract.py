import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        # BERDASARKAN GAMBAR: Bungkusan produk adalah class 'collection-card'
        items = soup.find_all('div', class_='collection-card') 

        for item in items:
            # Mengambil data dari dalam collection-card
            # Sesuaikan tag (h3/h5/p) berdasarkan isi kartu di gambar
            title = item.find('h3').get_text(strip=True) if item.find('h3') else "Unknown Product"
            price = item.find('p', class_='price').get_text(strip=True) if item.find('p', class_='price') else "$0"
            
            # Rating, Colors, Size, Gender biasanya berupa list <p> di bawah harga
            details = item.find_all('p')
            
            data = {
                'title': title,
                'price': price,
                'rating': "0", 
                'colors': "0",
                'size': "Unknown",
                'gender': "Unknown",
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            for p in details:
                txt = p.get_text(strip=True)
                if 'Rating:' in txt: data['rating'] = txt.replace('Rating:', '').strip()
                elif 'Colors' in txt: data['colors'] = txt
                elif 'Size:' in txt: data['size'] = txt
                elif 'Gender:' in txt: data['gender'] = txt

            products.append(data)
            
        return products
    except Exception as e:
        print(f"Error scraping: {e}")
        return []