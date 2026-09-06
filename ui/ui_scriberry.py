# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scriberryVkAkmi.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ScriberryWindow(object):
    def setupUi(self, ScriberryWindow):
        if not ScriberryWindow.objectName():
            ScriberryWindow.setObjectName(u"ScriberryWindow")
        ScriberryWindow.resize(971, 850)
        ScriberryWindow.setMinimumSize(QSize(860, 780))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        ScriberryWindow.setFont(font)
        ScriberryWindow.setStyleSheet(u"\n"
"QMainWindow, QWidget#centralwidget {\n"
"    background-color: #121018;\n"
"    color: #f1eef6;\n"
"}\n"
"QWidget {\n"
"    color: #f1eef6;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"QLabel { background: transparent; border: none; }\n"
"QLabel#brandMark {\n"
"    background: transparent;\n"
"}\n"
"QLabel#titleLabel { font-size: 27px; font-weight: 700; }\n"
"QLabel#subtitleLabel, QLabel#formatsLabel, QLabel#modelHintLabel,\n"
"QLabel#deviceHintLabel, QLabel#outputHintLabel, QLabel#progressDetailLabel {\n"
"    color: #a7a0b5;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#badgeLabel, QLabel#fileCountLabel {\n"
"    background: #282031;\n"
"    color: #c9afea;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 11px;\n"
"    font-weight: 600;\n"
"}\n"
"QLabel#filesTitleLabel, QLabel#settingsTitleLabel,\n"
"QLabel#outputTitleLabel, QLabel#logsTitleLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"QLabel#stateLabel { color: #c3addf; font-weight: "
                        "600; }\n"
"QLabel#percentLabel { color: #cbb3fa; font-weight: 600; }\n"
"QFrame#filesCard, QFrame#settingsCard, QFrame#outputCard, QFrame#logsCard {\n"
"    background: #1b1723;\n"
"    border: 1px solid #302938;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton {\n"
"    background: #2b2435;\n"
"    border: 1px solid #45384f;\n"
"    border-radius: 8px;\n"
"    padding: 9px 16px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover { background: #392e45; border-color: #8e6fb1; }\n"
"QPushButton:pressed { background: #463652; }\n"
"QPushButton:focus { border: 1px solid #c6a2f3; }\n"
"QPushButton:disabled { color: #756d82; background: #211c29; border-color: #332b3e; }\n"
"QPushButton#startButton {\n"
"    background: #bca1f7;\n"
"    color: #251636;\n"
"    border: 1px solid #bca1f7;\n"
"}\n"
"QPushButton#startButton:hover { background: #cfb6ff; border-color: #cfb6ff; }\n"
"QPushButton#startButton:pressed { background: #a889e0; }\n"
"QPushButton#startButton:disabled { background: #44364f; color: #9c8aaa; bord"
                        "er-color: #44364f; }\n"
"QLineEdit, QComboBox {\n"
"    background: #14111b;\n"
"    border: 1px solid #3a3046;\n"
"    border-radius: 8px;\n"
"    padding: 9px 11px;\n"
"    selection-background-color: #60447d;\n"
"    selection-color: #ffffff;\n"
"}\n"
"QLineEdit:focus, QComboBox:focus { border-color: #bca1f7; }\n"
"QComboBox:hover { border-color: #87669f; }\n"
"QComboBox::drop-down { width: 28px; border: none; }\n"
"QComboBox QAbstractItemView {\n"
"    background: #241d2d;\n"
"    border: 1px solid #554164;\n"
"    padding: 5px;\n"
"    selection-background-color: #60447d;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"}\n"
"QTreeWidget {\n"
"    background: #14111b;\n"
"    alternate-background-color: #1a1522;\n"
"    border: 1px solid #302938;\n"
"    border-radius: 8px;\n"
"    selection-background-color: #483254;\n"
"    selection-color: #f8f2ff;\n"
"    outline: 0;\n"
"}\n"
"QTreeWidget::item { padding: 8px 5px; border: none; }\n"
"QTreeWidget::item:hover { background: #2a2134; }\n"
"QTreeW"
                        "idget::item:selected { background: #483254; }\n"
