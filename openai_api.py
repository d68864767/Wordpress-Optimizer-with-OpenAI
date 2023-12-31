```python
import openai
import json

class OpenAI_API:
    def __init__(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
            self.api_key = data['openai_api_key']
        openai.api_key = self.api_key

    def optimize_content(self, content):
        try:
            response = openai.Completion.create(
              engine="text-davinci-002",
              prompt=content,
              temperature=0.5,
              max_tokens=100
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
```
