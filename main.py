from pathlib import Path
from PySide6.QtWidgets import QApplication

from scriberry.transcriber import WhisperTranscriber
from scriberry.gui.main_window import MainWindow

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())