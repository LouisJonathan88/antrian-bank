import os
import pygame

# Function Heap
class Heap:
    def __init__(self):
        self.heap = []
        
    def tambah(self, kode):
        self.heap.append(kode)
        self.saring_up(len(self.heap) - 1)
        
    def ambil(self):
        if not self.heap:
            return None
        antrian = self.heap[0]
        last_elem = self.heap.pop()
        if self.heap:
            self.heap[0] = last_elem
            self.saringbawah(0)
        return antrian

    def saring_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] > self.heap[idx]:
                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break

    def saringbawah(self, idx):
        while idx < len(self.heap):
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            min_idx = idx
            
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
                min_idx = left_child_idx
                
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
                min_idx = right_child_idx
                
            if min_idx != idx:
                self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
                idx = min_idx
            else:
                break
            
# Function Antrian
class AntrianApp:

    def __init__(self):
        self.antrian_next = Heap()
        self.antrian_meja1 = []
        self.antrian_meja2 = []
        self.personal_counter = 1
        self.bisnis_counter = 1
    
     # Inisialisasi pygame mixer untuk memainkan suara

        pygame.mixer.init()

        self.sound_antrian_nomor = pygame.mixer.Sound(r"Sound en\\for queue number.wav")
        self.sound_antrian_nomor_idn = pygame.mixer.Sound(r"Sound idn\\untuk nomor antrian.wav")

        self.sound_P = pygame.mixer.Sound(r"Sound en\\p.wav")
        self.sound_P_idn = pygame.mixer.Sound(r"Sound idn\\p.wav")

        self.sound_B = pygame.mixer.Sound(r"Sound en\\b.wav")
        self.sound_B_idn = pygame.mixer.Sound(r"Sound idn\\b.wav")

        self.sound_ke_loket = pygame.mixer.Sound(r"Sound en\\counter.wav")
        self.sound_ke_loket_idn = pygame.mixer.Sound(r"Sound idn\\loket.wav")
        
        self.sound_loket_1 = pygame.mixer.Sound(r"Sound en\\1.wav")
        self.sound_loket_1_idn = pygame.mixer.Sound(r"Sound idn\\1.wav")
        
        self.sound_loket_2 = pygame.mixer.Sound(r"Sound en\\2.wav")
        self.sound_loket_2_idn = pygame.mixer.Sound(r"Sound idn\\2.wav")

    def putar_instruksi_bahasa_no3(self, kode_bahasa):
        if kode_bahasa == "en":
            antrian_app.ambil_antrian_meja1()
        elif kode_bahasa == "id":
            antrian_app.ambil_antrian_meja1_idn()
        else:
            print("Bahasa tidak valid")
        return
    
    def putar_instruksi_bahasa_no4(self, kode_bahasa):
        if kode_bahasa == "en":
            antrian_app.ambil_antrian_meja2()
        elif kode_bahasa == "id":
            antrian_app.ambil_antrian_meja2_idn()
        else:
            print("Bahasa tidak valid")
        return
    
        
    def tambah_antrian_personal(self):
        kode_antrian = f"P{self.personal_counter:03}"
        self.antrian_next.tambah(kode_antrian)
        self.personal_counter += 1

    def tambah_antrian_bisnis(self):
        kode_antrian = f"B{self.bisnis_counter:03}"
        self.antrian_next.tambah(kode_antrian)
        self.bisnis_counter += 1

    def ambil_antrian_meja1(self):
        antrian = self.antrian_next.ambil()
        if antrian:
            self.antrian_meja1 = [antrian]
            print("\nNomor Antrian", antrian, "ke Meja 1.")
            self.play_sound(antrian,1)
        else:
            print("Meja 1 kosong.")
        self.tampilkan_antrian()
        
    def ambil_antrian_meja1_idn(self):
        antrian = self.antrian_next.ambil()
        if antrian:
            self.antrian_meja1 = [antrian]
            print("\nNomor Antrian", antrian, "ke Meja 1.")
            self.play_sound_idn(antrian,1)
        else:
            print("Meja 1 kosong.")
        self.tampilkan_antrian()

    def ambil_antrian_meja2(self):
        antrian = self.antrian_next.ambil()
        if antrian:
            self.antrian_meja2 = [antrian]
            print("\nNomor Antrian", antrian, "ke Meja 2.")
            self.play_sound(antrian,2)
        else:
            print("Meja 2 kosong.")
        self.tampilkan_antrian()
        
    def ambil_antrian_meja2_idn(self):
        antrian = self.antrian_next.ambil()
        if antrian:
            self.antrian_meja2 = [antrian]
            print("\nNomor Antrian", antrian, "ke Meja 2.")
            self.play_sound_idn(antrian,2)
        else:
            print("Meja 2 kosong.")
        self.tampilkan_antrian()

    def tampilkan_antrian(self):
        print("===========================================")
        print("Meja 1 : " + ", ".join(self.antrian_meja1))
        print("Meja 2 : " + ", ".join(self.antrian_meja2))
        print("Nomor Selanjutnya \t: " + (self.antrian_next.heap[0] if self.antrian_next.heap else "Kosong"))
        print("==============================================\n")

    def play_sound(self, antrian, loket):
        # Memainkan suara dengan pesan yang sesuai
        if "P" in antrian:
            jenis_antrian = "P"
        elif "B" in antrian:
            jenis_antrian = "B"
        else:
            jenis_antrian = "T"
            
        nomor_antrian = antrian[1:]
        pesan_suara = f"{jenis_antrian}{nomor_antrian} {loket}"
        
        for char in pesan_suara:
            if  char == "P":
                self.sound_antrian_nomor.play()
                pygame.time.wait(2000)
                self.sound_P.play()
                pygame.time.wait(800)
            elif  char == "B":
                self.sound_antrian_nomor.play()
                pygame.time.wait(2000)
                self.sound_B.play()
                pygame.time.wait(800)
            elif char == " ":
                self.sound_ke_loket.play()
                pygame.time.wait(1500)
            elif char.isdigit:
                self.play_digit(char)
                pygame.time.wait(1000)
            elif loket == 1:
                pygame.time.wait(500)
                self.sound_loket_1.play()
            elif loket == 2:
                pygame.time.wait(500)
                self.sound_loket_2.play()
                pygame.time.wait(500)
            else:
                pass
            
    def play_sound_idn(self, antrian, loket):
        # Memainkan suara dengan pesan yang sesuai
        if "P" in antrian:
            jenis_antrian = "P"
        elif "B" in antrian:
            jenis_antrian = "B"
        else:
            jenis_antrian = "T"
            
        nomor_antrian = antrian[1:]
        pesan_suara = f"{jenis_antrian}{nomor_antrian} {loket}"

        for char in pesan_suara:
            if  char == "P":
                self.sound_antrian_nomor_idn.play()
                pygame.time.wait(2000)
                self.sound_P_idn.play()
                pygame.time.wait(800)
            elif  char == "B":
                self.sound_antrian_nomor_idn.play()
                pygame.time.wait(2000)
                self.sound_B_idn.play()
                pygame.time.wait(800)
            elif char == " ":
                self.sound_ke_loket_idn.play()
                pygame.time.wait(2300)
            elif char.isdigit:
                self.play_digit_idn(char)
                pygame.time.wait(1000)
            elif loket == 1:
                pygame.time.wait(500)
                self.sound_loket_1_idn.play()
            elif loket == 2:
                pygame.time.wait(500)
                self.sound_loket_2_idn.play()
                pygame.time.wait(500)
            else:
                pass

    def play_digit(self, digit):
        digits_sound = {
            "0": pygame.mixer.Sound(r'Sound en\\0.wav'),
            "1": pygame.mixer.Sound(r'Sound en\\1.wav'),
            "2": pygame.mixer.Sound(r'Sound en\\2.wav'),
            "3": pygame.mixer.Sound(r'Sound en\\3.wav'),
            "4": pygame.mixer.Sound(r'Sound en\\4.wav'),
            "5": pygame.mixer.Sound(r'Sound en\\5.wav'),
            "6": pygame.mixer.Sound(r'Sound en\\6.wav'),
            "7": pygame.mixer.Sound(r'Sound en\\7.wav'),
            "8": pygame.mixer.Sound(r'Sound en\\8.wav'),
            "9": pygame.mixer.Sound(r'Sound en\\9.wav'),
        }

        if digit in digits_sound:
            digits_sound[digit].play()
            
    def play_digit_idn(self, digit):
        digits_sound = {
            "0": pygame.mixer.Sound(r'Sound idn\\0.wav'),
            "1": pygame.mixer.Sound(r'Sound idn\\1.wav'),
            "2": pygame.mixer.Sound(r'Sound idn\\2.wav'),
            "3": pygame.mixer.Sound(r'Sound idn\\3.wav'),
            "4": pygame.mixer.Sound(r'Sound idn\\4.wav'),
            "5": pygame.mixer.Sound(r'Sound idn\\5.wav'),
            "6": pygame.mixer.Sound(r'Sound idn\\6.wav'),
            "7": pygame.mixer.Sound(r'Sound idn\\7.wav'),
            "8": pygame.mixer.Sound(r'Sound idn\\8.wav'),
            "9": pygame.mixer.Sound(r'Sound idn\\9.wav'),
        }

        if digit in digits_sound:
            digits_sound[digit].play()
        
        
        
