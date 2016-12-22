# -*- coding: utf-8 -*-

import os,json
from bottle import route, run, request, response, HTTPResponse
from time import sleep

@route("/")
def hello():
	return "hello"

@route('/search',method=['OPTIONS'])
def search():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    return {}

@route('/search',method=['GET','POST'])
def search():
    data = request.json
    list= [
        {'id':'1','name':u'佐藤','kana':u'サトウ'},
        {'id':'2','name':u'田中','kana':u'タナカ'},
        {'id':'3','name':u'鈴木','kana':u'スズキ'},
        {'id':'4','name':u'斎藤','kana':u'サイトウ'},
        {'id':'5','name':u'高橋','kana':u'タカハシ'},
        {'id':'6','name':u'伊藤','kana':u'イトウ'},
        {'id':'7','name':u'渡辺','kana':u'ワタナベ'},
        {'id':'8','name':u'山本','kana':u'ヤマモト'},
        {'id':'9','name':u'中村','kana':u'ナカムラ'}
    ]

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Content-Type'] = 'application/json'

    if data is None:
        body = json.dumps(list)
    else:
        searchWord = data['searchWord']
        count = len(list)
        for i in range(len(list)):
            if list[count - i - 1]['kana'].find(searchWord)==-1:
                del list[count - i - 1]
        body = json.dumps(list)

    sleep(5)
    return body

@route('/search2',method=['OPTIONS'])
def search():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    return {}

@route('/search2',method=['GET','POST'])
def search():
    data = request.json
    list= [
        {'id':'1','name':u'佐藤','kana':u'サトウ'},
        {'id':'2','name':u'田中','kana':u'タナカ'},
        {'id':'3','name':u'鈴木','kana':u'スズキ'},
        {'id':'4','name':u'斎藤','kana':u'サイトウ'},
        {'id':'5','name':u'高橋','kana':u'タカハシ'},
        {'id':'6','name':u'伊藤','kana':u'イトウ'},
        {'id':'7','name':u'渡辺','kana':u'ワタナベ'},
        {'id':'8','name':u'山本','kana':u'ヤマモト'},
        {'id':'9','name':u'中村','kana':u'ナカムラ'}
    ]

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Content-Type'] = 'application/json'

    if data is None:
        body = json.dumps(list)
    else:
        searchWord = data['searchWord']
        count = len(list)
        for i in range(len(list)):
            if list[count - i - 1]['kana'].find(searchWord)==-1:
                del list[count - i - 1]
        body = json.dumps(list)

    return body


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#run(host="localhost", port=int(os.environ.get("PORT", 5000)))
