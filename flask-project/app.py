from flask import Flask,Response,jsonify
from soup import title_check
from title import notice_check
from title import notice_link

from flask_restful import Api, Resource
import requests 
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
api = Api(app)
# flask의 화면을 띄우기
@app.route('/tospring')
def hello():
    t=[]
    for i,title in enumerate(title_check()):
        t.append({'id':i,'title':title.decode('utf-8')})
    print(t)
    json_str = json.dumps(t,ensure_ascii=False)

    return  Response(json_str, content_type='application/json; charset=utf-8')

@app.route('/api', methods=['GET'])
def title():
    t=[]
    title_dict = {}
    for i,title in enumerate(title_check()):
        t.append({'id':i,'title':title.decode('utf-8')})
    print(t)
    title_dict["t"] = t
    #my_data = {'id': 'Alice', 'age': '30', 'title': 'New York'}
    return title_dict

@app.route('/notice')
def notice():
    t=[]
    title_dict = {}
    for i,title in enumerate(notice_link()):
        t.append({'id':i,'title':title})
    print(t)
    title_dict["t"] = t
    #my_data = {'id': 'Alice', 'age': '30', 'title': 'New York'}
    return title_dict


if __name__ == '__main__':
    app.run(debug=True, port='5000')
