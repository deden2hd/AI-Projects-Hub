def hitung_total_token(api_calls_per_hari, token_per_call,  hari_dalam_bulan):
    '''
    Fungsi untuk menghitung jumlah token yang dipanggil dalam 1 bulan

    api_calls_per_hari (int) : Jumlah API yang dipanggil dalam sehari
    token_per_call (int): Jumlah token pada setiap API dipanggil
    hari_dalam_bulan (int): Jumlah hari layanan API dijalankan dalam sebulan

    example:
    >>> hitung_total_token(5000, 150, 30)
    22500000
    '''
    # Perhitungan total token yang berjalan dalam 1 bulan
    total_token = api_calls_per_hari * token_per_call * hari_dalam_bulan
    return total_token

def hitung_biaya_api(total_token, biaya_per_token):
    '''
    Fungsi untuk menghitung biaya dari total token dalam 1 bulan

    total_token (int) : Jumlah total token yang dijalankan dalam 1 bulan
    biaya_per_token: biaya per token dipanggil

    example:
    >>> hitung_biaya_api(2, 2)
    4

    '''
    total_biaya = total_token * biaya_per_token
    return total_biaya

def rata_token_per_call(total_token, api_calls_per_hari, hari_dalam_bulan):
    '''
    Fungsi untuk menghitung rata rata token yang dipanggil dalam 1 bulan

    total_token (int):
    api_calls_per_hari (int):
    hari_dalam_bulan (init):

    >>> rata_token_per_call(10, 2, 5)
    1.0
    '''
    total_api = api_calls_per_hari * hari_dalam_bulan
    return total_token / total_api
if __name__ == '__main__':
    print(" === Selamat datang di program menghitung kalkulator biaya ====")

    api_calls = int(input("Jumlah API yang dipanggil dalam sehari: "))
    token = int(input("Jumlah token per API: "))
    biaya = float(input("Jumlah biaya dalam per token: "))
    hari = int(input("Jumlah hari: "))

    total_token = hitung_total_token(api_calls, token, hari)
    total_biaya = hitung_biaya_api(total_token, biaya)
    rata_token = rata_token_per_call(total_token, api_calls, hari)

    print(f"Total token per bulan: {total_token}")
    print(f"Total biaya API per bulan: ${total_biaya}")
    print(f"Rata-rata token per API call: {rata_token}")
