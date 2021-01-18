import paramiko

class createSSHClient(object):
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password

    def connect(self):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.server, self.port, self.user, self.password)
            return client
        except paramiko.AuthenticationException:
            raise {"Error" : "Authentication Exception"}
        except paramiko.SSHExceptionas as ssherr:
            raise {"Error" : "SSH Error"}
        except paramiko.BadHostKeyException as hostkeyerr:
            raise {"Error" : "Host Key Error"}
    
    def close(self, client):
        return client.close()
