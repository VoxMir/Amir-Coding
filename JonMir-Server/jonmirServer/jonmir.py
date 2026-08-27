from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

correct_username = "jonmir"
correct_password = "admin"


@app.route('/', methods=['GET', 'POST'])
def handle_form():

    if request.method == 'POST':

        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if username == correct_username and password == correct_password:
            return redirect(url_for('jonmir'))

        return render_template(
            'login.html',
            error='Wrong username or password.'
        )

    return render_template('login.html')



@app.route("/jonmir.html")
def jonmir():
    return render_template("jonmir.html")


@app.route("/jonmir.html/memories.html")
def memories():
    return render_template("memories.html")


@app.route("/jonmir.html/backups.html")
def backups():
    return render_template("backups.html")


@app.route("/jonmir.html/aboutus.html")
def aboutus():
    return render_template("aboutus.html")


@app.route("/jonmir.html/applications.html")
def jonmir_apps():
    return render_template("applications.html")


@app.route("/register.html", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        date = request.form.get("date")

        print("New account created:")
        print("Email:", email)
        print("Username:", username)
        print("Date of birth:", date)

        return render_template(
            "account_created.html",
            username=username,
            email=email
        )

    return render_template("register.html")

@app.route("/resetpassword.html", methods=["GET", "POST"])
def respassword():

    if request.method == "POST":

        email = request.form.get("email")

        if not email:
            return "Please enter your email."

        print("Reset requested for:", email)
        
        return render_template(
            "reset_sent.html",
            email=email
        )

    return render_template("resetpassword.html")

@app.route("/forgotemail.html", methods=["GET", "POST"])
def changeemail():

    if request.method == "POST":

        username = request.form.get("username")

        print("Username entered:", username)

        if username == correct_username:
            email = "your-email@example.com"

            return render_template(
                "email_found.html",
                email=email
            )

        return render_template(
            "email_not_found.html"
        )

    return render_template("forgotemail.html")

@app.route("/jonmir.html/projects.html")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)