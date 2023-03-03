import os
import sys
import json
import time
import socket
import logging
#import requests
import multiprocessing
from spyne.protocol.soap import Soap11
from spyne import Integer, Unicode, rpc, Application, Service
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication

import process_frame as wiserelf
import my_process_test as MyTest
from flask import Flask

class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Unicode)
    def hello(self, name, times):
        return """<?xml version="1.0" encoding="utf-8"?><return><resultCode>0</resultCode><msg>111</msg></return>"""

class Test(Service):
    @rpc(Unicode, Integer, _returns=Unicode)
    def hello2(self, name, times):
        return "22222222222222"

class MyFlask(object):
    """:param
    """
    def __init__(self, app):
        self.app = app

    def w_init(self):
        self.app.wsgi_app = DispatcherMiddleware(self.app.wsgi_app, {
            '/hello': WsgiApplication(self.create_app()),
            '/hello2': WsgiApplication(self.test())})
        return self.app

    def create_app(self):
        application = Application(
            [HelloWorldService], 'hello_world',
            in_protocol=Soap11(validator='lxml'),
            out_protocol=Soap11(),
        )
        return application

    def test(self):
        application = Application(
            [Test], 'test',
            in_protocol=Soap11(validator='lxml'),
            out_protocol=Soap11(),
        )
        return application



w_flask = Flask(sys.argv[0].split("/")[-1].split(".")[0])
logging.getLogger("werkzeug").setLevel(logging.ERROR)
app = MyFlask(w_flask).w_init()



class WFlask(multiprocessing.Process):
    """:param
    """
    def __init__(self, wiser_elf):
        multiprocessing.Process.__init__(self)
        self.wiser_elf = wiser_elf

    def run(self):
        app.run(host="127.0.0.1", port=8887)




if __name__ == '__main__':
    all_args = wiserelf.WiserElf.init_all_args_var()
    wiserelf.WiserElf.add_cmd_help_msg("input [list] to show all cmd line~", all_args)
    wiserelf.WiserElf.add_cmd_config_group_to_args({
        "show statistic": {},
        "set traceback switch": {},
    }, all_args)

    wiserelf.WiserElf.add_cmd_config_for_toml_group_to_args({}, all_args)
    wiserelf.WiserElf.add_static_config_group_to_args({
        "policy_backup_file": "",
        "token_map_backup_file": "",
        "time_point_file": "",
        "failed_send_file": ""
    }, all_args)
    wiserelf.WiserElf.add_global_config_group_to_args({
        "fpga_dev_map": {}
    }, all_args)

    wiserelf.WiserElf.add_process_fifo_group_to_args({
        "->[TimeManager]": None,
        "->[MysqlKeeper]": None,
    }, all_args)
    wiserelf.WiserElf.add_statistical_group_to_args({
        "POLICY_MANAGER_START_TIMES": 1,
    }, all_args)

    wiserelf.WiserElf.add_init_function_dict_to_args({}, all_args)
    wiserelf.WiserElf.add_start_function_dict_to_args({}, all_args)
    wiserelf.WiserElf.add_run_function_dict_to_args({}, all_args)
    wiserelf.WiserElf.add_stop_function_dict_to_args({}, all_args)
    wiserelf.WiserElf.add_clean_function_dict_to_args({}, all_args)

    wiserelf.WiserElf.add_process_group_to_args({
        "MyTest": MyTest.Mytest,
        "WFlask": WFlask,
    }, all_args)
    wiserelf.start_shadow("local", all_args)