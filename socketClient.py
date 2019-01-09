import socketio


class Socket:
    socket = socketio.Client()

    @classmethod
    def connect_server(cls):
        print("接続中")
        cls.socket.connect('http://localhost:8080')

    @classmethod
    def disconnect_server(cls):
        cls.socket.disconnect()
