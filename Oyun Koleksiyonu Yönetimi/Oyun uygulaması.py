

from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from tkinter import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_msgbox(hata_kodu,mesaj_text,icon,pencere):
    mesaj = tk.Toplevel(pencere)

    mesaj.title(hata_kodu)
    mesaj.geometry("300x100")

    l1 = tk.Label(mesaj, image="::tk::icons::"+icon)
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(mesaj, text=mesaj_text)
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(mesaj, text="Tamam", command=mesaj.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")


    mesaj.update_idletasks()
    x = pencere.winfo_rootx() + (pencere.winfo_width() - mesaj.winfo_width()) // 2
    y = pencere.winfo_rooty() + (pencere.winfo_height() - mesaj.winfo_height()) // 2
    mesaj.geometry(f"300x100+{x}+{y}")


window = Tk()

window.geometry("500x500")
window.configure(bg="#A0B2B0")
window.title("Zteam")





class Uygulama():
    def __init__(self):
        self.giris_paneli()

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_oyun"
    )

    def veritabani(self):

        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_oyun"
            )


##################################  GİRİŞ PENCERESİ VE FONKSİYONLARI  #####################################
    def giris_paneli(self):

        self.canvas = Canvas(
            window,
            bg="#A0B2B0",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            250.0,
            250.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            33.0,
            19.0,
            anchor="nw",
            text="                GAMER ZONE",
            fill="#ECE4E4",
            font=("JetBrainsMonoRoman ExtraBold", 30 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            130.0,
            135.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            130.0,
            207.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            show="*",
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )

        self.text2=self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )

        self.text1=self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )


        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.hesap_olustur = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.hide,
            relief="flat"
        )
        self.hesap_olustur.place(
            x=144.0,
            y=467.0,
            width=213.0,
            height=22.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.musteri_giris ,
            relief="flat"
        )
        self.button_2.place(
            x=33.0,
            y=250.0,
            width=47.643829345703125,
            height=34.0,

        )


        window.resizable(False, False)
        window.mainloop()

    def hide(self):
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.hesap_olustur.destroy()
        self.button_2.destroy()
        self.canvas.delete(self.entry_bg_1)
        self.canvas.delete(self.entry_bg_2)
        self.canvas.delete(self.text1)
        self.canvas.delete(self.text2)

        self.email_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.email_bg = self.canvas.create_image(
            130.0,
            135.5,
            image=self.email_resim
        )
        self.email = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )



        self.numara_resim = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.numara_bg = self.canvas.create_image(
            130.0,
            207.5,
            image=self.numara_resim
        )
        self.numara = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.numara.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )


        self.sifre_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.sifre_bg = self.canvas.create_image(
            130.0,
            276.5,
            image=self.sifre_resim
        )
        self.sifre = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sifre.place(
            x=49.0,
            y=261.0,
            width=162.0,
            height=35.0
        )
        self.email_text = self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.numara_text = self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Telefon numarası:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.sifre_text = self.canvas.create_text(
            33.0,
            237.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.kayit_buton = PhotoImage(
            file=relative_to_assets("kayitbuton.png"))
        self.kayit = Button(
            image=self.kayit_buton,
            borderwidth=0,
            highlightthickness=0,
            command=self.kayit_ol,
            relief="flat"
        )
        self.kayit.place(
            x=33.0,
            y=330.0,
            width=77.643829345703125,
            height=34.0,

        )
        self.gerigel_resim = PhotoImage(
            file=relative_to_assets("gerigel.png"))
        self.gerigel = Button(
            image=self.gerigel_resim,
            borderwidth=0,
            highlightthickness=0,
            command=self.giris_paneli,
            relief="flat"
        )
        self.gerigel.place(
            x=200.0,
            y=467.0,
            width=120.0,
            height=20.0,

        )

    def kayit_ol(self):
        self.veritabani()
        self.email_giris = self.email.get()
        self.numara_giris = self.numara.get()
        self.sifre_giris = self.sifre.get()
        self.mycursor = self.mydb.cursor()
        ################################################
        self.mycursor.execute(self.sql_kayit_kontrol)
        self.myresult = self.mycursor.fetchone()
        self.sql_kayit_kontrol = "Select id FROM kullanicilar where kullanici_adi = %s"
        self.sql_kayit = "INSERT INTO kullanicilar (kullanici_adi, sifre, numara) VALUES (%s, %s, %s)"

        if not self.email_giris.strip() or not self.numara_giris.strip() or not self.sifre_giris.strip():
            login_msgbox("HATA!", "Boşluk bırakma!", "warning",window)
        else:
            self.mycursor.execute(self.sql_kayit_kontrol, (self.email_giris,))
            self.myresult = self.mycursor.fetchone()

            if self.myresult:  # DEĞER DÖNDÜRÜYORSA
                login_msgbox("HATA!", "Kullanıcı adı zaten mevcut!", "warning",window)
            else:
                try:
                    self.mycursor.execute(self.sql_kayit, (self.email_giris, self.sifre_giris, self.numara_giris))
                    self.mydb.commit()
                    print("Kayıt Başarılı")
                    login_msgbox("Tebrikler!", "Tebrikler! Kayıt başarılı.", "information",window)
                except mysql.connector.Error as err:
                    print(err)
                    login_msgbox("Hata!", "Server hatası!", "error",window)

    def musteri_giris(self):
            self.veritabani()
            self.true_kullanici_adi = self.entry_1.get()
            self.true_sifre = self.entry_2.get()

            self.sql_giris = "Select * FROM kullanicilar where kullanici_adi = '" + self.true_kullanici_adi + "'" + "and sifre = '" + self.true_sifre + "'"
            self.sql_giris_admin = "Select id FROM admins where kullanici_adi = '" + self.true_kullanici_adi + "'" + "and sifre = '" + self.true_sifre + "'"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(self.sql_giris)
            self.myresult = self.mycursor.fetchone()
            self.mycursor.execute(self.sql_giris_admin)
            self.myresult2 = self.mycursor.fetchone()


            if self.myresult != None:
                self.id = self.myresult[0]
                window.destroy()
                self.kullanici_pencere()


            elif self.myresult2!=None:
                window.destroy()
                self.main_pencere()

            else:
                login_msgbox("HATA!","Kullanıcı adı veya şifre yanlış! ","warning",window)

##################################  ADMİN PENCERESİ VE FONKSİYONLARI  #####################################

    def main_pencere(self):
        self.main_window = Tk()

        self.main_window.geometry("850x500")
        self.main_window.configure(bg="#1d272e")
        self.main_window.title("Admins")

        self.main_canvas = Canvas(
        self.main_window,
        bg = "#1d272e",
        height = 500,
        width = 850,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.main_canvas.place(x = 0, y = 0)


        self.main_canvas.create_text(
            182.0,
            5.0,
            anchor="nw",
            text="   ADMINISTRATOR",
            fill="#85FFA7",
            font=("KumarOne Regular", 25 * -1)
        )

        self.main_entry_image_1 = PhotoImage(
            file=relative_to_assets("main_entry_1.png"))
        self.main_entry_bg_1 = self.main_canvas.create_image(
            112.0,
            84.0,
            image=self.main_entry_image_1
        )
        self.main_entry_1 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_1.place(
            x=44.0,
            y=65.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            31.0,
            41.0,
            anchor="nw",
            text="Oyun adı:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_2 = PhotoImage(
            file=relative_to_assets("main_entry_2.png"))
        self.main_entry_bg_2 = self.main_canvas.create_image(
            110.0,
            153.0,
            image=self.main_entry_image_2
        )
        self.main_entry_2 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_2.place(
            x=42.0,
            y=134.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            110.0,
            anchor="nw",
            text="Türü:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_entry_image_3 = PhotoImage(
            file=relative_to_assets("main_entry_3.png"))
        self.main_entry_bg_3 = self.main_canvas.create_image(
            110.0,
            222.0,
            image=self.main_entry_image_3
        )
        self.main_entry_3 = Entry(
            bd=0,
            bg="#A8A8A8",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.main_entry_3.place(
            x=42.0,
            y=203.0,
            width=136.0,
            height=36.0
        )

        self.main_canvas.create_text(
            32.0,
            179.0,
            anchor="nw",
            text="Platform:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.main_button_image_1 = PhotoImage(
            file=relative_to_assets("main_button_1.png"))
        self.main_button_1 = Button(
            image=self.main_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.tablo_kayit_button,
            relief="flat"
        )
        self.main_button_1.place(
            x=248.0,
            y=400.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_2 = PhotoImage(
            file=relative_to_assets("main_button_2.png"))
        self.main_button_2 = Button(
            image=self.main_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.guncelle_oyun,
            relief="flat"
        )
        self.main_button_2.place(
            x=248.0,
            y=340.0,
            width=98.0,
            height=44.0
        )
        self.main_button_image_3 = PhotoImage(
            file=relative_to_assets("main_button_3.png"))
        self.main_button_3 = Button(
            image=self.main_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.silme_islemi,
            relief="flat"
        )
        self.main_button_3.place(
            x=248.0,
            y=280.0,
            width=98.0,
            height=44.0
        )


        self.table_frame=Frame(self.main_window,bd=10,relief=RIDGE,bg="#141a1f")
        self.table_frame.place(x=400,y=55,width=450,height=395)

        self.scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=ttk.Scrollbar(self.table_frame, orient=VERTICAL)
        self.oyun_tablo=ttk.Treeview(self.table_frame,columns=("b","id","a_m","a_km"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.oyun_tablo.xview)
        self.scroll_y.config(command=self.oyun_tablo.yview)

        self.oyun_tablo.heading("b", text="id",anchor=W)
        self.oyun_tablo.heading("id",text="Oyun adı",anchor=W)
        self.oyun_tablo.heading("a_m", text="Türü",anchor=W)
        self.oyun_tablo.heading("a_km", text="Platform",anchor=W)

        self.oyun_tablo.column("b",width=20)
        self.oyun_tablo.column("id", width=50)
        self.oyun_tablo.column("a_m", width=50)
        self.oyun_tablo.column("a_km", width=40)
        self.veri_aktarimi()

        self.oyun_tablo["show"]="headings"
        self.oyun_tablo.pack(fill=BOTH,expand=1)

        self.oyun_tablo.bind("<ButtonRelease-1>", self.get_cursor_row)


        self.main_window.resizable(False, False)
        self.main_window.mainloop()

    def guncelle_oyun(self):
        selected_item = self.oyun_tablo.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir oyun seçin!", "warning", self.main_window)
            return

        selected = self.oyun_tablo.item(selected_item)['values'][0]

        yeni_oyun = self.main_entry_1.get()
        yeni_turu = self.main_entry_2.get()
        yeni_platfrom = self.main_entry_3.get()

        guncelle_query_parts = []


        if not selected:  # Eğer seçilmediyse
            login_msgbox("HATA!", "Güncellenecek bir alan seçilmedi!", "error", self.main_window)
            return

        update_query = f"UPDATE oyunlar SET Oyun_adi=%s , turu=%s , platform=%s WHERE Oyun_id = {str(selected)}"

        print("Sorgu:", update_query)

        try:
            self.my_cursor.execute(update_query, (yeni_oyun, yeni_turu,yeni_platfrom))
            login_msgbox("BAŞARILI", "Oyun bilgileri güncellendi!", "information", self.main_window)
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"Oyun bilgileri güncellenemedi: {e}", "error", self.main_window)

    def silme_islemi(self):

        selected_item = self.oyun_tablo.selection()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir oyun seçin!", "warning", self.main_window)
            return

        selected = self.oyun_tablo.item(selected_item)['values'][0]


        self.sql_guncelle_delete = "DELETE from oyunlar WHERE oyun_id = %s"

        try:
            self.my_cursor.execute(self.sql_guncelle_delete, ( selected,))
            self.mydb.commit()

            # Güncelleme başarılıysa Treeview'daki veriyi güncelle
            self.veri_aktarimi()

        except Exception as e:
            login_msgbox("HATA!", f"Kayıt silinemedi: {e}", "error", self.main_window)

    def tablo_kayit_button(self):
        # Veritabanı bağlantısını doğrudan oluşturun
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_oyun"
        )

        # Eğer `veritabani()` fonksiyonunuz bir veritabanı bağlantısı döndürmüyorsa, bu satırı kullanabilirsiniz
        # self.mydb = self.veritabani()

        self.giris1 = self.main_entry_1.get()
        self.giris2 = self.main_entry_2.get()
        self.giris3 = self.main_entry_3.get()


        # Eğer `self.mydb` değeri `None` ise, cursor oluşturmayın
        if self.mydb:
            self.my_cursor = self.mydb.cursor()
            self.sql_tablo_veri = "INSERT INTO oyunlar (Oyun_adi,turu,platform) VALUES (%s, %s, %s)"
            if not self.giris1.strip() or not self.giris2.strip() or not self.giris3.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.main_window)
            else:
                self.my_cursor.execute(self.sql_tablo_veri,
                                       (self.giris1, self.giris2, self.giris3))
                self.mydb.commit()
                self.veri_aktarimi()
                login_msgbox("Tebrikler!","Kayıt başarılı!","information",self.main_window)
        else:
            login_msgbox("HATA!", "Veritabanı bağlantı hatası!", "error", self.main_window)

    def veri_aktarimi(self):
        self.sql_veri_aktarimi="select Oyun_id,Oyun_adi,turu,platform from oyunlar"
        self.my_cursor = self.mydb.cursor()
        self.my_cursor.execute(self.sql_veri_aktarimi)
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.oyun_tablo.delete(*self.oyun_tablo.get_children())
            for i in self.rows:
                self.oyun_tablo.insert("",END,values=i)
            self.mydb.commit()

    def veri_aktarimi1(self):
        self.veritabani()
        self.sql_veri_aktarimi1="select Oyun_adi,turu,platform from oyunlar"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql_veri_aktarimi1)
        self.rows1=self.my_cursor1.fetchall()
        if len(self.rows1)!=0:
            self.oyun_tablo1.delete(*self.oyun_tablo1.get_children())
            for i in self.rows1:
                self.oyun_tablo1.insert("",END,values=i)
            self.mydb.commit()


    def get_cursor_row(self, event=""):
        cursor_row = self.oyun_tablo.focus()
        content = self.oyun_tablo.item(cursor_row)
        row = content["values"]

        # Entry widget'larını güncelle
        self.main_entry_1.delete(0, END)
        self.main_entry_1.insert(0, row[1] if row and len(row) > 0 else "")

        self.main_entry_2.delete(0, END)
        self.main_entry_2.insert(0, row[2] if row and len(row) > 1 else "")

        self.main_entry_3.delete(0, END)
        self.main_entry_3.insert(0, row[3] if row and len(row) > 2 else "")





##################################  KULLANICI PENCERESİ + YORUM PENCERESİ ve FONKSİYONLARI  #####################################
    def kullanici_pencere(self):

        self.kullanici_window = Tk()

        self.kullanici_window.geometry("850x500")
        self.kullanici_window.configure(bg="#2f753b")
        self.kullanici_window.title("Zteam")

        self.kullanici_window_canvas = Canvas(
            self.kullanici_window,
            bg="#2f753b",
            height=500,
            width=850,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.kullanici_window_canvas.place(x=0, y=0)
        self.kullanici_photo = PhotoImage(
            file=relative_to_assets("game1.png"))
        self.kullanici_image_1 = self.kullanici_window_canvas.create_image(
            425.0,
            250.0,
            image=self.kullanici_photo
        )



        self.table_frame1 = Frame(self.kullanici_window, bd=10, relief=RIDGE, bg="#80ad88")
        self.table_frame1.place(x=400, y=55, width=450, height=395)

        self.scroll_x1 = ttk.Scrollbar(self.table_frame1, orient=HORIZONTAL)
        self.scroll_y1 = ttk.Scrollbar(self.table_frame1, orient=VERTICAL)
        self.oyun_tablo1 = ttk.Treeview(self.table_frame1, columns=("oyun", "tür", "platform"),
                                       xscrollcommand=self.scroll_x1.set, yscrollcommand=self.scroll_y1.set)

        self.scroll_x1.pack(side=BOTTOM, fill=X)
        self.scroll_y1.pack(side=RIGHT, fill=Y)

        self.scroll_x1.config(command=self.oyun_tablo1.xview)
        self.scroll_y1.config(command=self.oyun_tablo1.yview)

        self.oyun_tablo1.heading("oyun", text="Oyun adı", anchor=W)
        self.oyun_tablo1.heading("tür", text="Türü", anchor=W)
        self.oyun_tablo1.heading("platform", text="Platform", anchor=W)

        self.oyun_tablo1.column("oyun", width=50)
        self.oyun_tablo1.column("tür", width=50)
        self.oyun_tablo1.column("platform", width=40)


        self.veri_aktarimi1()

        self.oyun_tablo1["show"] = "headings"
        self.oyun_tablo1.pack(fill=BOTH, expand=1)



        self.ekle_buton_image = PhotoImage(
            file=relative_to_assets("ekle.png"))
        self.ekle_buton = Button(
            image=self.ekle_buton_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command = self.ekleme_islemi
        )
        self.ekle_buton.place(
            x=250.0,
            y=400.0,
            width=140.0,
            height=44.0
        )

        self.bilgi_image = PhotoImage(
            file=relative_to_assets("bilgi.png"))
        self.bilgi = Button(
            image=self.bilgi_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.kayit_bilgi,
            relief="flat"
        )
        self.bilgi.place(
            x=10.0,
            y=10.0,
            width=150.0,
            height=44.0
        )

        self.yorumlar_image_1 = PhotoImage(
            file=relative_to_assets("yorumlar.png"))
        self.yorumlar_button = Button(
            image=self.yorumlar_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.yorumlar_penceresi,
            relief="flat"
        )
        self.yorumlar_button.place(
            x=10.0,
            y=140.0,
            width=150.0,
            height=44.0
        )
        self.geri_image_1 = PhotoImage(
            file=relative_to_assets("geri.png"))


        self.geri = Button(
            image=self.geri_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.geri_gel,
            relief="flat"
        )


        self.kullanici_window.resizable(False, False)
        self.kullanici_window.mainloop()

    def ekleme_islemi(self):
        selected_item = self.oyun_tablo1.focus()

        if not selected_item:
            login_msgbox("HATA!", "Lütfen bir oyun seçin!", "warning", self.kullanici_window)
            return

        selected = self.oyun_tablo1.item(selected_item)['values'][0]

        query_ekle = "UPDATE oyunlar SET alan=%s WHERE Oyun_adi = %s"
        val = (self.id, selected)

        try:
            self.my_cursor1 = self.mydb.cursor()
            self.my_cursor1.execute(query_ekle, val)
            self.mydb.commit()
            self.veri_aktarimi1()
            messagebox.showinfo("Başarılı", f"Kütüphaneye eklendi!")
        except Exception as e:
            messagebox.showerror("Hata!", f"Ekleme sırasında bir hata oluştu: {e}")

    def kayit_bilgi(self):
########### KAYIT BİLGİLERİNİ TABLOYA GETİRTME ###########
        self.oyun_tablo1.delete(*self.oyun_tablo1.get_children())



        self.veritabani()
        # Veriyi güncel Treeview'a aktar
        self.kayit_sql_sorgu = "SELECT Oyun_adi,turu,platform FROM oyunlar WHERE alan=%s"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.kayit_sql_sorgu, (self.id,))
        self.rows1 = self.my_cursor1.fetchall()

        if len(self.rows1) != 0:
            self.oyun_tablo1.delete(*self.oyun_tablo1.get_children())
            for i in self.rows1:
                self.oyun_tablo1.insert("", END, values=i)
            self.mydb.commit()

        self.geri.place(
            x=200.0,
            y=10.0,
            width=150.0,
            height=44.0
        )

    def geri_gel(self):
        self.oyun_tablo1.delete(*self.oyun_tablo1.get_children())
        self.veri_aktarimi1()

        self.geri.place_forget()

    def yorumlar_penceresi(self):
        self.kullanici_window.destroy()

        self.kullanici_window1 = Tk()

        self.kullanici_window1.geometry("850x500")
        self.kullanici_window1.configure(bg="#FFFFFF")
        self.kullanici_window1.title("Zteam")

        self.kullanici_window_canvas = Canvas(
            self.kullanici_window1,
            bg="#FFFFFF",
            height=500,
            width=850,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.kullanici_window_canvas.place(x=0, y=0)
        self.kullanici_photo = PhotoImage(
            file=relative_to_assets("game1.png"))
        self.kullanici_image_1 = self.kullanici_window_canvas.create_image(
            425.0,
            250.0,
            image=self.kullanici_photo
        )

        self.ara_image_1 = PhotoImage(
            file=relative_to_assets("ara.png"))
        self.ara = Button(
            image=self.ara_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.yorum_tablosu,
            relief="flat"
        )
        self.ara.place(
            x=45.0,
            y=120.0,
            width=150.0,
            height=44.0
        )
        self.geri_image_1 = PhotoImage(
            file=relative_to_assets("geri.png"))
        self.geri = Button(
            image=self.geri_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.gerigel_yorum,
            relief="flat"
        )
        self.geri.place(
            x=0.0,
            y=0.0,
            width=150.0,
            height=44.0
        )

        self.yorum_entry = Entry(
            bd=0,
            bg="WHITE",
            fg="#000716",
            highlightthickness=0,
        )
        self.yorum_entry.place(
            x=35.0,
            y=340.0,
            width=170.0,
            height=30.0
        )

        self.kullanici_window_canvas.create_text(
            22.0,
            320.0,
            anchor="nw",
            text="   Yorumunuz:",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )

        self.puan = Entry(
            bd=0,
            bg="WHITE",
            fg="#000716",
            highlightthickness=0,
            textvariable=StringVar(value="")
        )
        self.puan.place(
            x=35.0,
            y=400.0,
            width=170.0,
            height=30.0
        )

        self.kullanici_window_canvas.create_text(
            22.0,
            380.0,
            anchor="nw",
            text="   Puan(5 üzerinden):",
            fill="#FFFFFF",
            font=("KumarOne Regular", 15 * -1)
        )
        self.yorumekle_image = PhotoImage(
            file=relative_to_assets("yorum.png"))
        self.yorum_ekle = Button(
            image=self.yorumekle_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.yorum_yap,
            relief="flat"
        )
        self.yorum_ekle.place(
            x=215.0,
            y=395.0,
            width=150.0,
            height=44.0
        )
        self.kullanici_window_canvas.create_text(
            400,  # x koordinatı (tablonun ortası)
            20,  # y koordinatı (tablonun üstünde)
            anchor="nw",
            text="Tüm yorumlar anonimdir.",
            fill="Black",
            font=("Arial", 16),)


        self.table_frame11 = Frame(self.kullanici_window1, bd=10, relief=RIDGE, bg="#80ad88")
        self.table_frame11.place(x=400, y=55, width=450, height=395)

        self.scroll_x11 = ttk.Scrollbar(self.table_frame11, orient=HORIZONTAL)
        self.scroll_y11 = ttk.Scrollbar(self.table_frame11, orient=VERTICAL)
        self.oyun_tablo_yorum = ttk.Treeview(self.table_frame11, columns=("id", "a_m"),
                                       xscrollcommand=self.scroll_x11.set, yscrollcommand=self.scroll_y11.set)

        self.scroll_x11.pack(side=BOTTOM, fill=X)
        self.scroll_y11.pack(side=RIGHT, fill=Y)

        self.scroll_x11.config(command=self.oyun_tablo_yorum.xview)
        self.scroll_y11.config(command=self.oyun_tablo_yorum.yview)

        self.oyun_tablo_yorum.heading("id", text="Yorum", anchor=W)
        self.oyun_tablo_yorum.heading("a_m", text="Puan", anchor=W)


        self.oyun_tablo_yorum.column("id", width=130)
        self.oyun_tablo_yorum.column("a_m", width=50)

        self.oyun_tablo_yorum["show"] = "headings"
        self.oyun_tablo_yorum.pack(fill=BOTH, expand=1)


        n = tk.StringVar()
        self.oyun_secim = ttk.Combobox(self.kullanici_window1, width=30, textvariable=n, state="readonly")
        self.oyun_secim['values'] = ('Minecraft', 'GTA', 'Valorant')
        self.oyun_secim.grid(column=2, row=6, padx=(20, 50), pady=60,sticky="w")

        z = tk.StringVar()
        self.oyun_secim1 = ttk.Combobox(self.kullanici_window1, width=30, textvariable=z, state="readonly")
        self.oyun_secim1['values'] = ('Minecraft', 'GTA', 'Valorant')
        self.oyun_secim1.grid(column=2, row=11, padx=(20, 50), pady=110,sticky="w")  # İlk Combobox'ın konumu

    def yorum_tablosu(self):
        self.veritabani()
        cmb=self.oyun_secim.get()

        if cmb=="Minecraft":
            self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())

            self.sql_minecraft="Select * from yorumlar"

            self.my_cursor1 = self.mydb.cursor()
            self.my_cursor1.execute(self.sql_minecraft,)
            self.rows1 = self.my_cursor1.fetchall()

            if len(self.rows1) != 0:
                for i in self.rows1:
                    self.oyun_tablo_yorum.insert("", END, values=i)
                self.mydb.commit()
        elif cmb == "GTA":
            self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())

            self.sql_gta = "Select * from yorumlar_gta"

            self.my_cursor12 = self.mydb.cursor()
            self.my_cursor12.execute(self.sql_gta, )
            self.rows10 = self.my_cursor12.fetchall()

            if len(self.rows10) != 0:
                for i in self.rows10:
                    self.oyun_tablo_yorum.insert("", END, values=i)
                self.mydb.commit()
        elif cmb == "Valorant":
            self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())

            self.sql_valo = "Select * from yorumlar_valo"

            self.my_cursor13 = self.mydb.cursor()
            self.my_cursor13.execute(self.sql_valo, )
            self.rows11 = self.my_cursor13.fetchall()

            if len(self.rows11) != 0:
                for i in self.rows11:
                    self.oyun_tablo_yorum.insert("", END, values=i)
                self.mydb.commit()

    def gerigel_yorum(self):
        self.kullanici_window1.destroy()
        self.kullanici_pencere()

    def yorum_yap(self):
        self.yorum = self.yorum_entry.get()
        self.puan1=self.puan.get()
        cmb1=self.oyun_secim1.get()

        self.my_cursor = self.mydb.cursor()
        if cmb1=="Minecraft":
            sql_mc="INSERT INTO yorumlar (yorum,puan) values (%s,%s)"
            if not self.yorum.strip() or not self.puan1.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.kullanici_window1)
            else:
                self.my_cursor.execute(sql_mc,(self.yorum,self.puan1))
                self.mydb.commit()
                self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())

                self.sql_mc = "Select * from yorumlar"

                self.my_cursor_mc = self.mydb.cursor()
                self.my_cursor_mc.execute(self.sql_mc, )
                self.rows_mc = self.my_cursor_mc.fetchall()

                if len(self.rows_mc) != 0:
                    for i in self.rows_mc:
                        self.oyun_tablo_yorum.insert("", END, values=i)
                    self.mydb.commit()
                    login_msgbox("Tebrikler!", "Kayıt başarılı!", "information", self.kullanici_window1)
        elif cmb1=="GTA":
            sql_gta="INSERT INTO yorumlar_gta (yorum,puan) values (%s,%s)"
            if not self.yorum.strip() or not self.puan1.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.kullanici_window1)
            else:
                self.my_cursor.execute(sql_gta,(self.yorum,self.puan1))
                self.mydb.commit()
                self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())
                self.sql_gta = "Select * from yorumlar_gta"

                self.my_cursor_gta = self.mydb.cursor()
                self.my_cursor_gta.execute(self.sql_gta, )
                self.rows_gta = self.my_cursor_gta.fetchall()

                if len(self.rows_gta) != 0:
                    for i in self.rows_gta:
                        self.oyun_tablo_yorum.insert("", END, values=i)
                    self.mydb.commit()
                    login_msgbox("Tebrikler!", "Yorum kaydedildi!", "information", self.kullanici_window1)

        elif cmb1=="Valorant":
            sql_gta="INSERT INTO yorumlar_valo (yorum,puan) values (%s,%s)"
            if not self.yorum.strip() or not self.puan1.strip():
                login_msgbox("HATA!", "Boşluk bırakma!", "warning", self.kullanici_window1)
            else:
                self.my_cursor.execute(sql_gta,(self.yorum,self.puan1))
                self.mydb.commit()
                self.oyun_tablo_yorum.delete(*self.oyun_tablo_yorum.get_children())
                self.sql_valo = "Select * from yorumlar_valo"

                self.my_cursor_valo = self.mydb.cursor()
                self.my_cursor_valo.execute(self.sql_valo, )
                self.rows_valo = self.my_cursor_valo.fetchall()

                if len(self.rows_valo) != 0:
                    for i in self.rows_valo:
                        self.oyun_tablo_yorum.insert("", END, values=i)
                    self.mydb.commit()
                    login_msgbox("Tebrikler!", "Yorum kaydedildi!", "information", self.kullanici_window1)
        else:
            login_msgbox("HATA!", "Boşluk bırakma", "error", self.kullanici_window1)


app=Uygulama()