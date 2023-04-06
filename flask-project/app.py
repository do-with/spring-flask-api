from flask import Flask,Response,jsonify
from soup import title_check
from title import notice_check

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
    Title=[]
    title_dict = {}
    for i,title in enumerate(title_check()):
        Title.append({'id':i,'title':title.decode('utf-8')})
    print(Title)
    title_dict["Notices"] = Title
    return title_dict

@app.route('/img', methods=['GET'])
def noticeImg():
    URL=[]
    url_dict = {}
    
    decode_list = []
    #for i,url in enumerate(notice_check()):
        #URL.append({'id':i,'url':url[i]})
    for content in notice_check():
        decode_dict = {}
        decode_dict['src'] = content['src'].decode('utf-8')
        decode_dict['title'] = content['title'].decode('utf-8')
        decode_dict['content'] = content['content'].decode('utf-8')
        decode_list.append(decode_dict)

    for i,content in enumerate(decode_list):
        URL.append({"id":i ,"Contents":content})
    print(URL)
    url_dict["News"] = URL
    #my_data = {'id': 'Alice', 'age': '30', 'title': 'New York'}
    print(url_dict)
    return url_dict


if __name__ == '__main__':
    app.run(debug=True, port='5000')
