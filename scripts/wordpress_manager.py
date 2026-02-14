import requests
from requests.auth import HTTPBasicAuth
import json
import sys

class WordPressManager:
    def __init__(self, base_url, username, app_password):
        self.base_url = base_url.rstrip('/')
        self.auth = HTTPBasicAuth(username, app_password)
        self.api_url = f"{self.base_url}/wp-json/wp/v2"

    def test_connection(self):
        try:
            response = requests.get(f"{self.base_url}/wp-json", auth=self.auth)
            if response.status_code == 200:
                site_info = response.json()
                return f"Connected to: {site_info.get('name')} - {site_info.get('description')}"
            else:
                return f"Failed to connect. Status Code: {response.status_code}, Response: {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

    def list_posts(self, per_page=5):
        try:
            response = requests.get(f"{self.api_url}/posts", auth=self.auth, params={"per_page": per_page})
            if response.status_code == 200:
                posts = response.json()
                result = []
                for post in posts:
                    result.append(f"- {post['title']['rendered']} (ID: {post['id']})")
                return "\n".join(result)
            else:
                return f"Failed to fetch posts. Status: {response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    # For now, we test with a default username 'manrahul' - Boss can correct if needed
    manager = WordPressManager("https://www.manrahul.in/", "manrahul", "N2Ea KqZV 0KBU fwuz 1VLj kPHz")
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "test":
            print(manager.test_connection())
        elif action == "list":
            print(manager.list_posts())
    else:
        print("Usage: python3 wordpress_manager.py [test|list]")
