from random import *
from tkinter import *

width=1
color = "black"

# 서버 그림판
class CanvasDemo:

    c = None

    def __init__(self,c):  # 생성자

        self.c=c
        window = Tk()
        window.title("Server")
        window.geometry("640x400")  # 가로 X 세로 + X + Y
        window.resizable(True, True)
        window.configure(background="white")

        # 윈도우 창에 캔버스 배치한다.
        self.canvas = Canvas(window, relief="groove", bd=2)
        self.canvas.pack(expand=True, fill="both")

        # 프레임에 버튼을 배치한다.
        frame = Frame(window)
        frame.pack()

        # 버튼이름 및 클릭이벤트처리
        btRectangle = Button(frame, text="Rectangle", command=self.displayRect)
        btOval = Button(frame, text="Oval", command=self.displayOval)
        btArc = Button(frame, text="Arc", command=self.displayArc)
        btPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
        btClear = Button(frame, text="Clear", command=self.clearCanvas)
        btSn = Button(frame, text=str(width))

        # 버튼 색상
        btred = Button(frame, width=2, command=self.red, background="red")
        btorange = Button(frame, width=2, command=self.orange, background="orange")
        btyellow = Button(frame, width=2, command=self.yellow, background="yellow")
        btblue = Button(frame, width=2, command=self.blue, background="blue")
        btgreen = Button(frame, width=2, command=self.green, background="green")
        btpurple = Button(frame, width=2, command=self.purple, background="purple")
        btblack = Button(frame, width=2, command=self.black, background="black")

        # 버튼순서
        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btClear.grid(row=1, column=5)
        btSn.grid(row=1, column=6)

        btred.grid(row=1, column=7)
        btorange.grid(row=1, column=8)
        btyellow.grid(row=1, column=9)
        btblue.grid(row=1, column=10)
        btgreen.grid(row=1, column=11)
        btpurple.grid(row=1, column=12)
        btblack.grid(row=1, column=13)

        # 그리기 함수들
        def Draw(event):

            global x0, y0
            tx0 = str(x0)
            if len(tx0) == 2:
                tx0 += ' '

            ty0 = str(y0)
            if len(ty0) == 2:
                ty0 += ' '
                print(len(ty0))

            print("global:", x0, y0)

            tex0 = str(event.x)
            if len(tex0) == 2:
                tex0 += ' '

            tey0 = str(event.y)
            if len(tey0) == 2:
                tey0 += ' '


            print("event :", event.x, event.y)
            self.canvas.create_line(x0, y0, event.x, event.y, fill=color, width=width, tags="line")

            # 이벤트 값 서버로 보내기
            c.send(tx0.encode())
            c.send(ty0.encode())
            c.send(tex0.encode())
            c.send(tey0.encode())

            x0, y0 = event.x, event.y

        def down(event):
            global x0, y0
            x0, y0 = event.x, event.y

        def up(event):
            global x0, y0
            if (x0, y0) == (event.x, event.y):
                self.canvas.create_line(x0, y0, x0 + 1, y0 + 1)

        # 지우기
        def Eraser(event):
            global x0, y0
            self.canvas.create_rectangle(x0, y0, event.x, event.y, width=30, outline="#f0f0f0")
            x0, y0 = event.x, event.y

        # 펜 크기조절
        def scroll(event):
            global width
            if event.delta == 120:
                width += 1
            if event.delta == -120:
                width -= 1
            btSn.config(text=str(width))

        self.canvas.bind("<B1-Motion>", Draw)  # 왼쪽마우스 버튼을 누르면서 움직일때
        self.canvas.bind("<Button-1>", down)
        self.canvas.bind("<ButtonRelease-1>", up)
        self.canvas.bind("<B3-Motion>", Eraser)  # 오른쪽마우스 버튼을 누르면서 움직일때
        self.canvas.bind("<MouseWheel>", scroll)  # 마우스 휠 이동

    # 클라이언트에서 그린 그림 그리기
    def drawFromClient(self):

        global x0, y0

        print("drawFromClient")
        while True:
            x0 = int(self.c.recv(3).decode())
            y0 = int(self.c.recv(3).decode())
            eventx = int(self.c.recv(3).decode())
            eventy = int(self.c.recv(3).decode())

            print("global: ", x0, y0)
            print("event: ", eventx, eventy)
            self.canvas.create_line(x0, y0, eventx, eventy, fill=color, width=width, tags="line")
            x0, y0 = eventx, eventy


    # 도형 그리기
    def displayRect(self):
        x1 = randint(1, 1980)
        y1 = randint(1, 1080)
        x2 = randint(1, 60)
        y2 = randint(1, 60)
        self.canvas.create_rectangle(x1, y1, x2, y2, tags="rect")  # 위치, 위치, 가로, 세로

    def displayOval(self):
        x = randint(1, 640)
        y = randint(1, 400)
        self.canvas.create_oval(x, y, 190, 90, tags="oval")  # 위치, 위치, 가로, 세로

    def displayArc(self):
        x = randint(1, 640)
        y = randint(1, 400)
        self.canvas.create_arc(x, y, 190, 90, start=0, extent=90, width=2, tags="arc")  # 위치, 위치, 가로, 세로

    def displayPolygon(self):
        x = randint(1, 640)
        y = randint(1, 400)
        self.canvas.create_polygon(x, y, 190, 90, 30, 50, tags="polygon")  # 위치, 위치, 가로, 세로

    def clearCanvas(self):
        x = randint(1, 640)
        y = randint(1, 400)
        self.canvas.delete("rect", "oval", "arc", "polygon", "line")

    # 펜 색상 변경
    def red(self):
        global color
        color = "red"

    def orange(self):
        global color
        color = "orange"

    def yellow(self):
        global color
        color = "yellow"

    def green(self):
        global color
        color = "green"

    def blue(self):
        global color
        color = "blue"

    def purple(self):
        global color
        color = "purple"

    def black(self):
        global color
        color = "black"

