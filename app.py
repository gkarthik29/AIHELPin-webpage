from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
scope = ["http1s://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("project-1-451705-7f7dbd866fb0.json", scope)  # Replace with your credentials file
client = gspread.authorize(creds)
sheet = client.open("User Database").sheet1  # Replace with your sheet name

def check_user_exists(username):
    """Checks if a username already exists in the Google Sheet."""
    usernames = sheet.col_values(1)  # Assuming usernames are in the first column
    return username in usernames

def update_password(username, new_password):
    usernames = sheet.col_values(1)
    if username in usernames:
        index = usernames.index(username) + 1  # +1 because gspread is 1-indexed
        sheet.update_cell(index, 2, new_password) #2 is password column
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        if "signup" in request.form:
            username = request.form["signup_username"]
            password = request.form["signup_password"]
            category = request.form["category"]

            if check_user_exists(username):
                error = "User already exists."
            else:
                sheet.append_row([username, password, category])
                return redirect(url_for("login")) #automatically go to login page after signup
        elif "login" in request.form:
            username = request.form["login_username"]
            password = request.form["login_password"]

            usernames = sheet.col_values(1)
            passwords = sheet.col_values(2)
            categories = sheet.col_values(3)

            if username in usernames:
                index = usernames.index(username)
                if passwords[index] == password:
                    category = categories[index]
                    return redirect(url_for("dashboard", username=username, category=category))
                else:
                    error = "Incorrect password."
            else:
                error = "User not found."
        elif "forgot_password" in request.form:
            username = request.form["forgot_username"]
            new_password = request.form["forgot_password_new"]
            if update_password(username, new_password):
                return render_template("index.html", message="Password updated successfully. Please login.")
            else:
                error = "Username not found."

    return render_template("index.html", error=error)

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/dashboard/<username>/<category>")
def dashboard(username, category):
    return render_template("dashboard.html", username=username, category=category)

if __name__ == "__main__":
    app.run(debug=True)