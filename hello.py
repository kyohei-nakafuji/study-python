import os,json
from bottle import route, run, request, response

@route("/")
def hello():
	return "hello"

@route('/search',method='GET')
def search():
#    userId = request.params('userId')
    body = json.dumps({'message': 'helloAjax'})
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(body)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#run(host="localhost", port=int(os.environ.get("PORT", 5000)))
