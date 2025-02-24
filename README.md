# AIHELPin-webpage
Developed a webpage for recruitment process of AI-Help.in where google sheets have been connected as database

This project is a recruitment portal for **AIHelp.in**, built using **Flask**, **Google Sheets** as the database, and HTML/CSS for the frontend. It allows users to **sign up, log in, reset passwords, and access a categorized dashboard**.

## Features
- **User Signup & Login**  
- **Google Sheets Integration** as the Database  
- **Password Reset Functionality**  
- **Dashboard with User-Specific Features**  
- **Categorization of Users (Category A & B)**  
- **Responsive UI with Modern Styling**

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Google Sheets (via `gspread` library)
- **Authentication**: Form-based login with password storage in Google Sheets

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install Dependencies
Ensure you have Python installed. Then, install required dependencies:
```sh
pip install flask gspread oauth2client
```

3. Configure Google Sheets API
Create a Google Cloud project and enable the Google Sheets API.
Generate a Service Account Key (JSON file).
Replace project-1-451705-7f7dbd86****.json with your actual JSON key file.

4. Run the Flask App

├── app.py              # Flask Backend
├── templates/
│   ├── index.html      # Login & Signup Page
│   ├── dashboard.html  # User Dashboard
└── README.md           # Project Documentation

## Usage
1. Sign Up with a username, password, and category (A/B).
2. Log In to access the dashboard.
3. Forgot Password? Reset your password via the login page.
4. Dashboard will display user-specific options based on their category.
   
## Contribution
Feel free to fork this repo, submit PRs, or report issues. 🚀

