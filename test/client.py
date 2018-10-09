import canvasC
import socket
import threading

HOST = socket.gethostname()
PORT = 12341

# 클라이언트 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('연결..?')

# 서버와 연결
sock.connect((HOST, PORT))
print("서버와 연결이 되었다~~")

canvasT=canvasC.CanvasDemo(sock)

# 서브스레드 돌리기
t1=threading.Thread(target=canvasT.drawFromServer)
t1.daemon=True
t1.start()

canvasC.mainloop()
