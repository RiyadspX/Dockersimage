from app import app

def test_home():
    response = app.test_client().get("/")
    
    assert response.status_code == 200
    assert response.data == b"This page is only for making a CI/CD pipeline and deploy it on docker hub"