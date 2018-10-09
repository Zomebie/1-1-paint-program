import canvas
import socket
import threading

HOST = socket.gethostname()
PORT = 12341

# 서버소켓 생성
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen(0)

c = None
canvasT=None

if c is None:
    print("[ ===> 연결 대기 중 <===]")
    c, addr = server_socket.accept()
    print("[ ===> ", addr, "연결 되었다! <===]")


    canvasT=canvas.CanvasDemo(c)

    # 서브스레드 돌리자
    t1=threading.Thread(target=canvasT.drawFromClient)

    t1.daemon=True
    t1.start()

    #캠퍼스 띄우기
    canvas.mainloop()