"QHeaderView::section {\n"
"    background: #241d2d;\n"
"    color: #b8aec7;\n"
"    border: none;\n"
"    border-bottom: 1px solid #382d43;\n"
"    padding: 9px 8px;\n"
"    font-size: 12px;\n"
"}\n"
"QPlainTextEdit {\n"
"    background: #14111b;\n"
"    color: #b9b0c7;\n"
"    border: 1px solid #302938;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-family: \"Cascadia Code\", \"Consolas\", monospace;\n"
"    font-size: 12px;\n"
"    selection-background-color: #60447d;\n"
"}\n"
"QProgressBar {\n"
"    background: #302637;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    min-height: 10px;\n"
"    max-height: 10px;\n"
"}\n"
"QProgressBar::chunk { background: #bca1f7; border-radius: 5px; }\n"
"QScrollBar:vertical { background: #1b1723; width: 10px; margin: 0; }\n"
"QScrollBar::handle:vertical { background: #51405f; min-height: 24px; border-radius: 5px; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }\n"
""
                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: transparent; }\n"
"QToolTip { background: #30243b; color: #f1eef6; border: 1px solid #6f5089; padding: 5px; }\n"
"   ")
        self.centralwidget = QWidget(ScriberryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(12, 12, 12, 12)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setSpacing(14)
        self.headerLayout.setObjectName(u"headerLayout")
        self.brandTextLayout = QVBoxLayout()
        self.brandTextLayout.setSpacing(2)
        self.brandTextLayout.setObjectName(u"brandTextLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.brandTextLayout.addWidget(self.titleLabel)


        self.headerLayout.addLayout(self.brandTextLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.brandMark = QLabel(self.centralwidget)
        self.brandMark.setObjectName(u"brandMark")
        self.brandMark.setMinimumSize(QSize(40, 40))
        self.brandMark.setMaximumSize(QSize(40, 40))
        self.brandMark.setStyleSheet(u"")
        self.brandMark.setPixmap(QPixmap(u"scriberry_logo.png"))
        self.brandMark.setScaledContents(True)
        self.brandMark.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.headerLayout.addWidget(self.brandMark)


        self.mainLayout.addLayout(self.headerLayout)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(18)
        self.contentLayout.setObjectName(u"contentLayout")
        self.filesCard = QFrame(self.centralwidget)
        self.filesCard.setObjectName(u"filesCard")
        self.filesLayout = QVBoxLayout(self.filesCard)
        self.filesLayout.setSpacing(12)
        self.filesLayout.setObjectName(u"filesLayout")
        self.filesLayout.setContentsMargins(18, 18, 18, 18)
        self.filesHeaderLayout = QHBoxLayout()
        self.filesHeaderLayout.setObjectName(u"filesHeaderLayout")
        self.filesTitleLabel = QLabel(self.filesCard)
        self.filesTitleLabel.setObjectName(u"filesTitleLabel")

        self.filesHeaderLayout.addWidget(self.filesTitleLabel)

        self.filesHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filesHeaderLayout.addItem(self.filesHeaderSpacer)

        self.fileCountLabel = QLabel(self.filesCard)
        self.fileCountLabel.setObjectName(u"fileCountLabel")

        self.filesHeaderLayout.addWidget(self.fileCountLabel)


        self.filesLayout.addLayout(self.filesHeaderLayout)

        self.sourceButtonsLayout = QHBoxLayout()
        self.sourceButtonsLayout.setSpacing(10)
        self.sourceButtonsLayout.setObjectName(u"sourceButtonsLayout")
        self.selectVideoButton = QPushButton(self.filesCard)
        self.selectVideoButton.setObjectName(u"selectVideoButton")

        self.sourceButtonsLayout.addWidget(self.selectVideoButton)

        self.selectFolderButton = QPushButton(self.filesCard)
        self.selectFolderButton.setObjectName(u"selectFolderButton")

        self.sourceButtonsLayout.addWidget(self.selectFolderButton)


        self.filesLayout.addLayout(self.sourceButtonsLayout)

        self.sourcePathEdit = QLineEdit(self.filesCard)
        self.sourcePathEdit.setObjectName(u"sourcePathEdit")
        self.sourcePathEdit.setReadOnly(True)

        self.filesLayout.addWidget(self.sourcePathEdit)

        self.filesTreeWidget = QTreeWidget(self.filesCard)
        self.filesTreeWidget.setObjectName(u"filesTreeWidget")
        self.filesTreeWidget.setMinimumSize(QSize(0, 150))
        self.filesTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.filesTreeWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.filesTreeWidget.setAlternatingRowColors(True)
        self.filesTreeWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.filesTreeWidget.setRootIsDecorated(False)
        self.filesTreeWidget.setUniformRowHeights(True)
        self.filesTreeWidget.setSupportedDragActions(Qt.DropAction.CopyAction|Qt.DropAction.MoveAction)
        self.filesTreeWidget.header().setCascadingSectionResizes(False)
        self.filesTreeWidget.header().setDefaultSectionSize(150)
        self.filesTreeWidget.header().setHighlightSections(False)
        self.filesTreeWidget.header().setProperty(u"showSortIndicator", False)
        self.filesTreeWidget.header().setStretchLastSection(True)

        self.filesLayout.addWidget(self.filesTreeWidget)

        self.formatsLabel = QLabel(self.filesCard)
        self.formatsLabel.setObjectName(u"formatsLabel")
        self.formatsLabel.setWordWrap(True)

        self.filesLayout.addWidget(self.formatsLabel)


        self.contentLayout.addWidget(self.filesCard)

        self.settingsCard = QFrame(self.centralwidget)
        self.settingsCard.setObjectName(u"settingsCard")
        self.settingsLayout = QVBoxLayout(self.settingsCard)
        self.settingsLayout.setSpacing(9)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setContentsMargins(18, 18, 18, 18)
        self.settingsTitleLabel = QLabel(self.settingsCard)
        self.settingsTitleLabel.setObjectName(u"settingsTitleLabel")

        self.settingsLayout.addWidget(self.settingsTitleLabel)

        self.modelLabel = QLabel(self.settingsCard)
        self.modelLabel.setObjectName(u"modelLabel")

        self.settingsLayout.addWidget(self.modelLabel)

        self.modelComboBox = QComboBox(self.settingsCard)
        self.modelComboBox.addItem(u"tiny")
        self.modelComboBox.addItem(u"base")
        self.modelComboBox.addItem(u"small")
        self.modelComboBox.addItem(u"medium")
        self.modelComboBox.addItem(u"large-v3")
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.settingsLayout.addWidget(self.modelComboBox)

        self.modelHintLabel = QLabel(self.settingsCard)
        self.modelHintLabel.setObjectName(u"modelHintLabel")
        self.modelHintLabel.setWordWrap(True)

        self.settingsLayout.addWidget(self.modelHintLabel)

        self.deviceLabel = QLabel(self.settingsCard)
        self.deviceLabel.setObjectName(u"deviceLabel")

        self.settingsLayout.addWidget(self.deviceLabel)

        self.deviceComboBox = QComboBox(self.settingsCard)
        self.deviceComboBox.addItem(u"CPU")
        self.deviceComboBox.addItem(u"CUDA")
        self.deviceComboBox.setObjectName(u"deviceComboBox")

        self.settingsLayout.addWidget(self.deviceComboBox)

        self.deviceHintLabel = QLabel(self.settingsCard)
        self.deviceHintLabel.setObjectName(u"deviceHintLabel")
        self.deviceHintLabel.setWordWrap(True)

        self.settingsLayout.addWidget(self.deviceHintLabel)

        self.languageLabel = QLabel(self.settingsCard)
        self.languageLabel.setObjectName(u"languageLabel")

        self.settingsLayout.addWidget(self.languageLabel)

        self.languageComboBox = QComboBox(self.settingsCard)
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.settingsLayout.addWidget(self.languageComboBox)


        self.contentLayout.addWidget(self.settingsCard)

        self.contentLayout.setStretch(0, 5)
        self.contentLayout.setStretch(1, 3)

        self.mainLayout.addLayout(self.contentLayout)

        self.outputCard = QFrame(self.centralwidget)
        self.outputCard.setObjectName(u"outputCard")
        self.outputLayout = QVBoxLayout(self.outputCard)
        self.outputLayout.setSpacing(10)
        self.outputLayout.setObjectName(u"outputLayout")
        self.outputLayout.setContentsMargins(18, 16, 18, 16)
        self.outputTitleLabel = QLabel(self.outputCard)
        self.outputTitleLabel.setObjectName(u"outputTitleLabel")

        self.outputLayout.addWidget(self.outputTitleLabel)

        self.outputPathLayout = QHBoxLayout()
        self.outputPathLayout.setSpacing(10)
        self.outputPathLayout.setObjectName(u"outputPathLayout")
        self.outputPathEdit = QLineEdit(self.outputCard)
        self.outputPathEdit.setObjectName(u"outputPathEdit")
        self.outputPathEdit.setClearButtonEnabled(True)

        self.outputPathLayout.addWidget(self.outputPathEdit)

        self.selectOutputButton = QPushButton(self.outputCard)
        self.selectOutputButton.setObjectName(u"selectOutputButton")

        self.outputPathLayout.addWidget(self.selectOutputButton)


        self.outputLayout.addLayout(self.outputPathLayout)


        self.mainLayout.addWidget(self.outputCard)

        self.runLayout = QHBoxLayout()
        self.runLayout.setSpacing(12)
        self.runLayout.setObjectName(u"runLayout")
        self.progressLayout = QVBoxLayout()
        self.progressLayout.setSpacing(8)
        self.progressLayout.setObjectName(u"progressLayout")
        self.stateLayout = QHBoxLayout()
        self.stateLayout.setObjectName(u"stateLayout")
        self.stateLabel = QLabel(self.centralwidget)
        self.stateLabel.setObjectName(u"stateLabel")

        self.stateLayout.addWidget(self.stateLabel)

        self.stateSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.stateLayout.addItem(self.stateSpacer)

        self.percentLabel = QLabel(self.centralwidget)
        self.percentLabel.setObjectName(u"percentLabel")

        self.stateLayout.addWidget(self.percentLabel)


        self.progressLayout.addLayout(self.stateLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.progressLayout.addWidget(self.progressBar)

        self.progressDetailLabel = QLabel(self.centralwidget)
        self.progressDetailLabel.setObjectName(u"progressDetailLabel")

        self.progressLayout.addWidget(self.progressDetailLabel)


        self.runLayout.addLayout(self.progressLayout)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)
        self.cancelButton.setMinimumSize(QSize(100, 44))
        self.cancelButton.setText(u"Cancel")

        self.runLayout.addWidget(self.cancelButton)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(116, 44))
        self.startButton.setText(u"Start")

        self.runLayout.addWidget(self.startButton)

        self.runLayout.setStretch(0, 1)

        self.mainLayout.addLayout(self.runLayout)

        self.logsCard = QFrame(self.centralwidget)
        self.logsCard.setObjectName(u"logsCard")
        self.logsLayout = QVBoxLayout(self.logsCard)
        self.logsLayout.setSpacing(10)
        self.logsLayout.setObjectName(u"logsLayout")
        self.logsLayout.setContentsMargins(18, 16, 18, 16)
        self.logsTitleLabel = QLabel(self.logsCard)
        self.logsTitleLabel.setObjectName(u"logsTitleLabel")

        self.logsLayout.addWidget(self.logsTitleLabel)

        self.logTextEdit = QPlainTextEdit(self.logsCard)
        self.logTextEdit.setObjectName(u"logTextEdit")
        self.logTextEdit.setMinimumSize(QSize(0, 90))
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setMaximumBlockCount(2000)

        self.logsLayout.addWidget(self.logTextEdit)


        self.mainLayout.addWidget(self.logsCard)

        self.mainLayout.setStretch(1, 3)
        self.mainLayout.setStretch(4, 1)
        ScriberryWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.modelLabel.setBuddy(self.modelComboBox)
        self.deviceLabel.setBuddy(self.deviceComboBox)
        self.languageLabel.setBuddy(self.languageComboBox)
        self.outputTitleLabel.setBuddy(self.outputPathEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.selectVideoButton, self.selectFolderButton)
        QWidget.setTabOrder(self.selectFolderButton, self.sourcePathEdit)
        QWidget.setTabOrder(self.sourcePathEdit, self.filesTreeWidget)
        QWidget.setTabOrder(self.filesTreeWidget, self.modelComboBox)
        QWidget.setTabOrder(self.modelComboBox, self.deviceComboBox)
        QWidget.setTabOrder(self.deviceComboBox, self.languageComboBox)
        QWidget.setTabOrder(self.languageComboBox, self.outputPathEdit)
        QWidget.setTabOrder(self.outputPathEdit, self.selectOutputButton)
        QWidget.setTabOrder(self.selectOutputButton, self.startButton)
        QWidget.setTabOrder(self.startButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.logTextEdit)

        self.retranslateUi(ScriberryWindow)

        self.modelComboBox.setCurrentIndex(2)
        self.startButton.setDefault(True)


        QMetaObject.connectSlotsByName(ScriberryWindow)
    # setupUi

    def retranslateUi(self, ScriberryWindow):
        ScriberryWindow.setWindowTitle(QCoreApplication.translate("ScriberryWindow", u"Scriberry", None))
        self.titleLabel.setText(QCoreApplication.translate("ScriberryWindow", u"scriberry", None))
        self.brandMark.setText("")
        self.filesTitleLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.fileCountLabel.setText(QCoreApplication.translate("ScriberryWindow", u"0 \u0444\u0430\u0439\u043b\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.selectVideoButton.setToolTip(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0434\u0438\u043d \u0432\u0438\u0434\u0435\u043e\u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.selectVideoButton.setText(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
#if QT_CONFIG(tooltip)
        self.selectFolderButton.setToolTip(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0432\u0438\u0434\u0435\u043e\u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.selectFolderButton.setText(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
#if QT_CONFIG(accessibility)
        self.sourcePathEdit.setAccessibleName(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a", None))
#endif // QT_CONFIG(accessibility)
        self.sourcePathEdit.setPlaceholderText(QCoreApplication.translate("ScriberryWindow", u"\u041f\u0443\u0442\u044c \u043a \u0432\u0438\u0434\u0435\u043e \u0438\u043b\u0438 \u043f\u0430\u043f\u043a\u0435", None))
        ___qtreewidgetitem = self.filesTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("ScriberryWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ScriberryWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ScriberryWindow", u"\u0424\u0430\u0439\u043b", None))
#if QT_CONFIG(accessibility)
        self.filesTreeWidget.setAccessibleName(QCoreApplication.translate("ScriberryWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
#endif // QT_CONFIG(accessibility)
        self.formatsLabel.setText(QCoreApplication.translate("ScriberryWindow", u"MP4, MKV, MOV, AVI, WEBM \u0438 \u0434\u0440\u0443\u0433\u0438\u0435 \u0432\u0438\u0434\u0435\u043e\u0444\u043e\u0440\u043c\u0430\u0442\u044b", None))
        self.settingsTitleLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f", None))
        self.modelLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c Whisper", None))

        self.modelHintLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0411\u043e\u043b\u044c\u0448\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u0442\u0440\u0435\u0431\u0443\u044e\u0442 \u0431\u043e\u043b\u044c\u0448\u0435 \u043f\u0430\u043c\u044f\u0442\u0438.", None))
        self.deviceLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))

        self.deviceHintLabel.setText(QCoreApplication.translate("ScriberryWindow", u"CUDA \u2014 \u0434\u043b\u044f \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u044b\u0445 \u0432\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442 NVIDIA.", None))
        self.languageLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u042f\u0437\u044b\u043a \u0432\u0438\u0434\u0435\u043e", None))
        self.languageComboBox.setItemText(0, QCoreApplication.translate("ScriberryWindow", u"\u0410\u0432\u0442\u043e\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.languageComboBox.setItemText(1, QCoreApplication.translate("ScriberryWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439 (ru)", None))
        self.languageComboBox.setItemText(2, QCoreApplication.translate("ScriberryWindow", u"English (en)", None))
        self.languageComboBox.setItemText(3, QCoreApplication.translate("ScriberryWindow", u"Deutsch (de)", None))
        self.languageComboBox.setItemText(4, QCoreApplication.translate("ScriberryWindow", u"Fran\u00e7ais (fr)", None))
        self.languageComboBox.setItemText(5, QCoreApplication.translate("ScriberryWindow", u"Espa\u00f1ol (es)", None))
        self.languageComboBox.setItemText(6, QCoreApplication.translate("ScriberryWindow", u"Italiano (it)", None))
        self.languageComboBox.setItemText(7, QCoreApplication.translate("ScriberryWindow", u"Portugu\u00eas (pt)", None))
        self.languageComboBox.setItemText(8, QCoreApplication.translate("ScriberryWindow", u"\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430 (uk)", None))
        self.languageComboBox.setItemText(9, QCoreApplication.translate("ScriberryWindow", u"\u049a\u0430\u0437\u0430\u049b\u0448\u0430 (kk)", None))
        self.languageComboBox.setItemText(10, QCoreApplication.translate("ScriberryWindow", u"Polski (pl)", None))
        self.languageComboBox.setItemText(11, QCoreApplication.translate("ScriberryWindow", u"T\u00fcrk\u00e7e (tr)", None))
        self.languageComboBox.setItemText(12, QCoreApplication.translate("ScriberryWindow", u"\u4e2d\u6587 (zh)", None))
        self.languageComboBox.setItemText(13, QCoreApplication.translate("ScriberryWindow", u"\u65e5\u672c\u8a9e (ja)", None))
        self.languageComboBox.setItemText(14, QCoreApplication.translate("ScriberryWindow", u"\ud55c\uad6d\uc5b4 (ko)", None))
        self.languageComboBox.setItemText(15, QCoreApplication.translate("ScriberryWindow", u"\u0627\u0644\u0639\u0631\u0628\u064a\u0629 (ar)", None))
        self.languageComboBox.setItemText(16, QCoreApplication.translate("ScriberryWindow", u"\u0939\u093f\u0928\u094d\u0926\u0940 (hi)", None))

        self.outputTitleLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(accessibility)
        self.outputPathEdit.setAccessibleName(QCoreApplication.translate("ScriberryWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
#endif // QT_CONFIG(accessibility)
        self.outputPathEdit.setPlaceholderText(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.selectOutputButton.setToolTip(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.selectOutputButton.setText(QCoreApplication.translate("ScriberryWindow", u"\u041e\u0431\u0437\u043e\u0440\u2026", None))
        self.stateLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e \u043a \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.percentLabel.setText(QCoreApplication.translate("ScriberryWindow", u"0%", None))
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleName(QCoreApplication.translate("ScriberryWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f", None))
#endif // QT_CONFIG(accessibility)
        self.progressDetailLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b\u044b \u0438 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f.", None))
#if QT_CONFIG(tooltip)
        self.cancelButton.setToolTip(QCoreApplication.translate("ScriberryWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.startButton.setToolTip(QCoreApplication.translate("ScriberryWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.logsTitleLabel.setText(QCoreApplication.translate("ScriberryWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0441\u043e\u0431\u044b\u0442\u0438\u0439", None))
#if QT_CONFIG(accessibility)
        self.logTextEdit.setAccessibleName(QCoreApplication.translate("ScriberryWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0438 \u043b\u043e\u0433\u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f", None))
#endif // QT_CONFIG(accessibility)
        self.logTextEdit.setPlaceholderText(QCoreApplication.translate("ScriberryWindow", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u044f\u0432\u044f\u0442\u0441\u044f \u0441\u0442\u0430\u0442\u0443\u0441 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438, \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0438 \u043e\u0448\u0438\u0431\u043a\u0438.", None))
    # retranslateUi

