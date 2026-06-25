import src.app as app_module


def test_signup_duplicate_check_is_case_sensitive_current_behavior(client):
    # Arrange
    activity_name = "Chess Club"
    same_email_with_different_case = "Michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": same_email_with_different_case},
    )
    activities_after = client.get("/activities").json()

    # Assert
    assert response.status_code == 200
    assert same_email_with_different_case in activities_after[activity_name]["participants"]


def test_signup_rejects_when_activity_is_full(client):
    # Arrange
    activity_name = "Tiny Club"
    app_module.activities[activity_name] = {
        "description": "Capacity boundary test activity",
        "schedule": "Mondays, 1:00 PM - 2:00 PM",
        "max_participants": 1,
        "participants": ["first.student@mergington.edu"],
    }

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": "second.student@mergington.edu"},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
