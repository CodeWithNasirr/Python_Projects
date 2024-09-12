import os
import requests
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import re
import json
import platform

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.save1_location()  # Load the save location when the UI initializes

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(554, 451)
        self.setMaximumSize(QtCore.QSize(554, 451))
        self.setStyleSheet("""
                QWidget#centralwidget {
                    background: qlineargradient(spread:pad, x1:0.136409, y1:0.131, x2:1, y2:1, stop:0 rgba(36, 110, 233, 255), stop:1 rgba(255, 255, 255, 255));
                }""")
        self.centralWidget = QtWidgets.QWidget(self)
        self.objectName = "CentralWidget"
        self.Drag_drop = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.Drag_drop.setGeometry(QtCore.QRect(110, 20, 351, 91))
        self.Drag_drop.setPlaceholderText("Drag Your File Here...")
        self.Drag_drop.setStyleSheet("background: rgb(176, 196, 222);font:25 italic 16pt Calibri;border-radius:20px")
        self.Drag_drop.setAcceptDrops(True)
        self.Drag_drop.dragEnterEvent = self.Drag_Event
        self.Drag_drop.dropEvent = self.Drop_Event

        self.Samsung_Label = QtWidgets.QLabel(self.centralWidget)
        self.Samsung_Label.setObjectName("Samsung_Label")
        self.Samsung_Label.setGeometry(QtCore.QRect(0, 150, 121, 31))
        self.Samsung_Label.setStyleSheet("font: 87 11pt Arial Black;color:rgb(12, 12, 12);")

        self.Samsung_Text = QtWidgets.QLineEdit(self.centralWidget)
        self.Samsung_Text.setGeometry(QtCore.QRect(110, 150, 351, 31))
        self.Samsung_Text.setStyleSheet("border-radius:15px;")
        self.Samsung_Text.textChanged.connect(self.text_Id)

        self.Save_Label = QtWidgets.QLabel(self.centralWidget)
        self.Save_Label.setObjectName("Save_Label")
        self.Save_Label.setGeometry(QtCore.QRect(10, 190, 81, 51))
        self.Save_Label.setStyleSheet("font: 87 11pt Arial Black;color:rgb(12, 12, 12);")

        self.Save_Text = QtWidgets.QLineEdit(self.centralWidget)
        self.Save_Text.setGeometry(QtCore.QRect(110, 200, 351, 31))
        self.Save_Text.setStyleSheet("border-radius:15px;")

        self.Save_Button = QtWidgets.QPushButton(self.centralWidget)
        self.Save_Button.setGeometry(QtCore.QRect(160, 250, 91, 41))
        self.Save_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.Save_Button.setObjectName("SAVE")
        self.Save_Button.clicked.connect(self.save_location)
        

        self.Download_Button = QtWidgets.QPushButton(self.centralWidget)
        self.Download_Button.setGeometry(QtCore.QRect(290, 250, 110, 41))
        self.Download_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.Download_Button.setObjectName("DOWNLOAD")
        self.Download_Button.clicked.connect(self.Download)
        self.Download_Button.setEnabled(False)
        self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

        self.Rest_Button=QtWidgets.QPushButton(self.centralWidget)
        self.Rest_Button.setGeometry(QtCore.QRect(230, 360, 110, 41))
        self.Rest_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.Rest_Button.clicked.connect(self.Rest)


        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 330, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("ProgressBar")
        self.setCentralWidget(self.centralWidget)

        self.translate()
        QtCore.QMetaObject.connectSlotsByName(self)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "SAMSUNG DOWNLOADER"))
        self.Samsung_Label.setText(_translate("MainWindow", "Samsung ID: "))
        self.Save_Label.setText(_translate("MainWindow", "Save To: "))
        self.Save_Button.setText(_translate("MainWindow", "SAVE"))
        self.Download_Button.setText(_translate("MainWindow", "DOWNLOAD"))
        self.Rest_Button.setText(_translate("MainWindow","RESET"))
        

    def Drag_Event(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def Drop_Event(self, event):
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile())
            self.handle_file(file_path)  # Correctly call the handle_file method
            file_path1 = file_path[-10:]
            self.Drag_drop.setPlainText(file_path1)

    def handle_file(self, file_path):
        samsung_hex_value = b'\x53\x45\x43\x57\x55\x50'
        try:
            with open(file_path, "rb") as file:
                samsung_content = file.read()
                samsung_index = samsung_content.find(samsung_hex_value)
                if samsung_index != -1:
                    samsung_index += 13
                    next_bytes = samsung_content[samsung_index:samsung_index + 3]
                    samsung_id = next_bytes.decode('ascii')
                    self.Samsung_Text.clear()
                    self.Samsung_Text.setText(samsung_id)
                    self.Download_Button.setEnabled(True)
                    self.Download_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
                    self.show_message("Detect", f"Samsung ID: {samsung_id}")
                else:
                    self.show_message("Error", "Samsung ID not found in the file.", QMessageBox.Warning)
        except Exception as e:
            self.show_message("Error", f"Error processing file: {e}", QMessageBox.Critical)

    def save_location(self):
        save_location = QFileDialog.getExistingDirectory(self)
        if save_location:
            self.Save_Text.clear()
            self.Save_Text.setText(save_location)
            self.Download_Button.setEnabled(True)
            self.Save_Button.setEnabled(False)
            self.Save_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

            self.save_to_json(save_location)
            self.save_location = save_location

    def save_to_json(self, save_location):
        with open("save_location.json", "w") as f:
            json.dump({"save_location": save_location}, f)
            

    def save1_location(self):
        try:
            with open("save_location.json", "r") as f:
                data = json.load(f)
                save_location = data.get("save_location")
                if save_location:
                    self.Save_Text.clear()
                    self.Save_Text.setText(save_location)
                    self.Save_Button.setEnabled(False)
                    self.Save_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")
                    self.save_location = save_location
        except FileNotFoundError:
            with open("save_location.json", "w") as f:
                pass

    def text_Id(self):
        text = self.Samsung_Text.text().strip()
        if len(text) == 3:
            self.Download_Button.setEnabled(True)
            self.Download_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        else:
            self.Download_Button.setEnabled(False)
            self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

    def open_file(self,path):
        system_plateform=platform.system()
        if system_plateform == "Windows":
            os.startfile(path)
        #More OS


    def Rest(self):
        self.Drag_drop.clear()
        self.Samsung_Text.clear()
        self.Save_Text.clear()
        self.progressBar.setValue(0)
        self.Download_Button.setEnabled(False)
        self.Save_Button.setEnabled(True)
        self.Save_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")

    def Download(self):
        self.Rest_Button.setEnabled(False)
        self.Rest_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

        self.Download_Button.setEnabled(False)
        self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

        save_location = self.save_location
        samsung_id = self.Samsung_Text.text().strip()
        if not samsung_id:
            self.show_message("Error", "Please enter Samsung ID.", QMessageBox.Warning)
            return

        url = f"http://sbuservice.samsungmobile.com/BUWebServiceProc.asmx/GetContents?platformID={samsung_id}&PartNumber=AAAA"
        max_retries = 5
        delay = 1
        for attempt in range(max_retries):
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    content = response.text
                    match = re.search(r'<FilePathName>(.*?)</FilePathName>', content)
                    if match:
                        file = match.group(1)
                        for_download = f"http://sbuservice.samsungmobile.com/upload/BIOSUpdateItem/{file}"

                        file_path = os.path.join(save_location, file)
                        expected_size = int(requests.head(for_download).headers.get("Content-Length", 0))

                        if os.path.exists(file_path):
                            file_size = os.path.getsize(file_path)
                            if file_size < expected_size:
                                headers = {"Range": f"bytes={file_size}-"}
                                response = requests.get(for_download, headers=headers, stream=True)
                                response.raise_for_status()

                                with open(file_path, "ab") as f:
                                    self.progressBar.setMaximum(expected_size)
                                    self.progressBar.setValue(file_size)
                                    for chunk in response.iter_content(chunk_size=8192):
                                        if chunk:
                                            f.write(chunk)
                                            self.progressBar.setValue(self.progressBar.value() + len(chunk))
                                            QApplication.processEvents()
                                self.show_message("Success", "File downloaded successfully.")
                                self.open_file(save_location)
                            else:
                                self.show_message("Info", "File already downloaded.")
                                self.open_file(save_location)
                        else:
                            response = requests.get(for_download, stream=True)
                            with open(file_path, "wb") as f:
                                self.progressBar.setMaximum(expected_size)
                                self.progressBar.setValue(0)
                                for chunk in response.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                                        self.progressBar.setValue(self.progressBar.value() + len(chunk))
                                        QApplication.processEvents()

                            self.show_message("Success", "File downloaded successfully.")
                            self.open_file(save_location)
                    else:
                        self.show_message("File Not Found","Please Change The Samsung ID ",QMessageBox.Critical)
                break  # Exit the retry loop if successful
            except Exception as e:
                self.show_message("Error", f"Error downloading file: {e}", QMessageBox.Critical)
                if attempt < max_retries - 1:
                    time.sleep(delay)

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStyleSheet("background:white;color:black")
        msg_box.exec_()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
