const API = "http://127.0.0.1:5000";

/* -------------------------
   Doctor submits summary
-------------------------- */
function submitSummary() {
  const appointmentId = document.getElementById("appointmentId").value;

  fetch(`${API}/record`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      appointment_id: appointmentId,
      problems: document.getElementById("problems").value,
      notes: document.getElementById("notes").value,
      medications: [
        {
          name: document.getElementById("medName").value,
          dosage: document.getElementById("dosage").value,
          frequency: document.getElementById("frequency").value,
          duration: document.getElementById("duration").value
        }
      ]
    })
  })
  .then(res => res.json())
  .then(data => alert(data.message));
}

/* -------------------------
   Patient views summary
-------------------------- */
function loadSummary() {
  const appointmentId = document.getElementById("viewAppointmentId").value;

  fetch(`${API}/summary/${appointmentId}`)
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById("summary");

      if (data.error) {
        div.innerHTML = "No medical record found.";
        return;
      }

      div.innerHTML = `
        <h3>Diagnosis</h3>
        <p>${data.problems}</p>

        <h3>Doctor Notes</h3>
        <p>${data.notes}</p>

        <h3>Medications</h3>
        <ul>
          ${data.medications.map(
            m => `<li>${m[0]} – ${m[1]} – ${m[2]} – ${m[3]}</li>`
          ).join("")}
        </ul>
      `;
    });
}

