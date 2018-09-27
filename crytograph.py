from Tkinter import *
import tkMessageBox as mb
import ttk
import pyperclip

 
# MUHAMMAD LUQNI BAEHAQI
 
class crypto:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
  
        self.induk.resizable(True, True)
         
        self.aturKomponen()
         
        self.entUser.focus_set()

	self.membuatMenu()

	self.sandiCaesar()
         
    def aturKomponen(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
         
        # atur input username
        Label(frData, text=':: Sandi Balik ::').grid(row=0, column=1, sticky=W)
        Label(frData, text='Masukkan Teks : ').grid(row=2, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=2, column=1)
         
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
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData2 = Frame(frameUtama, bd=5)
        frData2.pack(fill=BOTH, expand=YES)
         
        # atur input username
        Label(frData2, text=':: Sandi Caesar ::').grid(row=0, column=1, sticky=W)
        Label(frData2, text='Masukan Teks : ').grid(row=1, column=0, sticky=W)
        self.Caesar = Entry(frData2)
        self.Caesar.grid(row=1, column=1)
        # memasukan kunci
        Label(frData2, text='Masukan Kunci : ').grid(row=2, column=0, sticky=W)
        self.Caesar2 = Entry(frData2)
        self.Caesar2.grid(row=2, column=1)
         
        # menampilkan hasil
        Label(frData2, text='Hasil :').grid(row=3, column=0)
	
        self.hasil2 = Entry(frData2)
        self.hasil2.grid(row=3, column=1)
         
        # atur frame tombol
        frTombol2 = Frame(frameUtama, bd=5)
        frTombol2.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btn = Button(frTombol2, text='Proses', command=self.caesar)
        self.btn.pack(side=LEFT, fill=BOTH, expand=YES)
         
    def prosesBalik(self, event=None):
        # ambil data input dari pengguna
        pesan = self.entUser.get()
	ubah = ''
	i = len(pesan)-1
	while i >= 0:
		ubah = ubah + pesan[i]
		i = i-1
	self.hasil.insert(0,ubah)
    def caesar(self):
	pesan2 = self.Caesar.get()
	kunci = eval(self.Caesar2.get())
	huruf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ubah2 = ''
	pesan2 = pesan2.upper()
	for symbol in pesan2:
		if symbol in huruf:
			nomor = huruf.find(symbol)
			nomor = nomor+kunci
			if nomor >= len(huruf):
				nomor = nomor - len(huruf)
			elif nomor < 0:
				nomor = nomor + len(huruf)
			ubah2 = ubah2 + huruf[nomor]
		else:
			ubah2 = ubah2 + symbol
	self.hasil2.insert(0, ubah2)
    def membuatMenu(self):
	menubar = Menu(self.induk)
	self.induk.config(menu=menubar)

    def membuatMenu(self):
	menubar = Menu(self.induk)
	self.induk.config(menu=menubar)

	fileMenu = Menu(menubar)
	fileMenu.add_command(label="Nama Kelompok",command='')
	fileMenu.add_command(label="Exit",command=self.perintahKeluar)
	menubar.add_cascade(label="File",menu=fileMenu)
    def perintahKeluar(self):
	self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
    app = crypto(root, ":: Demo Keamanan Sistem Informasi *Luqni*::")
     
    root.mainloop()
