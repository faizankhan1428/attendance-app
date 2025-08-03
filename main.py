import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import platform
import gspread
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials

# ====== CONFIGURATION (CHANGE FOR EACH EMPLOYEE) ======
EMPLOYEE_ID = "IDEF2021018"
EMPLOYEE_NAME = "Arham Noman"
EMPLOYEE_POSITION = "Sales Executive"
GOOGLE_SHEET_NAME = "Attendance"
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d"
LOGO_FILE = "IDE Logo.jpg"
# =======================================================

def get_attendance_data():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%I:%M %p")
    system_name = platform.node()
    return [EMPLOYEE_ID, EMPLOYEE_NAME, EMPLOYEE_POSITION, date, time, system_name]

def mark_attendance():
    try:
        # Look for credentials.json outside the .exe
        app_path = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
        credentials_path = os.path.join(app_path, "credentials.json")

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(GOOGLE_SHEET_URL).worksheet(GOOGLE_SHEET_NAME)
        sheet.append_row(get_attendance_data())
        messagebox.showinfo("Success", "Attendance marked successfully.")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", f"Failed to mark attendance.\n\n{str(e)}")

def create_gui():
    root = tk.Tk()
    root.title("Innovative Design Express - Attendance")
    root.geometry("400x550")
    root.resizable(False, False)

    # Load logo (bundled inside .exe)
    if getattr(sys, 'frozen', False):
        app_path = sys._MEIPASS
    else:
        app_path = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(app_path, LOGO_FILE)

    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((200, 100))
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.pack(pady=20)

    # Labels
    tk.Label(root, text="Employee Name:", font=("Arial", 12)).pack()
    tk.Label(root, text=EMPLOYEE_NAME, font=("Arial", 14, "bold")).pack(pady=5)

    tk.Label(root, text="Employee ID:", font=("Arial", 12)).pack()
    tk.Label(root, text=EMPLOYEE_ID, font=("Arial", 14, "bold")).pack(pady=5)

    tk.Label(root, text="Position:", font=("Arial", 12)).pack()
    tk.Label(root, text=EMPLOYEE_POSITION, font=("Arial", 14, "bold")).pack(pady=5)

    # Button
    tk.Button(root, text="Mark Attendance", font=("Arial", 14), bg="green", fg="white",
              width=20, height=2, command=mark_attendance).pack(pady=40)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
