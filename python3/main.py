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
print("Welcome to Daskom Aslab App CLI!")
print("1. Lihat TP\n2. Lihat Laporan\n3. Lihat Nilai")
inp=input("Masukan pilihan: ");
if inp == '2':
    # print("Lihat Laporan\n")
    # response=urllib.request.Request(url=website+"/getAllModul", method="POST")
    # response.add_header("Content-type", "application/json; charset=UTF-8")
    # with urllib.request.urlopen(response) as resp:
    #     result = json.loads(resp.read().decode("utf-8"))
    #     print(result)
    response=requests.post(website+"/getAllModul")
    output=response.json()
    for i in range(21):
        print(i);print("-->"+output[i]['judul'])
    modul=input("Masukan modul (dengan angka): ")
    response=requests.post(website+"/getAllLaporan/"+modul);
    output=response.json()
    print(output[1]['laporan'])

