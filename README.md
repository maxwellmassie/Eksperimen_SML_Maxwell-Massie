
# Eksperimen MSML – Maxwell Massie

Repository ini dibuat untuk memenuhi Kriteria 1: Eksperimen terhadap Dataset Pelatihan pada kelas Membangun Sistem Machine Learning.
Tahapan eksperimen dilakukan berdasarkan Template Eksperimen MSML, kemudian dikonversi menjadi script otomatisasi preprocessing dan diintegrasikan dengan workflow GitHub Actions (tingkat Advanced).

Dataset yang digunakan adalah Auto MPG dari UCI Machine Learning Repository, yang berisi data spesifikasi kendaraan dan target miles per gallon (mpg).

## Tujuan Proyek

1. Melakukan eksplorasi dan preprocessing dataset secara manual melalui notebook.

2. Mengubah proses manual tersebut menjadi pipeline otomatis menggunakan Python.

3. Menjalankan preprocessing otomatis melalui GitHub Actions dan menghasilkan dataset akhir sebagai artefak.

## 📌 Alasan Pemilihan Dataset

Dataset Auto MPG dipilih karena:

1. Ukuran kecil (398 baris) → sangat ideal untuk CI/CD, cepat dalam build & run.

2. Memungkinkan Ukuran Artefak model atau preprocessing kecil → mudah dipush dan disimpan GitHub Actions.

3. Fitur semua numerik kecuali satu kolom → preprocessing sederhana dan sesuai dengan fokus MSML (bukan data engineering berat).

4. Stabil & umum digunakan → cocok untuk latihan eksperimen dan otomasi MLOps.

Karena Submisison ini fokus pada pemahaman Membangun sistem amchine learning, maka Dataset ini membantu fokus pada workflow MLOps, bukan pada beban komputasi dataset besar.


## 📂 Struktur Repository (Final – Kriteria 1 Advanced)
```
Eksperimen_SML_Maxwell_Massie
├── .github/workflows
│   └── main.yml                  # Workflow CI (Advanced)
├── auto-mpg.csv                  # Dataset raw
├── preprocessing
│   ├── Eksperimen_Maxwell_Massie.ipynb   # Eksperimen manual sesuai template MSML
│   └── automate_maxwell-massie.py        # Script otomatisasi preprocessing
│   └── auto-mpg_preprocessed.csv     # Artefak preprocessing (dari CI)
```


## ⚙️ Preprocessing Otomatis (automate_maxwell-massie.py)

Script otomatis ini melakukan langkah-langkah:
```
1. Konversi horsepower ke numerik

2. Isi missing values dengan median

3. Standardisasi fitur numerik menggunakan StandardScaler

4. Menghapus kolom car name

5. Menyimpan hasil preprocessing ke folder preprocessing/
```

## 🚀 Workflow CI/CD (Advanced)

Workflow di .github/workflows/main.yml melakukan hal berikut:
```
1. Checkout repository

2. Menginstall dependensi

3. Menjalankan automate_maxwell-massie.py

4. Menghasilkan auto-mpg_preprocessed.csv

5. Meng-upload/push dataset tersebut sebagai artifact CI
```

---
Maxwell Massie
