"""
    An example of a simple RPC worker
    Run as follows:


        from browser import webworker as ww
        from asyncio import coroutine

        @coroutine
        def main(w):
            yield w.wait_for_status(ww.S_RUNNING)
            a = yield w.add(10,20)
            assert a == 30
            yield w.log("Test output")

        w = ww.RPCWorkerParent('web_workers/test_rpc.py',[1,2,3],{"USER":"nobody"})
        main(w)

"""
from browser.webworker import current_worker, Message
from browser import console

from sys import argv
from os import environ


def add(x, y):
    """Adds two numbers"""
    return x + y


def log(*args):
    print(*args)


def pong(self, message, **_):
    print('Web worker received message (', message.id, ')', message.name, message.data)
    current_worker.post_reply(message, Message('pong', message.data))


def quiting(self, *args, **kwargs):
    current_worker.terminate()


print("Starting test RPC worker with args:", argv, "and environment", environ)

current_worker.register_method(add)
current_worker.register_method(log)
current_worker.exec()


current_worker.bind_message('ping', pong)
current_worker.bind_message('quit', quiting)
current_worker.exec()
