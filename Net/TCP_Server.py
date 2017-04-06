#Ctrl-Alt-F
import socket  # импортируем библиотеку для использование TCP 

socket_attr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - показывает, что мы работаем с сетевыми сокетами (есть еще локальные)
# SOCK_STREAM - указывает на то, что мы будет использовать сокет для работы с TCP
socket_attr.bind(('127.0.0.1', 1234)) # сокет связывается с адресом 
socket_attr.listen(10) # приём данных соединений на данном адресе (number - число очереди клиентов)
while True:
    conn, addr = socket_attr.accept() # возвращается, когда установлено новое соединение с пользователем
    # conn - сокет работы с конкретным клиентом
    # addr - ip адрес клиента
    while True:
        data = conn.recv(1024) # читает данные
        if not data: # если данных нет, выйти
            break
        conn.send(data) # отправка данных назад
    conn.close()