# Tampilan Menu
if __name__ == "__main__":
    antrian_app = AntrianApp()
    
    os.system("cls")
    while True:
        print("\n\t===== Aplikasi Antrian =====")
        antrian_app.tampilkan_antrian()
        print("1. Tambah Antrian Bisnis")
        print("2. Tambah Antrian Personal")
        print("3. Meja 1 memanggil")
        print("4. Meja 2 memanggil")
        print("5. Keluar\n")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            antrian_app.tambah_antrian_bisnis()
        elif pilihan == "2":
            antrian_app.tambah_antrian_personal()
        elif pilihan == "3":
            print("\nPilih Bahasa:")
            print("1. Inggris")
            print("2. Indonesia")
            
            pilihan_bahasa = input("\nPilih bahasa: ")
            if pilihan_bahasa == "1":
                antrian_app.putar_instruksi_bahasa_no3("en")
            elif pilihan_bahasa == "2":
                antrian_app.putar_instruksi_bahasa_no3("id")
            
        elif pilihan == "4":
            print("\nPilih Bahasa:")
            print("1. Inggris")
            print("2. Indonesia")
            
            pilihan_bahasa = input("\nPilih bahasa: ")
            if pilihan_bahasa == "1":
                antrian_app.putar_instruksi_bahasa_no4("en")
            elif pilihan_bahasa == "2":
                antrian_app.putar_instruksi_bahasa_no4("id")
              
        elif pilihan == "5":
            os.system("cls")
            print("-----Terima Kasih-----")
            break
        else:
            print("Pilihan tidak valid.")
