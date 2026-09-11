from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTreeWidgetItem

from .ui_scriberry import Ui_ScriberryWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ScriberryWindow()
        self.ui.setupUi(self)

        self._selected_files: list[Path] = []
        self._output_directory: Path | None = None

        self._connect_signals()

    def _connect_signals(self):
        self.ui.selectVideoButton.clicked.connect(
            self._select_source
        )

    def _select_source(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            filter="Видео (*.mp4 *.mkv *.avi *.mov *.webm)"
        )
        if not file_path:
            return

        self._selected_files.append(file_path)
        print("\n".join(self._selected_files))

        path = Path(file_path)
        size_mb = path.stat().st_size / (1024 * 1024)

        item = QTreeWidgetItem([
            path.name,
            f"{size_mb:.1f} MB",
            "Ожидает"
        ])

        self.ui.filesTreeWidget.addTopLevelItem(item)
        self.ui.fileCountLabel.setText(
            f"{len(self._selected_files)} файлов"
        )