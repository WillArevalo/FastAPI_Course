import json

def test_create_job(client):
    data = {
        'title':'test title'
        , 'company':'test company'
        , 'company_url':'https://hitmail.com'
        , 'location':'test location'
        , 'description':'Test description'
        , 'date_posted': '2022-07-20'
        }
    response = client.post("/job/create-job",json.dumps(data))
    assert response.status_code == 200
    