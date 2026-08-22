from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

correct_username = "jonmir"
correct_password = "admin"


@app.route('/', methods=['POST', 'GET'])
def handle_form():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == correct_username and password == correct_password:
            return redirect('/jonmir.html')
        else:
            return "Wrong username or password"

    return render_template('/login.html')



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


@app.route("/register.html")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)