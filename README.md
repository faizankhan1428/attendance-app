# Employee Attendance App using Python and Google Sheets

This project is a desktop-based attendance system developed in Python for the company **Innovative Design Express**. It allows each employee to mark their attendance with a single click. The application records the employee's name, ID, position, current date, time, and system name, then logs the entry in a centralized Google Sheet for the administrator.

## Features

- One-click attendance marking for employees
- Real-time logging to Google Sheets via API
- Personalized .exe applications for each employee
- Admin access to complete attendance records in a structured format
- Clean desktop GUI with company branding (logo and employee details)

  ![App Screenshot](app%20image/screenshot.PNG)

## Technologies Used

- Python 3
- Tkinter (for GUI)
- Google Sheets API (via gspread)
- OAuth2 client authentication
- PyInstaller (for creating executable files)

## How It Works

1. The application opens with a personalized interface.
2. The employee clicks the "Mark Attendance" button.
3. The app records:
   - Employee ID
   - Name
   - Position
   - Current date and time
   - System name
4. This data is automatically appended to a shared Google Sheet using the Sheets API.

## Setup Instructions

To run or modify this project:

1. Clone this repository.
2. Create a Google Cloud project and enable the Google Sheets API.
3. Generate a `credentials.json` for your service account.
4. Share the target Google Sheet with your service account email.
5. Place `credentials.json` in the same directory as `main.py`.
