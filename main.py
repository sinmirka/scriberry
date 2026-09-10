from pathlib import Path
from PySide6.QtWidgets import QApplication

from scriberry.transcriber import WhisperTranscriber
from scriberry.gui.main_window import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()