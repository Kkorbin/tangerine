#tctx.py
# this context class will take in a request and response and will be passed to the view function
# the response will start with a default of 404 not found and will be changed by the view function
# the request will be passed to the view function and the self.request will be updated with
# any necessary changes such as a change in auth status or a change in the path.

from typing import Callable
from socket import socket
from request import Request
from response import Response
from keychain import Keychain
from auth import Auth

class Ctx:
    def __init__(self, request: Request, response: Response, keychain: Keychain, auth: bool = False):
        self.request = request
        self.response = response
        self.keychain = keychain
        self.auth = auth

    def req_intercept(self, request: Request):
        self.request = request
        return self.request

    def res_intercept(self, response: Response):
        self.response = response
        return self.response

    def send(self, conn: socket):
        self.response.send(conn)

    def get_req_header(self, header: str):
        return self.request.headers.get(header)

    def set_res_header(self, header: str, value: str):
        self.response.headers[header] = value

    def set_auth(self, auth: bool):
        self.auth = auth

    # def view(self, view_func):
    #     view_func(self)

    def __repr__(self):
        return f'<Tctx: {self.request} {self.response}>'
