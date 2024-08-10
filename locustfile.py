from locust import HttpUser, task

class web3User(HttpUser):
    host="https://arbitrum.blockpi.network/v1/rpc/49bb93bdb999e4b849bd0b52794671c145aa3a9b"
    @task
    def hello_world(self):
        self.client.post("/",data='''
                        {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
                        ''')