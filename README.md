# Semantic Scholar Journal Scraper 📚

Aplikasi Python sederhana untuk mengunduh dataset jurnal penelitian dari **Semantic Scholar API**. Aplikasi ini dirancang untuk mengambil metadata jurnal (Judul, Penulis, Abstrak, Tahun, dll) dengan filter otomatis **5 tahun terakhir**.

## 📋 Prasyarat

Pastikan komputer Anda sudah terinstal:
- **Python 3.x** (Cek dengan mengetik `python --version` di terminal/CMD)
- Koneksi Internet

---

## 🛠️ Langkah 1: Menyiapkan Virtual Environment (Instalasi)

Kita menggunakan `venv` agar library yang diinstal tidak tercampur dengan sistem global komputer Anda.

### 1. Buat dan Masuk ke Folder Proyek
Buka Terminal (macOS/Linux) atau Command Prompt/PowerShell (Windows):

```bash
mkdir riset_jurnal
cd riset_jurnal
````

### 2\. Buat Virtual Environment

Jalankan perintah berikut untuk membuat folder lingkungan isolasi bernama `venv`:

**Windows:**

```bash
python -m venv venv
```

**macOS / Linux:**

```bash
python3 -m venv venv
```

### 3\. Aktifkan Virtual Environment

Setelah diaktifkan, terminal Anda akan menampilkan tanda `(venv)` di sebelah kiri.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4\. Install Library

Install library yang dibutuhkan hanya di dalam lingkungan ini:

```bash
pip install requests pandas
```

-----

## 🚀 Langkah 3: Menjalankan Program

Setelah lingkungan siap dan file script (`scraper.py`) sudah dibuat, ikuti langkah ini untuk memulai scraping.

### 1\. Konfigurasi Topik Penelitian

Buka file `scraper.py` menggunakan Text Editor (Notepad, VS Code, dll). Cari bagian paling bawah pada blok `__main__` dan ubah variabel `topik`:

```python
if __name__ == "__main__":
    # Ganti topik penelitian di sini
    topik = "machine learning optimization"  <-- GANTI INI
    
    # Jalankan
    fetch_semantic_scholar_filtered(topik, total_results=1000, years_back=5)
```

### 2\. Jalankan Script

Pastikan terminal masih menampilkan status `(venv)`, lalu ketik:

```bash
python scraper.py
```

### 3\. Hasil Output

Program akan berjalan dan menampilkan progres per 100 data. Setelah selesai, file CSV akan muncul di folder proyek dengan format nama:
`dataset_terbaru_machine_learning_optimization.csv`

-----

## 🛑 Cara Keluar dari Virtual Environment

Jika sudah selesai menggunakan program, Anda bisa menonaktifkan mode virtual environment dengan perintah:

```bash
deactivate
```

-----

*Dibuat untuk keperluan penyusunan dataset penelitian.*

```
```