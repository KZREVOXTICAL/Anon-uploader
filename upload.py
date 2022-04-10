import sys
import json
import requests


def main(arg):
    raw = requests.post("https://api.anonfiles.com/upload",files={
        "file":(arg[1],open(arg[1],"rb").read()
        )
    }).json()
    if raw["status"] == True: print("[!] Upload Successful!");print("[!] Link : {}".format(raw["data"]["file"]["url"]["short"]))
    else: print("[!] Upload Failed")


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) != 1:
        try:
            open(arg[1],"rb").read() #Check File
            main(arg)
        except FileNotFoundError:
            print("[!] File Not Found!")
    else:
        print("[!] Please enter the file to be uploaded!")
