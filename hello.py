import os,json
from bottle import route, run, request, response, HTTPResponse

@route("/")
def hello():
	return "hello"

@route('/search',method='GET')
def search():
#    userId = request.params('userId')
    body = json.dumps([{'message':'helloAjax'}])
    response.status = 200
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
#    response.access_control_allow_origin = '*'
    
#    response.set_header('Access-Control-Allow-Origin','*')
#    response.add_header('Content-Type','application/json')
#    response.headers['Access-Control-Allow-Origin'] = '*'
#    response.headers['Content-Type'] = 'application/json'
#    r = HTTPResponse(status=200, body=body)
#    r.set_header("Content-Type", "application/json")
#    r.add_header("Access-Control-Allow-Origin","*")
#    return r
    return body

#run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
run(host="localhost", port=int(os.environ.get("PORT", 5000)))
