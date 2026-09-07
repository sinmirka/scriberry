from PySide6.QtWidgets import QMainWindow

from .ui_scriberry import Ui_ScriberryWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ScriberryWindow()
        self.ui.setupUi(self)