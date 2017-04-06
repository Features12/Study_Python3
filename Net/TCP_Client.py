#Ctrl-Alt-F
import socket # импортируем библиотеку для использование TCP 


message = b"Hello TCP!" # текст сообщение
socket_attr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# AF_INET - показывает, что мы работаем с сетевыми сокетами (есть еще локальные)
# SOCK_STREAM - указывает на то, что мы будет использовать сокет для работы с TCP
socket_attr.connect(('127.0.0.1', 1234)) # подключение к сокету('ip', port)
# если не было ошибки, то соединение установлено!
socket_attr.send(message) # отправление данных
rsp_answer = socket_attr.recv(1024) # получение данных (число сколько данных нам надо получить)
socket_attr.close()