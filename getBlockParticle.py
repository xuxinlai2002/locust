from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host="https://rpc.particle.network/evm-chain?chainId=42161&projectUuid=ca816894-16b8-4d56-9633-75be42229667&projectKey=crL2Oiekos42N3h663QkeagGqhxP7uiN5BEvzpdx"
    @task
    def eth_blockNumber(self):
        self.client.post("/",data='''
                        {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
                        ''')