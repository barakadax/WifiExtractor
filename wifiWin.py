import subprocess

try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
except subprocess.CalledProcessError as error:
    data = error.output.decode('utf-8')
if "The Wireless AutoConfig Service (wlansvc) is not running." in data:
    print("Can't exctract wifi passwords because there are none.")
    input()  # So cmd/terminal won't close quick after done running
    exit(1)
data = data.split('\n')
networks = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in networks:
    wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    password = [line.split(':')[1][1:-1] for line in wifi_info if "Key Content" in line]
    try:
        print(f'Wifi: {wifi} Password: {password[0]}')
    except IndexError:
        print(f'Wifi: {wifi} Password: no password!')
input()
exit(0)
