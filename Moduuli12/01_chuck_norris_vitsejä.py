import requests

def get_random_chuck_norris_joke():
    chuck_norris_api_url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(chuck_norris_api_url)

    if response.status_code == 200:
        data = response.json()
        return data.get('value')
    else:
        return None


if __name__ == "__main__":
    joke = get_random_chuck_norris_joke()

    if joke:
        print(joke)
    else:
        print("Failed to fetch a Chuck Norris joke. Please try again later.")
