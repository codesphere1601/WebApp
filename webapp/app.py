from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_data = {"name": "", "email": "", "message": ""}

    if request.method == "POST":
        # fetch data from form
        user_data["name"] = request.form.get("name")
        user_data["email"] = request.form.get("email")
        user_data["message"] = request.form.get("message")

        # pass submitted data to success page
        return render_template("success.html", data=user_data)

    # initial load
    return render_template("index.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=True)
