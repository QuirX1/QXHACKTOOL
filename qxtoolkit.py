#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyfiglet
from colorama import Fore, Back, Style

os.system("sudo apt-get install figlet toilet")
os.system("sudo apt-get install figlet boxes")
os.system("sudo apt-get install figlet lolcat")
os.system("pip3 install wget")

os.system("""git clone https://github.com/xero/figlet-fonts""")
os.system("git clone https://github.com/thewhiteh4t/seeker.git")
os.system("cd seeker")

os.system("./install.sh")
os.system("""cd figlet-fonts""")
os.system("""sudo mv * /usr/share/figlet/""")

os.system("""cd ..""")
os.system("clear")

os.system("""figlet -f Bloody "QuirX" | sed 's/^/                        /' | lolcat""")
os.system("""toilet -f ivrit 'QuirX HackToolKit' | boxes -p h8 | lolcat""")



print(Fore.LIGHTMAGENTA_EX + "\033[1m" + """ [1] ✓ Port Tarama""" + "\033[1m")
print(Fore.LIGHTGREEN_EX + "\033[1m" + """ [2] ✓ Wordlist Creator""" + "\033[1m")
print(Fore.LIGHTBLUE_EX + "\033[1m" + """ [3] ✓ Mac Changer""" + "\033[1m")
print(Fore.LIGHTCYAN_EX + "\033[1m" + """ [4] ✓ Port Bruter""" + "\033[1m")
print(Fore.LIGHTRED_EX + "\033[1m" + """ [5] ✓ Wordpress Scan""" + "\033[1m")
print(Fore.LIGHTYELLOW_EX + "\033[1m" + """ [6] ✓ Seeker""" + "\033[1m")
print(Fore.WHITE + "\033[1m" + """ [7] ✓ VPN Control""" + "\033[0m" + "\033[1m")
print(Fore.GREEN + "\033[1m" + """ [8] ✓ Sunucu Zafiyet Analizi""" + "\033[1m")
print(Fore.BLUE + "\033[1m" + """ [9] ✓ RootKit""" + "\033[1m")
print(Fore.MAGENTA + "\033[1m" + """ [10] ✓ Kickthemout""" + "\033[1m")
print(Fore.LIGHTBLUE_EX + "\033[1m" + """ [11] ✓ SpamWa""" + "\033[1m")
print(Fore.GREEN + "\033[1m" + """ [12] ✓ Cupp""" + "\033[1m")
print(Fore.LIGHTCYAN_EX + "\033[1m" + """ [13] ✓ User Recon""" + "\033[1m")
print(Fore.BLUE + "\033[1m" + """ [14] ✓ HiddenEye""" + "\033[1m")
print(Fore.LIGHTYELLOW_EX + "\033[1m" + """ [15] ✓ TheFatRat""" + "\033[1m")
print(Fore.LIGHTRED_EX + "\033[1m" + """ [16] ✓ PhoneInfoga""" + "\033[1m")
print(Fore.MAGENTA + "\033[1m" + """ [17] ✓ OSIF""" + "\033[1m")
print(Fore.LIGHTBLUE_EX + "\033[1m" + """ [18] ✓ RequiredQuir""" + "\033[1m")
print(Fore.LIGHTGREEN_EX + "\033[1m" + """ [0] ✓ Exit
      """ + "\033[1m")

# #### PORT TARAMA #####
islemnum = int(input("İslem Numarasını Giriniz: "))

if islemnum == 1:
    hedefip = input("Hedef İp'yi Giriniz: ")
    print(Fore.LIGHTGREEN_EX + "[+] İşlem Başarılı")
    os.system("nmap -sS -sV " + hedefip)
    os.system("clear")


#### WORDLİST CREATOR ####
elif islemnum == 2:
    minkarakter = int(input("Minimum Karakter Sayısı: "))
    maxkarakter = int(input("Max Karakter Sayısı: "))
    karakterler = input("İstediğiniz Karakterleri Giriniz: ")
    kayityeri = input("Kaydedilecek Konum: ")
    os.system("crunch " + str(minkarakter) + " " + str(maxkarakter) + " " + karakterler + " " + "-o " + kayityeri)
    print("[+] İşlem Başarılı")
  #### MAC CHANGER ####
elif islemnum == 3:
    print(""" 
          ___________________________________________
         |                                           |
         |          [1] Random Belirle               |
         |          [2] El ile Belirle               |
         |          [3] Orjinale Çevir               |
         |___________________________________________|                
    """)
    wordislem = int(input("Opsiyon Seçin: "))
    if wordislem == 1:
        os.system("ifconfig eth0 down")
        os.system("macchanger -r eth0")
        os.system("ifconfig eth0 up")
        print("\033[92mYeni MAC Adresi Random Belirlendi.")
    
    elif wordislem == 2:
        macadres = input("Yeni MAC Adres Girin: ")
        os.system("ifconfig eth0 down")
        os.system("macchanger --mac " + macadres + " eth0")
        os.system("ifconfig eth0 up")
        print("\033 [92mYeni MAC Adresi Elle Belirlendi.")
    
    elif wordislem == 3:
        os.system("ifconfig eth0 down")
        os.system("macchanger -p eth0")
        os.system("ifconfig eth0 up")
        print("\033 [92mMAC Adresi Orijinale Döndürüldü.")


 #### PORT KABA KUVVET ####
