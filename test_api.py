import requests
input_text = "This is my sentence"
response = requests.get('http://simple-text-analyzer.appspot.com/analyze?text='+input_text)
print response.status_code
print response.content