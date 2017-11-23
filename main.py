from flask import Flask, render_template, request, jsonify
import string

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome to Simple Text Analyzer - By Nitish'

@app.route('/analyze',methods=['GET','POST'])
def analyze():
	sta = {}
	text = request.args.get('text')
	print "Input Text = ",text

	## Remove punctuation and converting to lower case
	text_p = removePunctAndLower(text)
	print "Output Text = ",text_p

	## Counting number of words
	word_count = len(text_p.split(" "))

	## Filling the dictionary	
	sta['processed_text:'] = text_p
	sta['word_count:'] = word_count	
	print "Output JSON : ",sta
	
	return jsonify(sta)


def removePunctAndLower(text):
	# Removing punctuation and converting to lower case
	#line = None
	print "[removePunctAndLower] input = ",text
	for c in string.punctuation:
		text = text.replace(c," ")
	processed = text.lower()
	return processed