elif islemnum == 4:
    print(""" 
          ___________________________________________
         |                                           |
         |           [1] FTP                         |
         |           [2] SSH                         |
         |           [3] TELNET                      | 
         |           [4] HTTP                        |
         |           [5] SMB                         |
         |           [6] RDP                         |
         |           [7] VNC                         |
         |           [8] SIP                         | 
         |           [9] REDIS                       |
         |           [10] PostgreSQL                 |
         |           [11] MySql                      |
         |___________________________________________|
    """)

    portislem = int(input("Opsiyon Seçin: "))
    hedefip = input("Hedef İp'yi Giriniz: ")
    kadi = input("Kullanıcı Adı Dosya Yolu: ")
    wlist = input("Wordlist Dosya Yolu: ")

    if portislem == 1:
        os.system("ncrack -p 21 -U " + kadi + " -P " + wlist + " " + hedefip)

    elif portislem == 2:
        os.system("ncrack -p 22 -U " + kadi + " -P " + wlist + " " + hedefip)

    elif portislem == 3:
        os.system("ncrack -p 24 -U " + kadi + " -P " + wlist + " " + hedefip) 

    elif portislem == 4:
        os.system("ncrack -p 80 -U " + kadi + " -P " + wlist + " " + hedefip) 

    elif portislem == 5:
        os.system("ncrack -p 445 -U " + kadi + " -P " + wlist + " " + hedefip)  

    elif portislem == 6:
        os.system("ncrack -p 3389 -U " + kadi + " -P " + wlist + " " + hedefip)

    elif portislem == 7:
        os.system("ncrack -p 5900 -U " + kadi + " -P " + wlist + " " + hedefip)

    elif portislem == 8:
        os.system("ncrack -p 5060 -U " + kadi + " -P " + wlist + " " + hedefip)

    elif portislem == 9:
        os.system("ncrack -p 6379 -U " + kadi + " -P " + wlist + " " + hedefip) 

    elif portislem == 10:
        os.system("ncrack -p 5432 -U " + kadi + " -P " + wlist + " " + hedefip)  

    elif portislem == 11:
        os.system("ncrack -p 3306 -U " + kadi + " -P " + wlist + " " + hedefip)        

 #### WORDPRESS SCAN ####
elif islemnum == 5:
    print(""" 
          ___________________________________________
         |                                           |
         |          [1] Hızlı Tarama                 |
         |          [2] Eklenti Tarama               |
         |          [3] Tema Tarama                  |
         |          [4] Yönetici Kullanıcı Adı Bulma |
         |___________________________________________|                
    """)
    wpislem = int(input("Opsiyon Seçin: "))
    
    if wpislem == 1:
        site = input("Hedef Siteyi Giriniz: ")
        os.system("wpscan --url " + site)

    elif wpislem == 2:
        site = input("Hedef Siteyi Giriniz: ")
        os.system("wpscan --url " + site + " --enumerate p") 

    elif wpislem == 3:
        site = input("Hedef Siteyi Giriniz: ")
        os.system("wpscan --url " + site + " --enumerate t")    

    elif wpislem == 4:
        site = input("Hedef Siteyi Giriniz: ")
        os.system("wpscan --url " + site + " --enumerate u")   
        
    else:
        print("[-] Hatalı Seçim Tekrar Deneyiniz [-]")

#### SEEKER ####
elif islemnum == 6:
     os.system("git clone https://github.com/thewhiteh4t/seeker.git")
     os.chdir("seeker")
     os.system("chmod +x install.sh")
     os.system("./install.sh")
     os.system("python3 seeker.py")
     

  #### VPN TARAMA ####
elif islemnum == 7:
    hedefip = input("Hedef İp'yi Giriniz: ")
    os.system("ike-scan " + hedefip)

 #### SUNUCU ZAFİYET ANALİZİ ####
elif islemnum == 8:
    hedefip = input("Hedef İp'yi Giriniz: ")
    os.system("nikto -h " + hedefip)

 #### ROOTKİT TARAMA ####
elif islemnum == 9:
    os.system("chkrootkit")



elif islemnum == 10:
    os.system("git clone https://github.com/k4m4/kickthemout.git")
    os.chdir("kickthemout")
    os.system("sudo -H pip3 install -r requirements.txt")
    os.system("sudo python3 kickthemout.py")



elif islemnum == 11:
    os.system("git clone https://github.com/krypton-byte/SpamWa")
    os.chdir("SpamWa")
    os.system("python3 spam.py")


elif islemnum == 12:
    os.system("git clone https://github.com/Mebus/cupp.git")
    os.chdir("cupp")
    os.system("chmod +x cupp.py")
    os.system("python3 cupp.py")

elif islemnum == 13:
    os.system("git clone https://github.com/thelinuxchoice/userrecon")
    os.chdir("userrecon")
    os.system("bash userrecon.sh")


elif islemnum == 14:
    os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye")
    os.chdir("HiddenEye-Legacy")
    os.system("pip install -r requirements.txt")
    os.system("pip3 install wget")
    os.system("python3 HiddenEye.py")


elif islemnum == 15:
    os.system("git clone https://github.com/Screetsec/TheFatRat.git")
    os.chdir("TheFatRat")
    os.system("./update && chmod +x setup.sh && ./setup.sh")

elif islemnum == 16:
    os.system("git clone https://github.com/sundowndev/PhoneInfoga")
    os.chdir("PhoneInfoga")
    os.system("python3 -m pip install -r requirements.txt")
    os.systeö("python3 phoneinfoga.py")


elif islemnum == 17:
    os.system("git clone https://github.com/ciku370/OSIF")
    os.chdir("OSIF")
    os.system("pip2 install -r requirements.txt")
    os.system("python2 osif.py")


elif islemnum == 18:
    os.system("""toilet -f term -F border --gay "https://github.com/QuirX1" | boxes -d parchment | lolcat""")

elif islemnum == 0:
    os.system("35")
