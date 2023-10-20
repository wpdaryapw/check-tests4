import requests
import pytest

breeds_data = requests.get('https://dog.ceo/api/breeds/list/all').json()
breeds_to_test = list(breeds_data["message"].keys())

@pytest.mark.parametrize("breed",breeds_to_test)
def test_dog_api(breed):
    url = f'https://dog.ceo/api/breed/{breed}/images/random'
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert "message" in data

    breed_name = data["message"].split('/')[-2]

    assert breed in breed_name

if __name__ == "__main__":
    pytest.main([__file__])