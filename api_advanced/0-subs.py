#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
             or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'python3:0-subs:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response status code:", response.status_code)  # Add this line for debugging
    if response.status_code == 200:
        data = response.json().get('data')
        print("Data received:", data)  # Add this line for debugging
        subscribers = data.get('subscribers') if data else 0
        print("Number of subscribers:", subscribers)  # Add this line for debugging
        return subscribers
    else:
        print("Failed to fetch data from API")  # Add this line for debugging
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
