from flask import Flask, jsonify, render_template, request, redirect, url_for
from patients import generate_mock_patient
from flask_cors import CORS

# from waitress import serve

app = Flask(__name__)
CORS(app)


num_of_patients = 10


@app.route("/ifem/dataset")  # extra path for encryption
def dataset():
    sort = request.args.get("sort", "arrival_time")
    patients = [generate_mock_patient(num_of_patients) for _ in range(num_of_patients)]
    patients.sort(key=lambda p: getattr(p, sort))

    return jsonify(
        {
            "Waiting Patients": len(patients),
            "patients": [p.serialize() for p in patients],
        }
    )


@app.route("/phases")
def phases():
    return render_template("phases.html", title="Home")


@app.route("/triage")
def triage():
    return render_template("triage.html", title="Home")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] not in [
            "admin",
            "user001",
            "user002",
        ] or request.form["password"] not in ["admin", "user001", "user002"]:
            error = "Invalid Credentials. Please try again."
        else:
            return redirect("http://localhost:5173/")
    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
