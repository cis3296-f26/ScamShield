from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    risk_level = None
    warnings = []
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        message_lower = message.lower()

        
        scam_signs = {
            "urgent": "Uses urgent language",
            "immediately": "Creates pressure to act quickly",
            "bank information": "Requests banking information",
            "bank account": "Mentions bank account information",
            "gift card": "Mentions gift card payment",
            "wire transfer": "Mentions a wire transfer",
            "send money": "Asks you to send money",
            "password": "Requests or mentions a password",
            "social security": "Requests sensitive personal information",
            "you have won": "Claims you have won something",
            "click here": "Asks you to click a link"
        }

        
        for phrase, warning in scam_signs.items():
            if phrase in message_lower:
                warnings.append(warning)

        
        links = re.findall(r'https?://\S+|www\.\S+', message)

        if links:
            warnings.append(
                "Contains a link that should be checked before clicking"
            )

        
        if len(warnings) >= 4:
            risk_level = "HIGH"
        elif len(warnings) >= 2:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

    return render_template(
        "index.html",
        risk_level=risk_level,
        warnings=warnings,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)