import grpc

import calculator_pb2_grpc
import calculator_pb2

channel = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.calculatorStub(channel)

number = calculator_pb2.Number(value=125)

response = stub.SquareRoot(number)

print(response.value)