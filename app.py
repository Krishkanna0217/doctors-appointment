from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_db, init_db

app = Flask(__name__)
CORS(app)

# 🔹 Initialize database and tables on startup
init_db()

@app.route("/")
def home():
    return jsonify({"message": "Backend running successfully"})

# -------------------------------
# Book Appointment (Patient)
# -------------------------------
@app.route("/book", methods=["POST"])
def book_appointment():
    data = request.json

    db = get_db()
    cur = db.cursor()

    cur.execute(
        """
        INSERT INTO appointments (patient_id, doctor_id, date, time)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["patient_id"],
            data["doctor_id"],
            data["date"],
            data["time"]
        )
    )

    db.commit()
    db.close()

    return jsonify({"message": "Appointment booked successfully"})


# -----------------------------------------
# Doctor Adds Diagnosis + Medications
# -----------------------------------------
@app.route("/record", methods=["POST"])
def add_medical_record():
    data = request.json

    db = get_db()
    cur = db.cursor()

    # Insert medical record
    cur.execute(
        """
        INSERT INTO medical_records (appointment_id, problems, notes)
        VALUES (?, ?, ?)
        """,
        (
            data["appointment_id"],
            data["problems"],
            data["notes"]
        )
    )

    record_id = cur.lastrowid

    # Insert medications
    for med in data["medications"]:
        cur.execute(
            """
            INSERT INTO medications (record_id, name, dosage, frequency, duration)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                record_id,
                med["name"],
                med["dosage"],
                med["frequency"],
                med["duration"]
            )
        )

    db.commit()
    db.close()

    return jsonify({"message": "Medical record and medications saved"})


# -----------------------------------------
# Patient Views Appointment Summary
# -----------------------------------------
@app.route("/summary/<int:appointment_id>", methods=["GET"])
def get_summary(appointment_id):
    db = get_db()
    cur = db.cursor()

    # Get medical record
    cur.execute(
        "SELECT id, problems, notes FROM medical_records WHERE appointment_id = ?",
        (appointment_id,)
    )
    record = cur.fetchone()

    if not record:
        return jsonify({"error": "No record found"}), 404

    record_id = record[0]

    # Get medications
    cur.execute(
        """
        SELECT name, dosage, frequency, duration
        FROM medications
        WHERE record_id = ?
        """,
        (record_id,)
    )
    medications = cur.fetchall()

    db.close()

    return jsonify({
        "problems": record[1],
        "notes": record[2],
        "medications": medications
    })


if __name__ == "__main__":
    app.run(debug=True)
