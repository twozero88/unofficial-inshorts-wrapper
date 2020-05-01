from flask import Flask
from inshorts import fetchNews,fetchFromCategroy
from flask_cors import cross_origin
import json

app = Flask(__name__)

@app.route('/<lang>/<category>/<number>')
@cross_origin()
def pageY(lang,category,number):
   return json.dumps(fetchNews(category,int(number),lang),ensure_ascii=False).encode('utf8')

@app.route('/topic/<lang>/<category>/<number>')
@cross_origin()
def pageZ(lang,category,number):
   return json.dumps(fetchFromCategroy(category,int(number),lang),ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
   app.run(port=80)