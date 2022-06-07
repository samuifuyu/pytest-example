import json

import requests


def test_request():
    response = requests.get("wefef")

    assert response.status_code == 200
