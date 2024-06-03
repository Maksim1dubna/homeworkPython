from multiprocessing import Process

class WarehouseManager():
    def __init__(self):
        super(WarehouseManager, self).__init__()
        self.data = {}
    def process_request(self, request):
        for i in range(len(request)):
            if "receipt" in request[i]:
                self.data[request[i][0]] = request[i][2]
            elif ("shipment" in request[i]) and self.data[request[i][0]]>0:
                self.data[f"{request[i][0]}"] = self.data[f"{request[i][0]}"] - request[i][2]
        print(self.data)
if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)]
    manager = Process(target = manager.process_request(requests))
    manager.run()

