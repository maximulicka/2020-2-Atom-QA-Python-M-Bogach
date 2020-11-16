import socket
import json
import settings


class SocketClient:
    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port
        # создаём объект клиентского сокета
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # выставляем ожидание для сокета
        self.client.settimeout(0.2)

    def connection(self):
        # устанавливаем соединение
        self.client.connect((self.target_host, self.target_port))

    def response(self):
        total_data = []
        while True:
            # читаем данные из сокета до тех пор пока они там есть
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        return json.loads(data[-1])[0]

    def post_request(self, params, headers, data):
        self.connection()
        dict_headers = "\r\n".join([f"{header[0]}: {header[1]}" for header in headers])
        request = (f'POST {params} HTTP/1.1\r\n'
                   f'{dict_headers}: \r\n'
                   f'Content-Length: {str(len(data))}\r\n\r\n{data}')
        self.client.send(request.encode())
        return self.response()


if __name__ == '__main__':
    client = SocketClient(host=settings.APP_HOST, port=settings.APP_PORT)
    r = client.post_request(params='/', headers=[("Host", f"{settings.APP_HOST}")], data=json.dumps({"user": 'bogach'}))
    print(r)
