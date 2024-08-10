from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host="https://base.nirvanalabs.xyz/basemain-p44hd?apikey=ee9895eb7c874f9652ce5c22f96670ff899c"
    @task
    def eth_blockNumber(self):
        self.client.post("/",data='''
                        {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
                        ''')