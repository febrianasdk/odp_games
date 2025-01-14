def b():
    input_pengguna = input("Masukkan angka anda (Pisahkan dengan spasi): ").strip()

    if not input_pengguna:
        print("Input tidak boleh kosong!")
        return

    try:
        data_saya = list(map(int, input_pengguna.split()))
    except ValueError:
        print("Harap masukkan hanya angka yang valid!")
        return

    if len(data_saya) < 2:
        print("Masukkan setidaknya dua angka untuk mencari pasangan dengan selisih terkecil.")
        return

    data_saya.sort()

    minim = float('inf')
    terdekat = ()

    for i in range(len(data_saya) - 1):
        oke = data_saya[i + 1] - data_saya[i]
        if oke < minim:
            minim = oke
            terdekat = (data_saya[i], data_saya[i + 1])

    print(f"Angka dengan selisih terkecil adalah: {terdekat[0]} {terdekat[1]}")
    # """
    # Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    # MASUKAN
    # data = [4, 8, 15, 16, 23, 42]

    # KELUARAN
    # 15 16
    # """
