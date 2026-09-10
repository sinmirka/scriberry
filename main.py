from pathlib import Path
from PySide6.QtWidgets import QApplication

from scriberry.transcriber import WhisperTranscriber
from scriberry.gui.main_window import MainWindow

test_video = Path(__file__).parent / 'whisper_test.mp4'

app = QApplication([])

window = MainWindow()
window.show()

app.exec()