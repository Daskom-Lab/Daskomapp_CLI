import json
import urllib
from urllib import request
from os import system,name
import requests
def clear():

  # for windows
  if name == 'nt':
      _ = system('cls')

  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')
website="https://daskomlab.com/api"
clear();
data={

}
data=json.dumps(data)
print("Welcome to Daskom App CLI!")
print("1. Lihat TP\n2. Lihat Laporan\n3. Lihat Nilai")
inp=input("Masukan pilihan: ");
if inp == '2':
    response=requests.post(website+"/getAllModul")
    output=response.json()
    for i in range(24):
        print(i);print("-->"+output[i]['judul'])
    modul=input("Masukan modul (dengan angka): ")
    response=requests.post(website+"/getAllLaporan/"+modul);
    output=response.json()
    for n in range(4):
        print("================ S H I F T  "+str(n+1)+" ================")
        print(output['all_laporan'][n]['laporan'])
        print("\n")
if inp=='1':
    nim=input("Masukan nim: ")
    response=requests.post(website+"/getAllModul")
    output=response.json()
    for i in range(24):
        print(i);print("-->"+output[i]['judul'])
    modul=input("Masukan modul (dengan angka): ")
    modul=int(modul)+1
    nim_s=str(nim)
    modul_s=str(modul)
    response=requests.post(website+"/getTp/"+nim_s+"/"+modul_s);
    output=response.json()
    #print(output)
    if output['message']=='success':    
        for n in range(8):
            print("========== NOMOR "+str(n+1)+"=========")
            print(output['all_tp'][n]['soal'])
            print("---------------------------------------------------")
            print("jawaban: ")
            print(output['all_tp'][n]['jawaban'])
            print("\n")
    else:
        print(output['message'])

if inp=='3':
    nim=input("Masukan nim: ")
    response=requests.post(website+"/getAllModul")
    output=response.json()
    for i in range(24):
        print(i);print("-->"+output[i]['judul'])
    modul=input("Masukan modul (dengan angka): ")
    modul=int(modul)+1
    nim_s=str(nim)
    modul_s=str(modul)
    response=requests.post(website+"/getNilai/"+nim_s+"/"+modul_s);
    output=response.json()
    #print(output)
    if output['message']=='success':    
        print("Tugas Pendahuluan: ");print(output['nilai']['tp'])
        print("Tes Awal: ");print(output['nilai']['ta'])
        print("Jurnal: ");print(output['nilai']['jurnal'])
        print("Tes Akhir: ");print(output['nilai']['tk'])
        print("Skill: ");print(output['nilai']['skill'])
        print("Diskon: ");print(output['nilai']['diskon'])
        print("Rating: ");print(output['nilai']['rating'])
        print("Asisten ID: ");print(output['nilai']['asisten_id'])
    else:
        print(output['message'])
