import socketio

class Socket:
    socket = socketio.Client()

    @classmethod
    def connectServer(self):
        print("接続中")
        self.socket.connect('http://localhost:8080')

    def disconnectServer(self):
        self.socket.disconnect()