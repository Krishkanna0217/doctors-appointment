# Healthcare Appointment & Medication System

A web-based healthcare management system that allows patients to book appointments and doctors to record medical diagnoses and prescriptions. Built with Flask backend and a simple HTML/CSS/JavaScript frontend.

## Features

- **Patient Portal**: View prescription summaries and medical records
- **Doctor Portal**: Record diagnoses, notes, and prescribe medications
- **Appointment Booking**: Book appointments between patients and doctors
- **Medical Records**: Store and retrieve medical records with associated medications

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **CORS**: Flask-CORS for cross-origin requests

## Project Structure

```
hackathon/
├── app.py                 # Main Flask application (root)
├── database.py            # Database initialization and connection
├── backend/
│   ├── app.py            # Alternative Flask app structure
│   ├── database.py       # Database module
│   └── requirements.txt  # Backend dependencies
├── frontend/
│   ├── index.html        # Home page with role selection
│   ├── doctor.html       # Doctor portal interface
│   ├── patient.html      # Patient portal interface
│   ├── script.js         # Frontend JavaScript logic
│   └── style.css         # Styling
├── requirements.txt       # Root dependencies
└── database.db           # SQLite database (created on first run)
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd hackathon
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using the backend folder:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```
   
   The server will start on `http://localhost:5000`

4. **Open the frontend**
   - Open `frontend/index.html` in your web browser
   - Or serve it using a local web server

## API Endpoints

### `GET /`
Returns a success message confirming the backend is running.

### `POST /book`
Book an appointment.

**Request Body:**
```json
{
  "patient_id": 1,
  "doctor_id": 1,
  "date": "2024-01-15",
  "time": "10:00 AM"
}
```

### `POST /record`
Add a medical record with diagnosis and medications.

**Request Body:**
```json
{
  "appointment_id": 1,
  "problems": "Fever and cough",
  "notes": "Patient should rest and stay hydrated",
  "medications": [
    {
      "name": "Paracetamol",
      "dosage": "500mg",
      "frequency": "Twice daily",
      "duration": "5 days"
    }
  ]
}
```

### `GET /summary/<appointment_id>`
Retrieve medical summary for a specific appointment.

**Response:**
```json
{
  "problems": "Fever and cough",
  "notes": "Patient should rest and stay hydrated",
  "medications": [
    ["Paracetamol", "500mg", "Twice daily", "5 days"]
  ]
}
```

## Database Schema

### Tables

- **appointments**: Stores appointment information
  - `id`, `patient_id`, `doctor_id`, `date`, `time`

- **medical_records**: Stores diagnosis and notes
  - `id`, `appointment_id`, `problems`, `notes`

- **medications**: Stores prescribed medications
  - `id`, `record_id`, `name`, `dosage`, `frequency`, `duration`

## Usage

1. **For Patients**:
   - Navigate to Patient Portal
   - Enter your appointment ID
   - View your prescription and medical summary

2. **For Doctors**:
   - Navigate to Doctor Portal
   - Enter appointment ID
   - Fill in problems, notes, and medication details
   - Submit the medical summary

## Development

The database is automatically initialized when the Flask app starts. The `init_db()` function creates all necessary tables if they don't exist.

## Requirements

- Python 3.7+
- Flask 2.3.3
- Flask-CORS 4.0.0

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
