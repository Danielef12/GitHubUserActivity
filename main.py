import requests
import argparse


def get_github_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Error Unknown')}")
        return None


def analyze_events(events):
    event_summary = {}

    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        # Contiamo i tipi di eventi
        if event_type not in event_summary:
            event_summary[event_type] = {"count": 0, "repos": set()}

        event_summary[event_type]["count"] += 1
        event_summary[event_type]["repos"].add(repo_name)

    return event_summary


def display_summary(summary):
    print("\n- User Activity:")
    for event_type, data in summary.items():
        print(f"\n  - {event_type} ({data['count']} event)")
        for repo in data["repos"]:
            print(f"   - {repo}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display the activity of a GitHub User")
    parser.add_argument("username", type=str, help="Username of github user")
    args = parser.parse_args()
    username = args.username
    events = get_github_events(username)
    if events:
        summary = analyze_events(events)
        display_summary(summary)
    else:
        print("Events not found")
