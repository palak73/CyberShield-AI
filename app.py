from flask import Flask, render_template, request, jsonify
from analyzer import analyze_complaint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        complaint = data.get("complaint", "")

        if complaint.strip() == "":
            return jsonify({
                "error": "Complaint cannot be empty"
            }), 400

        result = analyze_complaint(complaint)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)