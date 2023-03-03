# coding=utf-8

from flask import Flask
from spyne.protocol.soap import Soap11
from spyne import Integer, Unicode, rpc, Application, Service
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from spyne.server.wsgi import WsgiApplication

app = Flask(__name__)

class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Unicode)
    def hello(self, name, times):
        return """<?xml version="1.0" encoding="utf-8"?><return><resultCode>0</resultCode><msg>111</msg></return>"""

class Test(Service):
    @rpc(Unicode, Integer, _returns=Unicode)
    def hello2(self, name, times):
        return "22222222222222"

def create_app():

    application = Application(
        [HelloWorldService], 'hello_world',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
    return application

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/hello': WsgiApplication(create_app()),
    '/hello2':WsgiApplication(Application(
        [Test], 'test',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    ))}
)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=50001)