# Cost Training Model Calculator

## 🚀 Overview
Tool untuk menghitung biaya training model AI berbasis GPU.

## 💻 Cara Menggunakan
```bash
python main.py
```

Masukkan parameter ketika diminta:

- Jumlah GPU
- Biaya per GPU per jam
- Jam training per hari
- Jumlah hari training

## 📝 Contoh
```python
>>> cost_training_model(8, 2.50, 8, 7)
Total jam training: 56
Biaya training per GPU: 140.0
Total biaya training untuk 8 GPU: $1120.
```

## 🧮 Rumus Perhitungan
```python
Total Biaya = (num_gpu) × (cost_per_gpu_hour) × (hours_per_day) × (days_training)
```

# 🧪 Testing
```bash
python -m unittest test_unittest.py
```