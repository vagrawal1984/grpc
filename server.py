import grpc
from concurrent import futures
import time
import calculator_pb2
import calculator_pb2_grpc

import pgrpc

class CalculatorServicer(calculator_pb2_grpc.calculatorServicer):

    def SquareRoot(self, request, context):
        response =calculator_pb2.Number()
        response.value = pgrpc.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_calculatorServicer_to_server(CalculatorServicer(), server)

print("Started Listning on port 50051")
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
