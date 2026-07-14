import requests
import argparse

def github_activity():

    parser = argparse.ArgumentParser(description="Github User Activity CLI")
    
    parser.add_argument("username")

    args = parser.parse_args()

    github_username = args.username
    url = f"https://api.github.com/users/{github_username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for dat in data:
            print(f"{dat['actor']['login']}")
            print(f"{dat['type']}")
            print(f"{dat['repo']['name']}")
            print(f"{dat['created_at']}")
        
    elif response.status_code == 404:
        print("Error 404")

    else:
        print(":( You encounter some issue)")

github_activity()