import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
from pytestqt.qtbot import QtBot
from main import Ui_MainWindow, current_folder, view_history

@pytest.fixture
def ui(qtbot):
    app = QApplication([])
    ui = Ui_MainWindow()
    ui.setupUi(ui)
    qtbot.addWidget(ui)
    return ui


def test_find_button_exists(ui: Ui_MainWindow, qtbot: QtBot):
    # ui.textEdit_2.setText(r"C:\Users\Admin")
    # qtbot.mouseClick(ui.pushButton_3, Qt.LeftButton)
    # assert current_folder == r"C:\Users\Admin"
    ui.model = ui.scrollArea.widget().model
    root_path = ui.model.rootPath()
    assert root_path

def test_find_button_not_exists(ui: Ui_MainWindow, qtbot: QtBot):
    ui.textEdit_2.setText("non_existent_file_or_folder")
    qtbot.mouseClick(ui.pushButton_3, Qt.LeftButton)
    message_box = ui.findChild(QMessageBox)
    assert message_box is not None
    assert message_box.text() == "Файла или директории с таким именем не существует"