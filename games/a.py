def a():
    def angka_ke_teks(n):
        if not (0 <= n <= 999_999_999):
            return "Input harus di interval 0 sampai 999.999.999"

        angka = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
        belasan = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", 
                "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
        puluhan = ["", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", 
                "tujuh puluh", "delapan puluh", "sembilan puluh"]
        
        if n == 0: 
            return "nol"
        def konversi_tiga_digit(num):
            
            teks = ""
            ratusan, sisa = divmod(num, 100)
            puluh, satuan = divmod(sisa, 10)

            
            if ratusan:
                teks += "seratus " if ratusan == 1 else angka[ratusan] + " ratus "
            
            if puluh == 1:
                teks += belasan[satuan]
            
            else:
                if puluh:
                    teks += puluhan[puluh] + " "
                if satuan:
                    teks += angka[satuan]
            
            return teks.strip()
        
        juta, sisa = divmod(n, 1_000_000)
        ribu, satuan = divmod(sisa, 1_000)
        
        teks_hasil = ""
        if juta:
            teks_hasil += konversi_tiga_digit(juta) + " juta "
        if ribu:
            if ribu == 1:
                teks_hasil += "seribu "
            else:
                teks_hasil += konversi_tiga_digit(ribu) + " ribu "
        if satuan:
            teks_hasil += konversi_tiga_digit(satuan)
        
        return teks_hasil.strip()

    n = int(input("Masukkan Angka: "))
    print(angka_ke_teks(n)) 