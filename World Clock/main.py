#Rafi Hossain
#Clock for Canada, Bangladesh, and Uae
#Pycharm


import tkinter as tk
from datetime import datetime
import pytz
import time

class ClockApp:
    def __init__(self, master):
        self.master = master
        master.title("World Clock")

        self.label_canada = tk.Label(master, font=("Alarm Clock", 36), background='white')
        self.label_canada.pack()

        self.label_bangladesh = tk.Label(master, font=("Alarm Clock", 36), background='white')
        self.label_bangladesh.pack()

        self.label_uae = tk.Label(master, font=("Alarm Clock", 36), background='white')
        self.label_uae.pack()

        # Load flag images with smaller dimensions
        self.image_canada = tk.PhotoImage(file="Canada.png").subsample(3, 3)
        self.image_bangladesh = tk.PhotoImage(file="Bangladesh.png").subsample(3, 3)
        self.image_uae = tk.PhotoImage(file="UAE.png").subsample(3, 3)

        self.update_clock()

    def update_clock(self):
        current_time_canada = self.get_time_in_timezone("America/Toronto")
        self.label_canada.config(text=f"Canada: {self.format_clock_time(current_time_canada)}")
        self.label_canada.img = self.image_canada  # Keep a reference to the image
        self.label_canada.config(image=self.label_canada.img, compound='right')  # Display the image

        current_time_bangladesh = self.get_time_in_timezone("Asia/Dhaka")
        self.label_bangladesh.config(text=f"Bangladesh: {self.format_clock_time(current_time_bangladesh)}")
        self.label_bangladesh.img = self.image_bangladesh  # Keep a reference to the image
        self.label_bangladesh.config(image=self.label_bangladesh.img, compound='right')  # Display the image

        current_time_uae = self.get_time_in_timezone("Asia/Dubai")
        self.label_uae.config(text=f"UAE: {self.format_clock_time(current_time_uae)}")
        self.label_uae.img = self.image_uae  # Keep a reference to the image
        self.label_uae.config(image=self.label_uae.img, compound='right')  # Display the image

        self.master.after(1000, self.update_clock)  # Update every 1000 milliseconds (1 second)

    def get_time_in_timezone(self, timezone):
        now = datetime.now(pytz.timezone(timezone))
        return now.strftime("%I:%M:%S %p")  # %I: Hour (12-hour clock), %M: Minute, %S: Second, %p: AM or PM

    def format_clock_time(self, time_str):
        # Extracting only HH:MM from the time string and including AM/PM
        return time_str.split(" ")[-2] + " " + time_str.split(" ")[-1]

def main():
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
