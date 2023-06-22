import socket
HOST = '10.2.53.209'
PORT = 2000

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        
        print('started server on', HOST, PORT)
        print('The Web server URL for this would be http://%s:%d/' % (HOST, PORT))
        
        while True:
            print('working...')
            client_socket, adress = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('shutdown')

def load_page_from_get_request(req):
    # HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    # # HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    # # path = req.split(' ')[1]
    # response = ''
    # # try:
    # with open('./index.html', 'rb') as file :
    #     response = file.read()
    # return HDRS.encode('utf-8') + response
    # # except FileNotFoundError:
    # #     return (HDRS_404 + '404 Page not found').encode('utf-8')

    return req.encode('utf-8')

if __name__ == '__main__':
    start_server()