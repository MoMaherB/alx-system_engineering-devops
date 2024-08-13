#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response was successful
        if response.status_code != 200:
            return 0

        # Parse the response JSON
        try:
            data = response.json()
        except ValueError:
            # If JSON parsing fails, print error and return 0
            print("Error: Unable to parse JSON response")
            return 0

        # Check if 'data' and 'subscribers' exist in the response
        results = data.get("data", {})
        return results.get("subscribers", 0)
    except requests.RequestException as e:
        # Catch all other requests exceptions
        print(f"Error: {e}")
        return 0
