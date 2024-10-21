from threading import Thread
from wsgiref.simple_server import make_server
from select_name import select_func
from jinja2 import Template


def html():
    sele = select_func()
    with open('wsgiref_day1.html', 'r',encoding='utf-8') as f:
        data = f.read()
    tem = Template(data)
    data = tem.render({'userinfo':sele})
    # data = data.replace('time',sele['name'])
    data = data.encode('utf-8')
    return data


def css():
    with open('wsgiref_day1.css', 'rb') as f:
        data = f.read()
    return data


def js():
    with open('wsgiref_day1.js', 'rb') as f:
        data = f.read()
    return data


def ico():
    with open('jd.ico', 'rb') as f:
        data = f.read()
    return data


def application(environ, start_response):
    start_response('200 OK', [('k1', 'v1')])
    # print(environ)
    print(environ['PATH_INFO'])
    user_param = [('/', html), ('/wsgiref_day1.css', css), ('/jd.ico', ico), ('/wsgiref_day1.js', js)]
    for i in user_param:
        if environ['PATH_INFO'] == i[0]:
            t = Thread(target=i[1])
            t.start()
            # t.join()
            ret = i[1]()
    return [ret]


httpd = make_server('127.0.0.1', 9000, application)
httpd.serve_forever()
