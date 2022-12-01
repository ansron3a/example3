import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from form_staff import Ui_Form

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())