import pytest

STUDENT_DATA = {
    "student_name": "Hari",
    "subject": "Hindi",
    "marks": 89
}

EMPTY_DATA = {}


@pytest.mark.parametrize(
    "data",
    [STUDENT_DATA]
)
def test_add_student_data(test_client, data):
    # when
    response = test_client.post(
        "/student", json=data
    )
    # then
    assert response.status_code == 200


def test_add_student_data_without_body(test_client):
    # given
    data = EMPTY_DATA
    # when
    response = test_client.post("/student", json=data)
    # then
    assert response.status_code == 422
