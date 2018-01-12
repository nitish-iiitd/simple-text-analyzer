# Simple Text Analyzer(STA) API 
This is a simple RESTful Web API for analyzing an english text.
Just create a get request to the server with your text as parameter and get a JSON object in response. 
It's that simple !

### How to use STA in Python
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

### How to use STA in Java
```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class Use_STA {
	public static void main(String[] args) throws IOException {
		String requestsent = "http://simple-text-analyzer.appspot.com/analyze?text=hello";
		URL sta = new URL(requestsent);
        URLConnection sta_con = sta.openConnection();
        BufferedReader in = new BufferedReader(new InputStreamReader(sta_con.getInputStream()));
        String inputLine;
        while ((inputLine = in.readLine()) != null) 
            System.out.println(inputLine);
        in.close();
	}
}
```

