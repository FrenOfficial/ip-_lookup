import requests

def get_ip_info(ip):
    url = f"https://api.iplocation.net/?ip={ip}"
    response = requests.get(url)
    data = response.json()
    return data

ip = input("Enter an IP address: ")
info = get_ip_info(ip)

print("Information about the IP address:")
for key, value in info.items():
    if key not in ["response_code", "response_message"]:
        print(f"{key}: {value}")