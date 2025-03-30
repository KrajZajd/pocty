from tkinter import *
from random import randint
import sys

def zacatek_programu():
    if druh_nasobilky == "m":
        mala_nasobilka_priprava()
    elif druh_nasobilky == "v":
        velka_nasobilka_priprava()
    else:
        error("Neočekávaná chyba\n můzete mě kontaktovat na misan.krajic@gmail.com",exit)
def mala_nasobilka_priprava():
    zadavaci_pole.delete(0,END)
    global prvni_cislo, druhy_cislo, text_vypis, tlacitko_ok
    prvni_cislo = randint(0, 10)
    druhy_cislo = randint(0, 10)
    priklad = str(prvni_cislo) + " \u2022 " + str(druhy_cislo) + " = "
    text_vypis.itemconfig(text, text= priklad )
    tlacitko_ok.config(command=vyhodnoceni)
def velka_nasobilka_priprava():
    zadavaci_pole.delete(0,END)
    global prvni_cislo, druhy_cislo, text_vypis, tlacitko_ok
    prvni_cislo = randint(0, 20)
    druhy_cislo = randint(0, 20)
    priklad = str(prvni_cislo) + " \u2022 " + str(druhy_cislo) + " = "
    text_vypis.itemconfig(text, text= priklad )
    tlacitko_ok.config(command=vyhodnoceni)
def vyhodnoceni():
    global body, zadavaci_pole, text_vypis, tlacitko_ok, cislo_prikladu
    zadano = zadavaci_pole.get()
    cislo_prikladu += 1
    try:
        zadanoint = int(zadano)
        if zadanoint == prvni_cislo * druhy_cislo:
            text_vypis.itemconfig(text, text="Výborně!\nsprávná odpověď")
            body += 1
        else:
            text_vypis.itemconfig(text, text="Bohužel\nšpatná odpověď")
        if cislo_prikladu != pocet_prikladu:
            tlacitko_ok.config(command=zacatek_programu)
        else:
            tlacitko_ok.config(command=konec)

    except ValueError:
        error("Můžete zadat jenom celá čísal", zacatek_programu)
def konec():
    zadavaci_pole.delete(0,END)
    global tlacitko_ok, text_vypis, druh_nasobilky, pocet_prikladu 
    vypis = "Vypočítali jsete všechny příklady\n měli jste jich " + str(body) + " právně a " + str(pocet_prikladu - body) + " špatně\n stisknutím tlačítka \nOK program resetujete"
    text_vypis.itemconfig(text, text=vypis)
    pocet_prikladu = 10
    druh_nasobilky = "m"
    tlacitko_ok.config(command=uvitaci_obrazovka)
def pomoc():
    zadavaci_pole.delete(0,END)
    global text_vypis
    text_vypis.itemconfig(text, text="Násobení je jdnoduchý program na \nprocvičení násobilky. \n Ve výchozím nastavení vypočítáte\ndeset příkladů malé násobilky.\nPokud chcete nastavení \nzměnit vyberte možnost \"2\"\nPokud nechcete nastavení \nzměnit vyberte možnost \"1\"")
def nastaveni1():
    zadavaci_pole.delete(0,END)
    global text_vypis, tlacitko_ok
    text_vypis.itemconfig(text, text="kolik příkladů chceš vypočítat?")
    tlacitko_ok.config(command=nastaveni2)
def nastaveni2():
    zadano = zadavaci_pole.get()
    try:
        global pocet_prikladu
        pocet_prikladu = int(zadano)
        nastaveni25()
    except ValueError:
        error("Vstup musí být celé číslo", nastaveni1)
def nastaveni25():
    global text_vypis
    zadavaci_pole.delete(0,END)
    text_vypis.itemconfig(text, text="chcete počítat malou násobilku \n zadejte \" m \".\n Chcete-li počítat velkou\n zadejte \"v\"")
    tlacitko_ok.config(command=nastaveni3)
def nastaveni3():
    global druh_nasobilky, zadavaci_pole
    zadano = zadavaci_pole.get()
    if zadano == "m" or zadano == "v":
        druh_nasobilky = zadano
        zacatek_programu()
    else:
        error("Musíte zadat \"m\" jako malá\n nebo \"v\" jako velká", nastaveni25)
    
def error(zprava_erroru, prikaz_erroru):
    zadavaci_pole.delete(0,END)
    global text_vypis, tlacitko_ok
    text_vypis.itemconfig(text, text="Chyba \n" + zprava_erroru)
    tlacitko_ok.config(command=prikaz_erroru)
def uvitaci_obrazovka_rozcesti():
    zadano = zadavaci_pole.get()
    if zadano == "1":
        zacatek_programu()
    elif zadano == "2":
        nastaveni1()
    elif zadano == "3":
        pomoc()
    else:
        error("neplatný příkaz", uvitaci_obrazovka)
def uvitaci_obrazovka():
    zadavaci_pole.delete(0,END)
    global text_vypis, tlacitko_ok
    text_vypis.itemconfig(text, text="zadejte možnost \n\n 1. Další \n 2.nastavení \n 3. Pomoc")
    zadavaci_pole.pack()
    tlacitko_ok.config(command=uvitaci_obrazovka_rozcesti)
def ukonceni():
    sys.exit()
pocet_prikladu = 10
druh_nasobilky = "m"
prvni_cislo = 0
druhy_cislo = 0
cislo_prikladu = 0
body = 0
okno = Tk()
zadavaci_pole = Entry()
okno.title("násobení")
text_vypis = Canvas(okno, width=200, height=150)
zadavaci_pole = Entry()
text = text_vypis.create_text(100, 75, text="výtejte v počtech \n \n \n \n běží na NT")
tlacitko_ok = Button(text="ok", command=uvitaci_obrazovka)
tlacitko_exit = Button(text="exit", command=ukonceni)
text_vypis.pack()
tlacitko_exit.pack(side=LEFT)
tlacitko_ok.pack(side=RIGHT)
okno.mainloop()
