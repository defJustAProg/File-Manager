from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QLabel, QTextEdit, \
    QMessageBox, QMainWindow

current_folder: str = ""
view_history = []
view_history.append(current_folder)


class CustomTextEdit(QTextEdit):

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if os.path.exists(self.toPlainText()):
                if os.path.isdir(self.toPlainText()):
                    global current_folder
                    current_folder = self.toPlainText()
                    print(current_folder)
                    view_history.append(self.toPlainText())
                    ui.scrollArea_2.setWidget(FolderViewer(self.toPlainText()))
                    ui.label.setText(f"Элементов: {str(len(os.listdir(self.toPlainText())))}")
                elif os.path.isfile(self.toPlainText()):
                    subprocess.Popen([self.toPlainText()], shell=True)
            else:
                messageBox = QMessageBox()
                messageBox.setIcon(QMessageBox.Warning)
                messageBox.setText("Файла или директории с таким путем не существует")
                messageBox.setWindowTitle("Предупреждение")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec_()
        else:  # C:\Users\Admin    C:\Users\Admin\Desktop
            super().keyPressEvent(event)


class CustomTextEdit_2(QTextEdit):

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if os.path.exists(self.toPlainText()):
                if os.path.isdir(self.toPlainText()):
                    global current_folder
                    current_folder = self.toPlainText()
                    view_history.append(self.toPlainText())
                    ui.scrollArea_2.setWidget(FolderViewer(self.toPlainText()))
                    ui.label.setText(f"Элементов: {str(len(os.listdir(self.toPlainText())))}")
                elif os.path.isfile(self.toPlainText()):
                    subprocess.Popen([self.toPlainText()], shell=True)
            elif self.toPlainText():
                for root, dirs, files in os.walk('/'):
                    if self.toPlainText() in files:
                        subprocess.Popen([os.path.join(root, self.toPlainText())], shell=True)
                        break
                else:
                    messageBox = QMessageBox()
                    messageBox.setIcon(QMessageBox.Warning)
                    messageBox.setText("Файла или директории с таким именем не существует")
                    messageBox.setWindowTitle("Предупреждение")
                    messageBox.setStandardButtons(QMessageBox.Ok)
                    messageBox.exec_()
            else:
                messageBox = QMessageBox()
                messageBox.setIcon(QMessageBox.Warning)
                messageBox.setText("Файла или директории с таким именем не существует")
                messageBox.setWindowTitle("Предупреждение")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec_()
        else:  # C:\Users\Admin    C:\Users\Admin\Desktop
            super().keyPressEvent(event)


class FolderViewer(QWidget):
    def __init__(self, root: str):
        super().__init__()

        self.tree_view = QTreeView()
        self.model = QFileSystemModel()
        self.model.setRootPath(root)

        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(root))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree_view)
        self.setLayout(self.layout)
        self.tree_view.clicked.connect(self.handleClicked)

    def handleClicked(self, index):
        file_path = self.model.filePath(index)
        if os.path.isfile(file_path):
            subprocess.Popen([file_path], shell=True)


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("File manager")
        MainWindow.resize(1259, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 361, 741))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(FolderViewer(""))

        # self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        # self.treeWidget.setGeometry(QtCore.QRect(0, 0, 341, 741))
        # self.treeWidget.setObjectName("treeWidget")
        # self.treeWidget.headerItem().setText(0, "Root catalog")
        #
        #
        # def onClicked(item: QTreeWidgetItem, len: int):
        #     name = item.data(0, QtCore.Qt.UserRole)
        #     if os.path.isdir('/' + name):
        #         print("dir")
        #         for sub_name in os.listdir('/' + name):
        #             subitem = QTreeWidgetItem(item, [sub_name])
        #             item.addChild(subitem)
        #             subitem.clicked.connect(lambda subitem=subitem: onClicked(subitem))
        #     elif os.path.isfile('/' + name):
        #         print("file")
        #
        # for catalog in os.listdir('/'):
        #     item = QTreeWidgetItem(self.treeWidget, [catalog])
        #     item.setData(0, QtCore.Qt.UserRole, catalog)
        #     self.treeWidget.addTopLevelItem(item)
        #
        # self.treeWidget.itemClicked.connect(lambda item, onClicked=onClicked: onClicked(item))
        #
        #
        # def get_QTreeWidgetItem_from_vault(self, path: str, item: QTreeWidgetItem):
        #     print(os.listdir(path))
        #     return QTreeWidgetItem(item, os.listdir(path))

        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(380, 40, 871, 741))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea()
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidget(FolderViewer(""))
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onButtonPrevClick)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.onButtonNextClick)
        self.textEdit = CustomTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 0, 711, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = CustomTextEdit_2(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(890, 0, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 786, 361, 20))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 30, 20, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1190, 0, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.onButtonFindClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def onButtonClick(self):
    #     global current_folder
    #     try:
    #         print(view_history[current_folder])
    #         # self.scrollArea_2.setWidget(FolderViewer(view_history[view_history.index(current_folder)] - 1))
    #         # current_folder = view_history[view_history.index(current_folder)] - 1
    #     except IndexError:
    #         pass

    def onButtonFindClicked(self):
        if os.path.exists(self.textEdit_2.toPlainText()):
            if os.path.isdir(self.textEdit_2.toPlainText()):
                global current_folder
                current_folder = self.textEdit_2.toPlainText()
                view_history.append(self.textEdit_2.toPlainText())
                ui.scrollArea_2.setWidget(FolderViewer(self.textEdit_2.toPlainText()))
                ui.label.setText(f"Элементов: {str(len(os.listdir(self.textEdit_2.toPlainText())))}")
            elif os.path.isfile(self.textEdit_2.toPlainText()):
                subprocess.Popen([self.textEdit_2.toPlainText()], shell=True)
        elif self.textEdit_2.toPlainText():
            for root, dirs, files in os.walk('/'):
                if self.textEdit_2.toPlainText() in files:
                    subprocess.Popen([os.path.join(root, self.textEdit_2.toPlainText())], shell=True)
                    break
            else:
                messageBox = QMessageBox()
                messageBox.setIcon(QMessageBox.Warning)
                messageBox.setText("Файла или директории с таким именем не существует")
                messageBox.setWindowTitle("Предупреждение")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec_()
        else:
            messageBox = QMessageBox()
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Файла или директории с таким именем не существует")
            messageBox.setWindowTitle("Предупреждение")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec_()

    def onButtonPrevClick(self):
        global current_folder
        try:
            view_history_index = view_history.index(current_folder)
            if view_history_index > 0:
                ui.scrollArea_2.setWidget(FolderViewer(view_history[view_history_index - 1]))
                # ui.label.setText(f"Элементов: {len(os.listdir(view_history[view_history_index - 1]))}")
                current_folder = view_history[view_history_index - 1]
        except ValueError:
            pass

    def onButtonNextClick(self):
        global current_folder
        try:
            view_history_index = view_history.index(current_folder)
            if view_history_index < len(view_history) - 1:
                ui.scrollArea_2.setWidget(FolderViewer(view_history[view_history_index + 1]))
                # ui.label.setText(f"Элементов: {len(os.listdir(view_history[view_history_index + 1]))}")
                current_folder = view_history[view_history_index + 1]
        except ValueError:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Prev"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "Элементов:"))
        self.pushButton_3.setText(_translate("MainWindow", "Find"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
