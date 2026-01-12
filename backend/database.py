import sqlite3

DATABASE = "database.db"


def get_db():
    """
    Create and return a database connection
    """
    conn = sqlite3.connect(DATABASE)
    return conn


def init_db():
    """
    Create tables if they do not exist
    """
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT,
        time TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medical_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        problems TEXT,
        notes TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        record_id INTEGER,
        name TEXT,
        dosage TEXT,
        frequency TEXT,
        duration TEXT
    )
    """)

    conn.commit()
    conn.close()
