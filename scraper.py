import requests
import pandas as pd
import time
import os
import json
from datetime import datetime

def fetch_semantic_scholar_filtered(query, total_results=1000, years_back=5, output_format="csv"):
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    # Validasi format output
    if output_format.lower() not in ["csv", "json", "both"]:
        raise ValueError("Format output harus 'csv', 'json', atau 'both'")
    
    # 1. Menghitung Rentang Tahun Dinamis
    current_year = datetime.now().year
    start_year = current_year - years_back
    year_range = f"{start_year}-{current_year}"
    
    print(f"--- Konfigurasi ---")
    print(f"Keyword      : {query}")
    print(f"Filter Tahun : {year_range} ({years_back} tahun terakhir)")
    print(f"Target Data  : {total_results}")
    print(f"Format Output: {output_format.upper()}")
    print(f"-------------------")

    # Field yang ingin diambil
    fields = "title,abstract,year,authors,venue,url,citationCount,externalIds,fieldsOfStudy"
    
    all_papers = []
    offset = 0
    limit = 100 
    
    while len(all_papers) < total_results:
        params = {
            "query": query,
            "limit": limit,
            "offset": offset,
            "fields": fields,
            "year": year_range  # <-- Parameter filter tahun ditambahkan di sini
        }
        
        try:
            response = requests.get(base_url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'data' not in data or not data['data']:
                    print("Tidak ada data tambahan ditemukan untuk kriteria ini.")
                    break
                
                papers = data['data']
                
                for paper in papers:
                    # Validasi ekstra: Kadang API memberikan data di perbatasan tahun
                    # Kita pastikan tahunnya tidak None
                    p_year = paper.get('year')
                    if p_year is None:
                        continue

                    author_names = ", ".join([a['name'] for a in paper.get('authors', [])])
                    
                    # Ambil DOI dari externalIds
                    external_ids = paper.get('externalIds', {})
                    doi = external_ids.get('DOI') if external_ids else None
                    
                    # Ambil keyword dari fieldsOfStudy
                    fields_of_study = paper.get('fieldsOfStudy', [])
                    keywords = ", ".join(fields_of_study) if fields_of_study else None
                    
                    paper_info = {
                        'Title': paper.get('title'),
                        'Year': int(p_year),
                        'Citations': paper.get('citationCount'),
                        'Authors': author_names,
                        'Venue': paper.get('venue'),
                        'URL': paper.get('url'),
                        'DOI': doi,
                        'Keywords': keywords,
                        'Abstract': paper.get('abstract')
                    }
                    all_papers.append(paper_info)
                
                print(f"Berhasil mengambil batch {offset} - {offset + len(papers)} (Total terkumpul: {len(all_papers)})")
                
                offset += limit
                
                if len(all_papers) >= total_results:
                    all_papers = all_papers[:total_results]
                    break
                
                time.sleep(1) 
                
            elif response.status_code == 429:
                print("Rate Limit tercapai. Menunggu 10 detik...")
                time.sleep(10)
            else:
                print(f"Error {response.status_code}: {response.text}")
                break
                
        except Exception as e:
            print(f"Terjadi kesalahan koneksi: {e}")
            break

    # Simpan ke file sesuai format yang dipilih
    if all_papers:
        # Buat folder output jika belum ada
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"📁 Folder '{output_folder}' berhasil dibuat.")
        
        # Fungsi untuk menyimpan ke CSV
        def save_to_csv():
            df = pd.DataFrame(all_papers)
            
            # Bersihkan format
            df['Abstract'] = df['Abstract'].astype(str).str.replace(r'\n', ' ', regex=True)
            
            # Urutkan berdasarkan tahun terbaru agar lebih rapi
            df = df.sort_values(by='Year', ascending=False)
            
            filename = f"dataset_terbaru_{query.replace(' ', '_')}.csv"
            filepath = os.path.join(output_folder, filename)
            df.to_csv(filepath, index=False)
            print(f"📄 CSV: {len(df)} jurnal tersimpan di '{filepath}'")
            return filepath
        
        # Fungsi untuk menyimpan ke JSON
        def save_to_json():
            # Urutkan berdasarkan tahun terbaru
            all_papers_sorted = sorted(all_papers, key=lambda x: x['Year'], reverse=True)
            
            # Bersihkan format abstract untuk JSON
            for paper in all_papers_sorted:
                if paper.get('Abstract'):
                    paper['Abstract'] = paper['Abstract'].replace('\n', ' ')
            
            filename = f"dataset_terbaru_{query.replace(' ', '_')}.json"
            filepath = os.path.join(output_folder, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    "metadata": {
                        "query": query,
                        "year_range": year_range,
                        "total_results": len(all_papers_sorted),
                        "generated_at": datetime.now().isoformat()
                    },
                    "papers": all_papers_sorted
                }, f, indent=2, ensure_ascii=False)
            
            print(f"📄 JSON: {len(all_papers_sorted)} jurnal tersimpan di '{filepath}'")
            return filepath
        
        # Eksekusi sesuai format yang dipilih
        saved_files = []
        
        if output_format.lower() == "csv":
            saved_files.append(save_to_csv())
            
        elif output_format.lower() == "json":
            saved_files.append(save_to_json())
            
        elif output_format.lower() == "both":
            print(f"\n📦 Menyimpan dalam 2 format...")
            saved_files.append(save_to_csv())
            saved_files.append(save_to_json())
        
        print(f"\n✅ Selesai! {len(all_papers)} jurnal dari tahun {year_range} berhasil disimpan.")
        if len(saved_files) > 1:
            print(f"📁 File tersimpan: {len(saved_files)} format berbeda")
    else:
        print("Gagal mendapatkan data atau tidak ada jurnal yang cocok.")

# --- EKSEKUSI ---
if __name__ == "__main__":
    # Ganti topik penelitian di sini
    topik = "computer science"
    
    # Pilih salah satu format output:
    
    # 1. Format CSV saja
    fetch_semantic_scholar_filtered(topik, total_results=50, years_back=5, output_format="csv")
    
    # 2. Format JSON saja
    # fetch_semantic_scholar_filtered(topik, total_results=50, years_back=5, output_format="json")
    
    # 3. Kedua format (CSV + JSON)
    # fetch_semantic_scholar_filtered(topik, total_results=50, years_back=5, output_format="both")