# import library
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_car_dataset(input_path, output_path):
    """
    Fungsi untuk melakukan preprocessing dataset mobil.
    Langkah-langkah:
    1. Konversi 'horsepower' ke numerik dan isi missing values dengan median
    2. Standardisasi fitur numerik
    3. Hapus kolom 'car name'
    4. Simpan dataset hasil preprocessing ke file baru
    """

    # Load dataset
    df = pd.read_csv(input_path)

    # Konversi 'horsepower' ke numerik dan isi missing values dengan median
    df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
    df['horsepower'] = df['horsepower'].fillna(df['horsepower'].median())

    # Standardisasi fitur numerik
    numerical_cols = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin']
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Hapus kolom 'car name'
    if 'car name' in df.columns:
        df.drop('car name', axis=1, inplace=True)

    # Cek missing values
    print("\nMissing Values Setelah Preprocessing:")
    print(df.isnull().sum())

    # Simpan dataset hasil preprocessing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nDataset hasil preprocessing tersimpan di: {output_path}")

    return df


if __name__ == "__main__":
    input_file = "../auto-mpg.csv"
    output_file = "preprocessing/auto-mpg_preprocessed.csv"
    preprocess_car_dataset(input_file, output_file)
