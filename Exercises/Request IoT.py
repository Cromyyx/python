import requests
import psutil
import time

API_KEY = '8A8VU9S997XDY39S'
url = 'https://api.thingspeak.com/update'

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "1" if plugged else "0"  # 1 = Plugged in, 0 = Not plugged in
    print(percent + '% | ' + plugged)

    data = {
        'api_key': API_KEY,
        'field1': plugged,  # Example value for field 1
        'field2': percent,  # Example value for field 2
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Data sent successfully!')
    else:
        print('Error sending data:', response.status_code)

    time.sleep(15)  # Wait for 15 seconds before running the loop again
