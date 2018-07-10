import base64
class account:
    def __init__(self,username,password):
        self.username = username;
        self.password = base64.decode(password)
        