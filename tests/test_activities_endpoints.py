def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert expected_keys.issubset(data["Chess Club"].keys())
    assert isinstance(data["Chess Club"]["participants"], list)


def test_get_activities_contains_baseline_dataset(client):
    # Arrange
    minimum_expected_activities = 5

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) >= minimum_expected_activities
