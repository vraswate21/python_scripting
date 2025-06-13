import requests

url = input("enter website url (with https://):")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("website is up")

    else:
        print(f"website returned status code {response.status_code}")

except:
    print("cloud not reach the website.")