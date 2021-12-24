import requests
import string
import random
import time
import threading
import sys

print("NitroMake Code Generator")
try:
    f = sys.argv[1]
    if f=='-f':
        rl = 0
    else:
        rl = 0.5
except:
    rl = 0.5
    print("\n\nTo prevent ratelimiting, a request will only be posted every 0.5 seconds. To avoid that, run the generator with the -f Parameter")
num = int(input("How many codes do you want to generate? > "))
with open("NitroCodes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered a high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

def check(url):
        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            with open("ValidCodes.txt","r") as f:
                data = f.read()
            data+="\n"+nitro
            with open("ValidCodes.txt","w") as f:
                f.write(data)
            return
        else:
            #should be invalid
            print(f" Invalid | {nitro} ")

with open("NitroCodes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        
        t = threading.Thread(target=lambda: check(url))
        t.start()
        time.sleep(rl)


print("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt try going for high numbers and being patient.")
