# Input dari pengguna

# Data rute dan harga langsung di dalam kode Python
routes = {
    1: {"destination": "Malang - Surabaya", "price": 35000},
    2: {"destination": "Malang - Pasuruan", "price": 20000},
    3: {"destination": "Malang - Jombang",  "price": 25000}
}

print("=== TIKET BUS ===")
for k, v in routes.items():
    print(f"Tekan {k} : {v['destination']} (Rp {v['price']:,})")

# Input rute dari pengguna
try:
    pilihan = int(input("Pilih rute (1-3): "))
    # Input jumlah penumpang dari pengguna
    jumlah = int(input("Masukkan jumlah penumpang: "))
except ValueError:
    print("Error: Input harus berupa angka!")
    exit()

# Hitung dan tampilkan hasil
if pilihan in routes and jumlah > 0:
    rute = routes[pilihan]
    total = rute["price"] * jumlah
    
    print("\n=== RINCIAN PEMESANAN TIKET ===")
    print(f"Rute Perjalanan  : {rute['destination']}")
    print(f"Harga per Tiket  : Rp {rute['price']:,}")
    print(f"Jumlah Penumpang : {jumlah} orang")
    print(f"TOTAL BAYAR      : Rp {total:,}")
else:
    print("Input tidak valid!")
