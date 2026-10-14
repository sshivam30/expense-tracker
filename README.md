
# Expense Tracker

A simple web application built using Python, Flask, and SQLite to manage daily expenses.

## Features

- Add new expenses
- View saved expenses
- Edit existing expenses
- Delete expenses
- Store expense records using SQLite
- User interface styled with HTML and CSS

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
Flask/
├── app.py
├── requirements.txt
├── expenses.db
├── templates/
│   ├── index.html
│   └── edit.html
└── static/
    └── style.css
```

Note: The local database is created or maintained by the application and is not included in the GitHub repository.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sshivam30/expense-tracker.git
   ```

2. Navigate to the project folder:

   ```bash
   cd expense-tracker
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python app.py
   ```

7. Open the local URL displayed in your terminal, usually:

   http://127.0.0.1:5000

## Learning Outcomes

- Building routes and handling form submissions with Flask
- Performing database operations using SQLite
- Implementing CRUD functionality
- Connecting HTML templates with a Python backend
- Using Git and GitHub for version control

## Author

Shivam Kumar Sah

GitHub: https://github.com/sshivam30
