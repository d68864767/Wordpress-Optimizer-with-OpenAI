```python
import requests
import json
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, EditPost

class WordPress_API:
    def __init__(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
            self.site_url = data['wordpress_site_url']
            self.username = data['wordpress_username']
            self.password = data['wordpress_password']
            self.post_limit = data['post_optimization_limit']
        self.client = Client(self.site_url, self.username, self.password)

    def get_posts(self):
        try:
            posts = self.client.call(GetPosts({'number': self.post_limit}))
            return posts
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def update_post(self, post_id, content):
        try:
            post = WordPressPost()
            post.content = content
            self.client.call(EditPost(post_id, post))
        except Exception as e:
            print(f"An error occurred: {e}")
```
