from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
dispatcher = Dispatcher()

# def eda_handler(address, *args):
#     print(f"Received EDA data: {args}")

# dispatcher.map("/EmotiBit/0/EDA", eda_handler)

server = BlockingOSCUDPServer(("127.0.0.1", 12345), dispatcher)