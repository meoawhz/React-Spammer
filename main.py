import platform
import os
import requests

# Config

ch = ""

msg_id = ""

emj_code = ""

def main():

    if platform.system() == 'Windows':

        os.system('cls & title React X ( 1.0 )')

        db = open("token.txt", "r").readlines()

        for token in db:

            token_real = token.replace("\n", "")

            meoaw = {
                'authorization': token_real
            }

            auth = requests.put(f"https://discord.com/api/v9/channels/{ch}/messages/{msg_id}/reactions/{emj_code}/%40me?location=Message&type=0", headers=meoaw)

            if auth == 204:

                print(" ")

                print("[ + ] React !")

                print(" ")

            else:

                pass

        else:

            print(" ")

            print("[ + ] React Done !")

            print(" ")

    else:

        os.system('cls')

main()