from Tkinter import *


 
# MUHAMMAD LUQNI BAEHAQI
 
class crypto:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
  
        self.induk.resizable(True, True)
         
        self.sandiBalik()
         
        # self.entUser.focus_set()

	self.membuatMenu()

	self.sandiCaesar()

	# self.decryptCaesar()
         
    def sandiBalik(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
         
        # atur input username
        Label(frData, text=':: Sandi Balik ::').grid(row=0, column=1, sticky=W)
        Label(frData, text='Masukkan Teks : ').grid(row=2, column=0, sticky=W)
        self.balik = Entry(frData)
        self.balik.grid(row=2, column=1)
         
        # menampilkan hasil
        Label(frData, text='Hasil : ').grid(row=3, column=0)
	
        self.hasil = Entry(frData)
        self.hasil.grid(row=3, column=1)
         
        # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btnLogin = Button(frTombol, text='Proses', command=self.prosesBalik)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)
    
    def sandiCaesar(self):
    	var = IntVar()
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData2 = Frame(frameUtama, bd=5)
        frData2.pack(fill=BOTH, expand=YES)
         
        # atur input username
        Label(frData2, text=':: Sandi Caesar ::').grid(row=0, column=1, sticky=W)

        # Radiobutton(frData2, text="encrypt", variable=var, value=1).grid(row=1, column=1, sticky=W)
        # self.var = Entry(frData2)
        # Radiobutton(frData2, text="decrypt", variable=var, value=2).grid(row=2, column=1, sticky=W)
        Label(frData2, text='encrypt/decrypt : ').grid(row=2, column=0, sticky=W)
        self.var = Entry(frData2)
        self.var.grid(row=2, column=1)
        
        Label(frData2, text='Masukan Teks : ').grid(row=3, column=0, sticky=W)
        self.Caesar = Entry(frData2)
        self.Caesar.grid(row=3, column=1)
        # memasukan kunci
        Label(frData2, text='Masukan Kunci : ').grid(row=4, column=0, sticky=W)
        self.Caesar2 = Entry(frData2)
        self.Caesar2.grid(row=4, column=1)
         
        # menampilkan hasil
        Label(frData2, text='Hasil :').grid(row=5, column=0)
	
        self.hasil2 = Entry(frData2)
        self.hasil2.grid(row=5, column=1)
         
        # atur frame tombol
        frTombol2 = Frame(frameUtama, bd=5)
        frTombol2.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btn = Button(frTombol2, text='Proses', command=self.caesar)
        self.btn.pack(side=LEFT, fill=BOTH, expand=YES)
         
    def prosesBalik(self, event=None):
        # ambil data input dari pengguna
        pesan = self.balik.get()
	ubah = ''
	i = len(pesan)-1
	while i >= 0:
		ubah = ubah + pesan[i]
		i = i-1
	self.hasil.insert(0,ubah)
    def caesar(self):
	pesan2 = self.Caesar.get()
	kunci = eval(self.Caesar2.get())
	mode = str(self.var.get())
	huruf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ubah2 = ''
	pesan2 = pesan2.upper()
	for symbol in pesan2:
		if symbol in huruf:
			nomor = huruf.find(symbol)
			if mode == 'encrypt':
				nomor = nomor+kunci
			elif mode == 'decrypt':
				nomor = nomor - kunci
			if nomor >= len(huruf):
				nomor = nomor - len(huruf)
			elif nomor < 0:
				nomor = nomor + len(huruf)
			ubah2 = ubah2 + huruf[nomor]
		else:
			ubah2 = ubah2 + symbol
	self.hasil2.insert(0, ubah2)

	# def DecryptCaesar(self):
	# 	pesan3 = self.DecryptCaesar.get()
	
	# 	kunci2 = eval(self.DecryptCaesar2.get())
	# 	huruf2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# 	ubah3 = ''
	# 	pesan3 = pesan3.upper()
	# 	for symbol in pesan3:
	# 		if symbol in huruf2:
	# 			nomor2 = huruf2.find(symbol)
	# 			nomor2 = nomor2-kunci2
	# 			if nomor2 >= len(huruf2):
	# 				nomor2 = nomor2 - len(huruf2)
	# 			elif nomor2 < 0:
	# 				nomor2 = nomor2 + len(huruf2)
	# 			ubah3 = ubah3 + huruf2[nomor2]
	# 		else:
	# 			ubah3 = ubah3 + symbol
	# 	self.hasil3.insert(0, ubah3)




    def membuatMenu(self):
	menubar = Menu(self.induk)
	self.induk.config(menu=menubar)

    def membuatMenu(self):
	menubar = Menu(self.induk)
	self.induk.config(menu=menubar)

	fileMenu = Menu(menubar)
	fileMenu.add_command(label="Alfa paizun",command='')
	fileMenu.add_command(label="Hasna M",command='')
	fileMenu.add_command(label="Luqni B",command='')
	fileMenu.add_command(label="Tika A",command='')
	fileMenu.add_command(label="Exit",command=self.perintahKeluar)
	menubar.add_cascade(label="Nama Kelompok",menu=fileMenu)
    def perintahKeluar(self):
	self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
    app = crypto(root, ":: Demo Keamanan Sistem Informasi *Luqni*::")
     
    root.mainloop()
