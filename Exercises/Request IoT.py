import requests
import psutil

API_KEY = '8A8VU9S997XDY39S'
url = 'https://api.thingspeak.com/update'

last_percent = None
last_plugged = None

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    plugged_str = "1" if plugged else "0"  # 1 = Plugged in, 0 = Not plugged in

    if percent != last_percent or plugged_str != last_plugged:
        print(f'{percent}% | {plugged_str}')

        data = {
            'api_key': API_KEY,
            'field1': plugged_str,  # Example value for field 1
            'field2': str(percent),  # Example value for field 2
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            print('Data sent successfully!')
        else:
            print(f'Error sending data: {response.status_code}')

        last_percent = percent
        last_plugged = plugged_str
