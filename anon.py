import sys
import json
import requests


def main(arg):
    raw = requests.post("https://api.anonfiles.com/upload",files={
        "file":(arg[1],open(arg[1],"rb").read()
        )
    }).json()
    if raw["status"] == True: print("[!] Upload Berhasil!");print("[!] Link : {}".format(raw["data"]["file"]["url"]["short"]))
    else: print("[!] Upload Gagal")


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) != 1:
        try:
            open(arg[1],"rb").read() #Check File
            main(arg)
        except FileNotFoundError:
            print("[!] File Tidak Ada")
    else:
        print("[!] Silahkan masukkan file yang akan di upload!")
