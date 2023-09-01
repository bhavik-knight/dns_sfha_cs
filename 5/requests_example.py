import json
import sys

import pandas as pd
import requests


def main():
    # get 10 random user's data
    number_of_users = 10

    # website url to make API calls
    url = "https://randomuser.me/api/"
    parsed_url = f"{url}?results={number_of_users}"

    # connect to the api
    response = connect_api(parsed_url)

    if response.status_code != 200:
        sys.exit(f"Sorry! Couldn't connect to the website. Error: {response.status_code}")

    # get users data
    users = get_data(response)
    print(users)


def connect_api(url):
    response = requests.get(url)
    return response


def get_data(response) -> list:
    users_data = json.loads(response.content).get("results")
    users = list()
    for user in users_data:
        r = dict()
        r["name"] = f'{user["name"]["first"]} {user["name"]["last"]}'
        r["email"] = f'{user["email"]}'
        r["country"] = f'{user["location"]["country"]}'
        r["phone"] = f'{user["cell"]}'
        users.append(r)
    return pd.DataFrame(users)


if __name__ == "__main__":
    main()
