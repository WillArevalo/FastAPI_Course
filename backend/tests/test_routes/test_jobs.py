import json


def test_create_job(client, normal_user_token_headers):
    data = {
        'title':'test title 3'
        , 'company':'test company'
        , 'company_url':'https://hitmail.com'
        , 'location':'test location'
        , 'description':'Test description'
        , 'date_posted': '2022-07-20'
        }
    response = client.post(
        "/job/create-job",
        data=json.dumps(data),
        headers=normal_user_token_headers
        )
    assert response.status_code == 200


def test_retrieve_job_by_id(client):
    data = {
        'title':'test title 3'
        , 'company':'test company'
        , 'company_url':'https://hitmail.com'
        , 'location':'test location'
        , 'description':'Test description'
        , 'date_posted': '2022-07-20'
        }
    client.post("/job/create-job",json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()['title'] == 'test title 3'
    