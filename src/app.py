from fastapi import FastAPI, HTTPException # pyright: ignore[reportMissingImports]

app = FastAPI()
# Add a root endpoint to show a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington High School Activities API! Visit /docs for API documentation."}

# Define activities outside the function
activities = {
    "basketball": {
        "type": "sport",
        "description": "Join the basketball team and compete in local tournaments.",
        "participants": []
    },
    "swimming": {
        "type": "sport",
        "description": "Participate in swimming lessons and competitions.",
        "participants": []
    },
    "painting": {
        "type": "artistic",
        "description": "Express your creativity in our painting club.",
        "participants": []
    },
    "theater": {
        "type": "artistic",
        "description": "Act, direct, or help backstage in school theater productions.",
        "participants": []
    },
    "chess": {
        "type": "intellectual",
        "description": "Join the chess club to improve your strategy and compete.",
        "participants": []
    },
    "debate": {
        "type": "intellectual",
        "description": "Develop your public speaking and argumentation skills in debate club.",
        "participants": []
    },
}

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student to participants
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}