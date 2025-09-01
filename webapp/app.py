from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

EMAIL = "info@codesphere.space"
PASSWORD = "infoCodeSphere@123"

@app.route("/", methods=["GET", "POST"])
def index():
    user_data = {"name": "", "email": "", "message": ""}

    if request.method == "POST":
        # fetch data from form
        user_data["name"] = request.form.get("name")
        user_data["email"] = request.form.get("email")
        user_data["subject"] = request.form.get("subject")
        user_data["message"] = request.form.get("message")

        try:
            # prepare the email
            msg = MIMEMultipart()
            msg["From"] = EMAIL
            msg["To"] = request.form.get("email")  # change to your destination
            msg["cc"] = "info@codesphere.space"
            msg["Subject"] = request.form.get("subject")

            user_body = f"""
            Hi {user_data['name']},
            {user_data['email']}

            ✅ Thank you for contacting CodeSphere!  
            We have received your query and our team will get back to you shortly.

            Here’s a copy of your submission:
            
            Subject: {user_data['subject']}
            Message: {user_data['message']}

            Best regards,  
            CodeSphere Team
            """
            msg.attach(MIMEText(user_body, "plain"))

            # send via yahoo smtp
            server = smtplib.SMTP_SSL("smtp.hostinger.com", 465)
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, msg["To"], msg.as_string())
            server.quit()

            # success = True
            return render_template("index.html", data={})

        except Exception as e:
            print("❌ Error sending email:", e)

    # initial load
    return render_template("index.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=False)
