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
            if dat["type"] == "PushEvent":
                print(f"Pushed commits in {dat['repo']['name']}")

            elif dat["type"] == "CreateEvent":
                print(f"Create event in {dat['repo']['name']}")

            elif dat["type"] == "DeleteEvent":
                print(f"Delete event in {dat['repo']['name']}")

            elif dat["type"] == "WatchEvent":
                print(f"Watch event in {dat['repo']['name']}")

            elif dat["type"] == "ForkEvent":
                print(f"Fork event in {dat['repo']['name']}")

            elif dat["type"] == "IssuesEvent":
                print(f"Issue event in {dat['repo']['name']}")

            elif dat["type"] == "IssueCommentEvent":
                print(f"Issue comment in {dat['repo']['name']}")

            elif dat["type"] == "PullRequestEvent":
                print(f"Pull request in {dat['repo']['name']}")

            elif dat["type"] == "ReleaseEvent":
                print(f"Release event in {dat['repo']['name']}")
        
    elif response.status_code == 404:
        print(f"User Not Found")

    else:
        print(f"Error {response.status_code}")

github_activity()