
import os, platform, subprocess, os, time, speedtest

import wifi
from tkinter import messagebox, scrolledtext
from tkinter import *
from pip._internal import main
import tkinter.ttk as ttk
from PIL import ImageTk, Image
windowWidth = 670
windowHeight = 650
root = Tk()
positionTop = int(root.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
root.title("WiFi TRACKER")
root.iconbitmap('main.ico')
root.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, positionRight ,positionTop))
root.resizable(False, False)
speed = speedtest.Speedtest()
wifiImage = ImageTk.PhotoImage(Image.open('main.ico'))
logo = ImageTk.PhotoImage(Image.open('main1.ico'))

#-------------------------
options =['netsh', 'wlan', 'show', 'profiles']
data = subprocess.check_output(options).\
    decode('utf-8', errors="backslashreplace").split('\n')
# wifi profile names
profiles = [i.split(":")[1][1:-1] for i in
            data if "All User Profile" in i]
# printing wifi and their passwords
def showWifiNamesAndPasswords():
    for i in profiles:
          try:
              results = subprocess.check_output(
                  ['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])\
                  .decode('utf-8', errors="backslashreplace").split('\n')
              # result object holds the wifi password.
              results = [b.split(":")[1][1:-1]
                         for b in results if "Key Content" in b]
              try:
                  wifi_passwords_Names.config(state="normal")
                  wifi_passwords_Names.insert('0.0', "|{:<30}|  {:<25}|\n".format(i, results[0]))
                  wifi_passwords_Names.config(state="disabled")
                  # print ("|{:<30}|  {:<25}|".format(i, results[0]))
              except IndexError:
                  print ("|{:<30}|  {:<25}|".format(i, ""))
          except subprocess.CalledProcessError:
              print ("|{:<30}|  {:<}|".format(i, "ENCODING ERROR"))

    return
label =Label(root, text="WiFi TRACKER", image=wifiImage ,compound=LEFT, font=("Arial",15,  "bold"))
label.grid(row=0, column=0, columnspan =3, pady=10, sticky=W)
Label(root, image=wifiImage ,compound=LEFT, font=("Arial",15,  "bold")).grid(row=0, column=2, sticky=E)
surperator = ttk.Separator(root, orient=HORIZONTAL)
surperator.grid(row=1, column=0, ipadx=500, sticky=W, columnspan =8)

Label(root, text="WiFi Infomation").grid(row=2, column=0, sticky=W, columnspan=2)
Label(root, text="Name").grid(row=3, column=0 , sticky=W)
upload= Label(root, text="Upload Speed")
upload.grid(row=4, column=0 , sticky=W)
download= Label(root, text="Download Speed")
download.grid(row=5, column=0, sticky=W)
Label(root, text="Password").grid(row=6, column=0, sticky=W)

name_entry = ttk.Entry(root)
name_entry.grid(row=3, column=1 , sticky=W, pady=5, columnspan=2)
name_entry.insert(0, profiles[0])
upload_entry = ttk.Entry(root)
upload_entry.insert(0, speed.upload())
upload_entry.grid(row=4, column=1 , sticky=W, pady=5, columnspan=2)
download_entry=ttk.Entry(root)
download_entry.insert(0, speed.download())
download_entry.grid(row=5, column=1 , sticky=W, pady=5, columnspan=2)
password_entry=ttk.Entry(root)
password_entry.grid(row=6, column=1 , sticky=W, pady=5, columnspan=2)

ttk.Separator(root, orient=HORIZONTAL).grid(row=7, column=0, ipadx=500, sticky=W, columnspan =8)

client = speed.get_config()['client']
client2 = speed.get_best_server()
Label(root, text="WiFi Router Infomation").grid(row=8, column=0, sticky=W, columnspan=2)
Label(root, text="Internet Service Provider (ISP)").grid(row=9, column=0 , sticky=W)
Label(root, text="Country").grid(row=10, column=0 , sticky=W)
Label(root, text="Coodinates").grid(row=11, column=0 , sticky=W)
Label(root, text="Country Name").grid(row=12, column=0 , sticky=W)
Label(root, text="Host").grid(row=13, column=0 , sticky=W)
Label(root, text="ID").grid(row=14, column=0 , sticky=W)
isp_entry = ttk.Entry(root)
isp_entry.grid(row=9, column=1 , sticky=W, pady=5,  columnspan=2)
isp_entry.insert(0, client['isp'])
country_entry = ttk.Entry(root)
country_entry.insert(0, client['country'])
country_entry.grid(row=10, column=1 , sticky=W, pady=5, columnspan=2)
lat_entry=ttk.Entry(root)
lat_entry.grid(row=11, column=1 , sticky=W, pady=5)
lat_entry.insert(0,f'latitude: {client["lat"]}')
lng_entry=ttk.Entry(root)
lng_entry.insert(0,f'longitude: {client["lon"]}')
lng_entry.grid(row=11, column=2 , sticky=W, pady=5)
countryname_entry = ttk.Entry(root)
countryname_entry.insert(0, client2['country'])
countryname_entry.grid(row=12, column=1 , sticky=W, pady=5, columnspan=2)
host_entry = ttk.Entry(root)
host_entry.insert(0, client2['host'])
host_entry.grid(row=13, column=1 , sticky=W, pady=5, columnspan=2)
id_entry = ttk.Entry(root)
id_entry.insert(0,client2['id'])
id_entry.grid(row=14, column=1 , sticky=W, pady=5, columnspan=2)

btn_showWifi =Button(root, text="Show WiFi & Passwords" ,relief=SOLID, borderwidth=1, command=showWifiNamesAndPasswords)
btn_showWifi.grid(row=15, column=2, sticky=E, pady=2)

wifi_passwords_Names = scrolledtext.ScrolledText(root, height=6, width=80, state=DISABLED)
wifi_passwords_Names.grid(sticky=W, row=16, column=0, columnspan=7, padx=5)
password_entry.insert(0, "Undefined")
root.mainloop()