**ETL Pipeline: Retail Competitor Research 🚀
Proyek ini adalah sebuah ETL (Extract, Transform, Load) Pipeline sederhana yang dirancang untuk mengotomatisasi pengambilan data produk dari website kompetitor (Fashion Studio). Proyek ini dibangun sebagai bagian dari tugas Data Engineering untuk mensimulasikan riset pasar di bidang fashion.**

**🛠️ Tech Stack**

Language: Python 3.12

Libraries: * Requests & BeautifulSoup4 (Extraction/Scraping)

Pandas (Transformation/Data Cleaning)

Pytest & Pytest-cov (Unit Testing & Coverage)



**⚙️ Alur Kerja ETL**


1. Extract

Mengambil data mentah dari 50 halaman website kompetitor (total 1000 baris data). Data yang diambil meliputi:

Nama Produk (Title)

Harga (Price) dalam USD

Rating, Warna, Ukuran, dan Gender.

Timestamp pengambilan data.

2. Transform
   
Proses pembersihan data menggunakan Pandas:

Konversi Mata Uang: Mengubah harga dari USD ke IDR (Kurs Rp16.000).

Pembersihan String: Menghapus prefix seperti "Size: " atau "Gender: ".

Filtering: Menghapus data "Unknown Product" atau data dengan rating/harga tidak valid.

Deduplikasi: Memastikan tidak ada data ganda dalam laporan akhir.

3. Load
4. 
Menyimpan data yang telah dibersihkan ke dalam format file products.csv agar siap digunakan oleh tim Data Science.

**🚀 Cara Menjalankan**

Clone repositori ini.

Install dependensi:

Bash
pip install -r requirements.txt
Jalankan pipeline:

Bash
python main.py
Untuk menjalankan unit test:

Bash
pytest --cov=utils tests/

**📊 Hasil Akhir**

Setelah pipeline dijalankan, file products.csv akan berisi data kompetitor yang bersih, terstandarisasi, dan siap dianalisis untuk menentukan strategi harga dan model baju baru.
