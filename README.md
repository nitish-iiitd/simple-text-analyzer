# Simple Text Analyzer(STA) API 
This is a simple RESTful Web API for analyzing an english text.

### How to use STA in python
Just create a get request to the server with your text as parameter and get a JSON object in response. It's that simple !
```python
import requests
input_text = "This is my sentence"
response = requests.get('http://simple-text-analyzer.appspot.com/analyze?text='+input_text)
print "Status : ",response.status_code
print "Content : ",response.content
```

Output
```
Status :  200
Content :  {
  "processed_text:": "this is my sentence", 
  "word_count:": 4
}
```

