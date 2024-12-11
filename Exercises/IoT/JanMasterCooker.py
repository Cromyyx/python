import sys
print(sys.path)

import requests
import datetime
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Replace with your OANDA API key and account ID
API_KEY = 'c87c6526c1d4e236dd321e7d0fd24f34-1af4ff9516cc3cf7c348ee4c514ef80b'
ACCOUNT_ID = '101-001-30091896-001'


def get_candle_close_price(date_time, instrument):
    date_time_str = date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    next_minute_str = (date_time + datetime.timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%SZ')

    url = f"https://api-fxpractice.oanda.com/v3/instruments/{instrument}/candles"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    params = {
        'granularity': 'M1',
        'price': 'M',
        'from': date_time_str,
        'to': next_minute_str
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['candles']:
            close_price = data['candles'][0]['mid']['c']
            return close_price
        else:
            return "No data available for the specified time."
    else:
        return f"Error: {response.status_code} - {response.text}"


def get_closing_prices(start_date, end_date, times, instrument):
    current_date = start_date
    closing_prices = {}

    while current_date <= end_date:
        prices = []
        for time in times:
            date_time = datetime.datetime.combine(current_date, time)
            close_price = get_candle_close_price(date_time, instrument)
            prices.append((time, close_price))
        closing_prices[current_date] = prices
        current_date += datetime.timedelta(days=1)

    return closing_prices


def write_to_csv(closing_prices, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Time1', 'Close Price1', 'Time2', 'Close Price2'])
        for date, prices in closing_prices.items():
            if len(prices) == 2:
                writer.writerow([date, prices[0][0], prices[0][1], prices[1][0], prices[1][1]])


def run_script():
    try:
        start_date = datetime.datetime.strptime(start_date_entry.get(), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date_entry.get(), '%Y-%m-%d').date()
        file_path = file_path_entry.get()
        instrument = instrument_entry.get()
        times = [datetime.time(20, 59), datetime.time(21, 4)]  # You can modify this as needed

        closing_prices = get_closing_prices(start_date, end_date, times, instrument)
        write_to_csv(closing_prices, file_path)

        messagebox.showinfo("Success", f"CSV file has been generated at {file_path}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("OANDA Data Fetcher")

tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Instrument (ex.: EUR_USD):").grid(row=2, column=0, padx=10, pady=5)
instrument_entry = tk.Entry(root)
instrument_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="File Path:").grid(row=3, column=0, padx=10, pady=5)
file_path_entry = tk.Entry(root)
file_path_entry.grid(row=3, column=1, padx=10, pady=5)


def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)


tk.Button(root, text="Browse", command=browse_file).grid(row=3, column=2, padx=10, pady=5)

tk.Button(root, text="Run", command=run_script).grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
