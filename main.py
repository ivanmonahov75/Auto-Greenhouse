from PyQt6 import QtWidgets, uic, QtCore
import datetime

app = QtWidgets.QApplication([])
ui = uic.loadUi('design.ui')

ui.val_temp.setText(f'{10} C°')
ui.mods.addItems(['Auto', 'Manual'])

def timerEvent():
    global time
    now = datetime.datetime.now()
    time = QtCore.QTime(now.hour, now.minute, now.second)
    print(time.toString("hh:mm:ss"))
    ui.datetime.setDateTime(datetime.datetime.now())


timer = QtCore.QTimer()
now = datetime.datetime.now()
time = QtCore.QTime(now.hour, now.minute, now.second)

timer.timeout.connect(timerEvent)
timer.start(1000)

def mode_changer(what):
    print(what)

def fan_in(val):
    print(val)

ui.mods.currentIndexChanged.connect(mode_changer)
ui.slight.valueChanged.connect(fan_in)
ui.show()
app.exec()
