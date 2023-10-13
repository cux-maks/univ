import math
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
from circularbuffer import CircularBuffer
from producer import Producer
from consumer import Consumer

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.visible_mode = "home"
        self.initUI()
        self.bufferSize = 0
        self.circularbuffer = CircularBuffer(1)
        self.producerCnt = 0
        self.consumerCnt = 0

    def initUI(self):

        # window 설정
        self.setFixedSize(1152, 720)
        self.setStyleSheet("background-color: #FFF8EA;")

        # title: PCP
        font_title = QFont("Arial", 100)
        self.title = QLabel("PCP", self)
        self.title.setFont(font_title)
        self.title.adjustSize()
        self.title.move(439, 150)

        # subtitle: Producer and Consumer Problem
        font_subtitle = QFont("Arial", 17)
        self.subtitle = QLabel("Producer and Consumer Problem", self)
        self.subtitle.setFont(font_subtitle)
        self.subtitle.adjustSize()
        self.subtitle.move(398, 301)

        # startbtn
        font_startbtn = QFont("Arial", 20)
        self.startbtn = QPushButton("START", self)
        self.startbtn.setFont(font_startbtn)
        self.startbtn.setStyleSheet("""
            QPushButton{
                background-color: #9E7676;
                border-radius: 5px;
            }
            QPushButton:hover{
                background-color: #815B5B;
            }
            """)
        self.startbtn.setFixedSize(120, 50)
        self.startbtn.move(516, 350)
        self.startbtn.clicked.connect(self.click_startbtn)

        # backbtn
        font_backbtn = QFont("Arial", 15)
        self.backbtn = QPushButton("back", self)
        self.backbtn.setFont(font_backbtn)
        self.backbtn.setStyleSheet("""
            QPushButton{
                background-color: #9E7676;
                border-radius: 5px;
            }
            QPushButton:hover{
                background-color: #815B5B;
            }
            """)
        self.backbtn.setFixedSize(50, 30)
        self.backbtn.move(521, 650)
        self.backbtn.clicked.connect(self.click_backbtn)
        self.backbtn.setVisible(False)

        # nextbtn
        font_nextbtn = QFont("Arial", 15)
        self.nextbtn = QPushButton("next", self)
        self.nextbtn.setFont(font_nextbtn)
        self.nextbtn.setStyleSheet("""
            QPushButton{
                background-color: #9E7676;
                border-radius: 5px;
            }
            QPushButton:hover{
                background-color: #815B5B;
            }
            """)
        self.nextbtn.setFixedSize(50, 30)
        self.nextbtn.move(581, 650)
        self.nextbtn.clicked.connect(self.click_nextbtn)
        self.nextbtn.setVisible(False)

        # circularbuffer size label
        font_settings_label = QFont("Arial", 20)
        self.settings_label = QLabel("Check circular buffer size", self)
        self.settings_label.setFont(font_settings_label)
        self.settings_label.adjustSize()
        self.settings_label.move(110, 200)
        self.settings_label.setVisible(False)

        # check_box 4 ~ 12
        self.check_size_list = []
        for i in range(9):
            buf = QRadioButton(f"{i + 4}", self)
            buf.setStyleSheet("font-size: 20px;")
            buf.move(120 + i * 100, 300)
            buf.setVisible(False)
            self.check_size_list.append(buf)

        # circularbuffer items label 4 ~ 12
        self.circularbuffer_items = []
        
        # mutexP
        font_mutexP = QFont("Arial", 10)
        self.mutexP = QLabel("mutexP", self)
        self.mutexP.setFont(font_mutexP)
        self.mutexP.adjustSize()
        self.mutexP.move(420, 400)
        self.mutexP.setVisible(False)

        # mutexP value
        font_mutexPval = QFont("Arial", 20)
        self.mutexPval = QLabel("None", self)
        self.mutexPval.setFont(font_mutexPval)
        self.mutexPval.setStyleSheet("border: 1px solid black;")
        self.mutexPval.setFixedSize(80, 40)
        self.mutexPval.move(400, 420)
        self.mutexPval.setVisible(False)

        # mutexP queue
        self.mutexPqueue = []
        for i in range(5):
            font_buf = QFont("Arial", 10)
            buf = QLabel("None", self)
            buf.setFont(font_buf)
            buf.setFixedSize(60, 40)
            buf.move(340 - i * 70, 420)
            buf.setVisible(False)
            self.mutexPqueue.append(buf)

        # mutexC
        font_mutexC = QFont("Arial", 10)
        self.mutexC = QLabel("mutexC", self)
        self.mutexC.setFont(font_mutexC)
        self.mutexC.adjustSize()
        self.mutexC.move(697, 400)
        self.mutexC.setVisible(False)

        # mutexC value
        font_mutexCval = QFont("Arial", 20)
        self.mutexCval = QLabel("None", self)
        self.mutexCval.setFont(font_mutexCval)
        self.mutexCval.setStyleSheet("border: 1px solid black;")
        self.mutexCval.setFixedSize(80, 40)
        self.mutexCval.move(677, 420)
        self.mutexCval.setVisible(False)

        # mutexC queue
        self.mutexCqueue = []
        for i in range(5):
            font_buf = QFont("Arial", 10)
            buf = QLabel("None", self)
            buf.setFont(font_buf)
            buf.setFixedSize(60, 40)
            buf.move(817 + i * 70, 420)
            buf.setVisible(False)
            self.mutexCqueue.append(buf)

        # nrfull
        font_nrfull = QFont("Arial", 10)
        self.nrfull = QLabel("nrfull", self)
        self.nrfull.setFont(font_nrfull)
        self.nrfull.adjustSize()
        self.nrfull.move(425, 500)
        self.nrfull.setVisible(False)

        # nrfull value
        font_nrfullval = QFont("Arial", 20)
        self.nrfullval = QLabel("None", self)
        self.nrfullval.setFont(font_nrfullval)
        self.nrfullval.setStyleSheet("border: 1px solid black;")
        self.nrfullval.setFixedSize(80, 40)
        self.nrfullval.move(400, 520)
        self.nrfullval.setVisible(False)

        # nrfull queue
        self.nrfullqueue = []
        for i in range(5):
            font_buf = QFont("Arial", 10)
            buf = QLabel("None", self)
            buf.setFont(font_buf)
            buf.setFixedSize(60, 40)
            buf.move(340 - i * 70, 520)
            buf.setVisible(False)
            self.nrfullqueue.append(buf)

        # nrempty
        font_nrempty = QFont("Arial", 10)
        self.nrempty = QLabel("nrempty", self)
        self.nrempty.setFont(font_nrempty)
        self.nrempty.adjustSize()
        self.nrempty.move(697, 500)
        self.nrempty.setVisible(False)

        # nrempty value
        font_nremptyval = QFont("Arial", 20)
        self.nremptyval = QLabel("None", self)
        self.nremptyval.setFont(font_nremptyval)
        self.nremptyval.setStyleSheet("border: 1px solid black;")
        self.nremptyval.setFixedSize(80, 40)
        self.nremptyval.move(677, 520)
        self.nremptyval.setVisible(False)

        # nrempty queue
        self.nremptyqueue = []
        for i in range(5):
            font_buf = QFont("Arial", 10)
            buf = QLabel("None", self)
            buf.setFont(font_buf)
            buf.setFixedSize(60, 40)
            buf.move(817 + i * 70, 520)
            buf.setVisible(False)
            self.nremptyqueue.append(buf)

        # in
        font_in_title = QFont("Arial", 10)
        self.in_title = QLabel("in", self)
        self.in_title.setFont(font_in_title)
        self.in_title.adjustSize()
        self.in_title.move(202, 180)
        self.in_title.setVisible(False)
        font_in = QFont("Arial", 20)
        self.inidx = QLabel("None", self)
        self.inidx.setFont(font_in)
        self.inidx.adjustSize()
        self.inidx.move(200, 200)
        self.inidx.setVisible(False)

        # out
        font_out_title = QFont("Arial", 10)
        self.out_title = QLabel("out", self)
        self.out_title.setFont(font_out_title)
        self.out_title.adjustSize()
        self.out_title.move(898, 180)
        self.out_title.setVisible(False)
        font_out = QFont("Arial", 20)
        self.outidx = QLabel("None", self)
        self.outidx.setFont(font_out)
        self.outidx.adjustSize()
        self.outidx.move(900, 200)
        self.outidx.setVisible(False)

        # producer btn
        font_producerbtn = QFont("Arial", 15)
        self.producerbtn = QPushButton("Producer", self)
        self.producerbtn.setFont(font_producerbtn)
        self.producerbtn.setStyleSheet("""
            QPushButton{
                background-color: #9E7676;
                border-radius: 5px;
            }
            QPushButton:hover{
                background-color: #815B5B;
            }
            """)
        self.producerbtn.setFixedSize(100, 50)
        self.producerbtn.move(526, 415)
        self.producerbtn.clicked.connect(self.click_producerbtn)
        self.producerbtn.setVisible(False)

        # consumer btn
        font_consumerbtn = QFont("Arial", 15)
        self.consumerbtn = QPushButton("Consumer", self)
        self.consumerbtn.setFont(font_consumerbtn)
        self.consumerbtn.setStyleSheet("""
            QPushButton{
                background-color: #9E7676;
                border-radius: 5px;
            }
            QPushButton:hover{
                background-color: #815B5B;
            }
            """)
        self.consumerbtn.setFixedSize(100, 50)
        self.consumerbtn.move(526, 515)
        self.consumerbtn.clicked.connect(self.click_consumerbtn)
        self.consumerbtn.setVisible(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateUI)
        self.timer.start(100)  # 0.1초마다 UI 업데이트
        self.setWindowTitle('Producer and Consumer Problem Simulation: 2021136124 조병하')
        self.show()

    def updateUI(self):
        if self.visible_mode == "home":
            self.title.setVisible(True)
            self.subtitle.setVisible(True)
            self.startbtn.setVisible(True)
            self.backbtn.setVisible(False)
            self.nextbtn.setVisible(False)
            self.settings_label.setVisible(False)
            for x in self.check_size_list: x.setVisible(False)
        elif self.visible_mode == "settings":
            self.title.setVisible(False)
            self.subtitle.setVisible(False)
            self.startbtn.setVisible(False)
            self.backbtn.setVisible(True)
            self.nextbtn.setVisible(True)
            self.settings_label.setVisible(True)
            self.mutexPval.setVisible(False)
            self.mutexCval.setVisible(False)
            self.mutexP.setVisible(False)
            self.mutexC.setVisible(False)
            self.nrfull.setVisible(False)
            self.nrfullval.setVisible(False)
            self.nrempty.setVisible(False)
            self.nremptyval.setVisible(False)
            self.producerbtn.setVisible(False)
            self.consumerbtn.setVisible(False)
            self.inidx.setVisible(False)
            self.outidx.setVisible(False)
            self.in_title.setVisible(False)
            self.out_title.setVisible(False)
            for x in self.check_size_list: x.setVisible(True)
            for x in self.circularbuffer_items: x.setVisible(False)
            for x in self.mutexPqueue: x.setVisible(False)
            for x in self.mutexCqueue: x.setVisible(False)
            for x in self.nremptyqueue: x.setVisible(False)
            for x in self.nrfullqueue: x.setVisible(False)
        elif self.visible_mode == "simulator":
            self.backbtn.setVisible(True)
            self.nextbtn.setVisible(False)
            self.settings_label.setVisible(False)
            self.mutexPval.setVisible(True)
            self.mutexP.setVisible(True)
            self.mutexCval.setVisible(True)
            self.mutexC.setVisible(True)
            self.nrfull.setVisible(True)
            self.nrfullval.setVisible(True)
            self.nrempty.setVisible(True)
            self.nremptyval.setVisible(True)
            self.producerbtn.setVisible(True)
            self.consumerbtn.setVisible(True)
            self.inidx.setVisible(True)
            self.outidx.setVisible(True)
            self.in_title.setVisible(True)
            self.out_title.setVisible(True)
            for x in self.check_size_list: x.setVisible(False)
            for x in self.circularbuffer_items: x.setVisible(True)
            for x in self.mutexPqueue: x.setVisible(True)
            for x in self.mutexCqueue: x.setVisible(True)
            for x in self.nremptyqueue: x.setVisible(True)
            for x in self.nrfullqueue: x.setVisible(True)
            for x in range(self.bufferSize):
                if self.circularbuffer.buffer[x] == None:
                    self.circularbuffer_items[x].setStyleSheet("color: gray;")
                else:
                    self.circularbuffer_items[x].setStyleSheet("color: balck; font-weight: bold;")
                self.circularbuffer_items[x].setText(f"{self.circularbuffer.buffer[x]}")
            self.mutexPval.setText(f"{self.circularbuffer.mutexP.value}")
            self.mutexCval.setText(f"{self.circularbuffer.mutexC.value}")
            self.nremptyval.setText(f"{self.circularbuffer.nrempty.value}")
            self.nrfullval.setText(f"{self.circularbuffer.nrfull.value}")
            self.inidx.setText(f"{self.circularbuffer.in_index}")
            self.outidx.setText(F"{self.circularbuffer.out_index}")
            for x in range(5):
                if x <= len(self.circularbuffer.mutexP.queue) - 1:
                    self.mutexPqueue[x].setStyleSheet("color: black; font-weight: bold;")
                    self.mutexPqueue[x].setText(f"{self.circularbuffer.mutexP.queue[x].name}")
                else:
                    self.mutexPqueue[x].setStyleSheet("color: gray;")
                    self.mutexPqueue[x].setText("None")
            for x in range(5):
                if x <= len(self.circularbuffer.mutexC.queue) - 1:
                    self.mutexCqueue[x].setStyleSheet("color: black; font-weight: bold;")
                    self.mutexCqueue[x].setText(f"{self.circularbuffer.mutexC.queue[x].name}")
                else:
                    self.mutexCqueue[x].setStyleSheet("color: gray;")
                    self.mutexCqueue[x].setText("None")
            for x in range(5):
                if x <= len(self.circularbuffer.nrempty.queue) - 1:
                    self.nremptyqueue[x].setStyleSheet("color: black; font-weight: bold;")
                    self.nremptyqueue[x].setText(f"{self.circularbuffer.nrempty.queue[x].name}")
                else:
                    self.nremptyqueue[x].setStyleSheet("color: gray;")
                    self.nremptyqueue[x].setText("None")
            for x in range(5):
                if x <= len(self.circularbuffer.nrfull.queue) - 1:
                    self.nrfullqueue[x].setStyleSheet("color: black; font-weight: bold;")
                    self.nrfullqueue[x].setText(f"{self.circularbuffer.nrfull.queue[x].name}")
                else:
                    self.nrfullqueue[x].setStyleSheet("color: gray;")
                    self.nrfullqueue[x].setText("None")
        self.update()  # UI 다시 그리기 요청

    def click_startbtn(self):
        self.visible_mode = "settings"
        self.updateUI()
    
    def click_backbtn(self):
        if self.visible_mode == "settings": self.visible_mode = "home"
        elif self.visible_mode == "simulator": self.visible_mode = "settings"
        self.updateUI()
    
    def click_nextbtn(self):
        if self.visible_mode == "settings":
            self.bufferSize = self.check_size()
            if not self.bufferSize:
                QMessageBox.warning(self, "Warning", "Select circular buffer size.")
            else:
                self.circularbuffer = CircularBuffer(self.bufferSize)
                self.circularbuffer_items = []
                for x, y in self.calculateCircularPositions(576, 200, 150, self.bufferSize):
                    buf = QLabel("None", self)
                    buf.setFont(QFont("Arial", 10))
                    buf.setFixedSize(50, 15)
                    buf.setStyleSheet("color: gray;")
                    buf.move(x, y)
                    buf.setVisible(False)
                    self.circularbuffer_items.append(buf)
                self.visible_mode = "simulator"
        self.updateUI()

    def click_producerbtn(self):
        newProducer = Producer(f"Prod{self.producerCnt}", self.circularbuffer)
        self.producerCnt += 1
        newProducer.start()

    def click_consumerbtn(self):
        newConsumer = Consumer(f"Cons{self.consumerCnt}", self.circularbuffer)
        self.consumerCnt += 1
        newConsumer.start()

    def check_size(self):
        for x in range(len(self.check_size_list)):
            if self.check_size_list[x].isChecked():
                return x + 4
        return False
    
    def calculateCircularPositions(self, center_x, center_y, radius, total_items):
        angle_per_item = 2 * math.pi / total_items
        for i in range(total_items):
            angle = i * angle_per_item
            item_x = center_x + radius * math.cos(angle - 0.5 * math.pi)
            item_y = center_y + radius * math.sin(angle - 0.5 * math.pi)
            yield int(item_x) - 25, int(item_y) - 7

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    sys.exit(app.exec())
