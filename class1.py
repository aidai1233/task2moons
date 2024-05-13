class Hello:
    def __init__(self, str):
        self.str = str

from art import tprint
class NewHello(Hello):
    def tptint(self):
        tprint(self.str)