from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import socket
import platform
import json
from urllib.request import urlopen

interface = Tk()
interface.geometry('200x100')
interface.title('Failide avaja')
def openfile():
    return filedialog.askopenfilename()

button = ttk.Button(interface, text="Ava", command=openfile)
button2 = ttk.Button(interface, text="Välju programmist", command=interface.destroy)
button.grid(column=2, row=2)
button2.grid(column=1, row=2)

#Lisab tekstikasti kollase taustavärvusega
t1 = Text(interface,  height=1, width=8,bg='yellow')
t1.grid(row=1,column=2)


interface.mainloop()


#Näitab arvutinime ja ip-addressi
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Sinu arvuti nimi on:" + hostname)
print("Sinu arvuti IP-aaddress on:" + IPAddr)
#Näitab süsteemiinfot, mis versioon windows jne...
print  (platform.uname())
#Näitab veelgi täpsemalt ip addressi andmeid.
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
loc=data['loc']
postal=data['postal']

print ('Sinu IP-detailid\n ')
print ('IP: {4} \nRegioon: {1} \nRiik: {2} \nLinn: {3} \nOrg: {0} \nPostiindeks: {6} \nKordinaadid: {5} '.format(org,region,country,city,IP,loc,postal))