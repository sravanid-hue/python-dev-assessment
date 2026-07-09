import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected JSON structure")
            return None

        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"City: {city}")
                print("-" * 30)

            except KeyError:
                print("Error: Missing user information")
                return None

        return users[:num_users]

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
        return None

    except ValueError:
        print("Error: Invalid JSON response")
        return None


# Example usage
fetch_and_display_users(3)