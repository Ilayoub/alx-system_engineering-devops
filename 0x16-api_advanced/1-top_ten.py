#!/usr/bin/python3
"""
The function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top ten hot posts."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Chrome'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            hot_posts = data.get('data', {}).get('children', [])
            for post in hot_posts[:11]:
                title = post['data']['title']
                print(title)
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
