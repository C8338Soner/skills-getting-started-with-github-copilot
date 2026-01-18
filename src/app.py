from fastapi import FastAPI, HTTPException # pyright: ignore[reportMissingImports]


app = FastAPI()
# Add a root endpoint to show a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington High School Activities API! Visit /docs for API documentation."}

# Define activities outside the function
activities = {
    "basketball": {"type": "sport", "participants": []},
    "swimming": {"type": "sport", "participants": []},
    "painting": {"type": "artistic", "participants": []},
    "theater": {"type": "artistic", "participants": []},
    "chess": {"type": "intellectual", "participants": []},
    "debate": {"type": "intellectual", "participants": []},
}

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student to participants
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}