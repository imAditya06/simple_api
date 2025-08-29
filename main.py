from fastapi import FastAPI

app = FastAPI()

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# In-memory storage
appointments = []

# Create appointment
@app.post("/appointments")
def create_appointment(appointment: dict):
    appointments.append(appointment)
    return appointment

# Get all appointments
@app.get("/appointments")
def get_appointments():
    return appointments
