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
        # Central Widget Open
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # Drag And Drop Area.....
        self.Drag_Drop = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Drag_Drop.setGeometry(QtCore.QRect(110, 20, 351, 91))
        self.Drag_Drop.setObjectName("Drag_Drop")
        self.Drag_Drop.setPlaceholderText("Drag Your File Here")
        self.Drag_Drop.setStyleSheet("background: rgb(176, 196, 222);font:25 italic 16pt Calibri;border-radius:20px")
        # Connect drag-and-drop events
        self.Drag_Drop.setAcceptDrops(True)
        self.Drag_Drop.dragEnterEvent = self.dragEnterEvent
        self.Drag_Drop.dropEvent = self.dropEvent
        # SAMSUNG ID Label....
        self.SamsungID_label = QtWidgets.QLabel(self.centralwidget)
        self.SamsungID_label.setGeometry(QtCore.QRect(0, 150, 121, 31))
    
        self.SamsungID_label.setStyleSheet("font: 87 11pt Arial Black;color:rgb(255, 255, 255);")
        self.SamsungID_label.setObjectName("SamsungID_label")

        # Samsung id Entry...
        self.Samsung_Id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Samsung_Id_lineEdit.setGeometry(QtCore.QRect(110, 150, 351, 31))
        self.Samsung_Id_lineEdit.setObjectName("Samsung_Id_lineEdit")
        self.Samsung_Id_lineEdit.setStyleSheet("border-radius:15px")
        self.Samsung_Id_lineEdit.setPlaceholderText("Enter PlateFrom ID:")
        self.Samsung_Id_lineEdit.textChanged.connect(self.on_text_changed)
        # Save to Label...
        self.SAveTo_label = QtWidgets.QLabel(self.centralwidget)
        self.SAveTo_label.setGeometry(QtCore.QRect(20, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SAveTo_label.setFont(font)
        self.SAveTo_label.setStyleSheet("font: 87 11pt Arial Black;color:rgb(255, 255, 255);")
        self.SAveTo_label.setObjectName("SAveTo_label")


        # Save To Entry....
        self.Save_To_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Save_To_lineEdit.setGeometry(QtCore.QRect(110, 200, 351, 31))
        self.Save_To_lineEdit.setObjectName("Save_To_lineEdit")
        self.Save_To_lineEdit.setStyleSheet("border-radius:15px")
        # Set Button....
        self.SET_Button = QtWidgets.QPushButton(self.centralwidget)
        #self.SET_Button.setGeometry(QtCore.QRect(240, 250, 91, 41))
        self.SET_Button.setIcon(QtGui.QIcon("s.png"))
        self.SET_Button.setIconSize(QtCore.QSize(35,60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SET_Button.setFont(font)
        self.SET_Button.setGeometry(QtCore.QRect(160, 250, 91, 41))
        self.SET_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.SET_Button.setObjectName("SET_Button")
        self.SET_Button.clicked.connect(self.set)

        # Download Button...
        self.Download_Button = QtWidgets.QPushButton(self.centralwidget)
        #self.Download_Button.setGeometry(QtCore.QRect(240, 360, 125, 41))
        self.Download_Button.setIcon(QtGui.QIcon("d.png"))
        self.Download_Button.setIconSize(QtCore.QSize(35,60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Download_Button.setFont(font)
        self.Download_Button.setGeometry(QtCore.QRect(290, 250, 128, 41))
        self.Download_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.Download_Button.setObjectName("Download_Button")
        self.Download_Button.clicked.connect(self.Download)
        self.Download_Button.setEnabled(False)
        self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")
        #REST BUTTON
        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(230, 360, 110, 41))
        self.Reset_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        self.Reset_Button.setObjectName("REST")
        self.Reset_Button.clicked.connect(self.Reset)

        # Progress Bar...
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 330, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        #self.progressBar.setStyleSheet("border-radius:5px")

        # Central Widget End
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.Download_Button.setText(_translate("MainWindow","Download"))
        self.SamsungID_label.setText(_translate("MainWindow", "Samsung Id:"))
        self.SET_Button.setText(_translate("MainWindow", "SAVE"))
        self.SAveTo_label.setText(_translate("MainWindow", "Save To:"))
        self.Reset_Button.setText(_translate("MainWindow","RESET"))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile())
            self.handle_file(file_path)
            file_path1=file_path[-10:]
            self.Drag_Drop.setPlainText(file_path1)
            self.show_message("Dropped file", f"Dropped file: {file_path1}")

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
                    self.Samsung_Id_lineEdit.clear()
                    self.Samsung_Id_lineEdit.setText(samsung_id)
                    self.Download_Button.setEnabled(True)
                    self.samsung_id = samsung_id
                    self.show_message("Detect", f"Samsung ID: {samsung_id}")
                else:
                    self.show_message("Error", "Samsung ID not found in the file.", QMessageBox.Warning)
        except Exception as e:
            self.show_message("Error", f"Error reading file: {e}", QMessageBox.Critical)

    def set(self):
        save_location = QFileDialog.getExistingDirectory(self)
        if save_location:
            self.Save_To_lineEdit.clear()
            self.Save_To_lineEdit.setText(save_location)
            self.save_to_json(save_location)
            self.Download_Button.setEnabled(False)
            self.SET_Button.setEnabled(False)
            self.SET_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")
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
                    self.Save_To_lineEdit.clear()
                    self.Save_To_lineEdit.setText(save_location)
                    self.SET_Button.setEnabled(False)
                    self.SET_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")
                    self.save_location = save_location
        except FileNotFoundError:
            with open("save_location.json", "w") as f:
                pass
    def open_explorer(self,path):
        system_plateform=platform.system()
        if system_plateform =="Windows":
            os.startfile(path)
        elif system_plateform == "Linux":
            os.startfile(path)
        #ADD MORE OS
        else:
            self.show_message("Invalid OS")


    def on_text_changed(self):
        text = self.Samsung_Id_lineEdit.text().strip()
        if len(text)==3:
            self.Download_Button.setEnabled(True)
            self.Download_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")
        else:
            self.Download_Button.setEnabled(False)
            self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

    def Reset(self):
        self.Drag_Drop.clear()
        self.Samsung_Id_lineEdit.clear()
        self.Save_To_lineEdit.clear()
        self.progressBar.setValue(0)
        self.Download_Button.setEnabled(False)
        self.SET_Button.setEnabled(True)
        self.SET_Button.setStyleSheet("border-radius:20px;background:rgb(29, 220, 20);color:rgb(255, 255, 255)")


    def Download(self):
        self.Reset_Button.setEnabled(False)
        self.Reset_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")

        self.Download_Button.setEnabled(False)
        self.Download_Button.setStyleSheet("border-radius:20px;background:red;color:rgb(255, 255, 255)")
        try:
            samsung_id= self.Samsung_Id_lineEdit.text().strip()
            if not samsung_id:
                self.show_message("Error", "Please enter a Samsung ID", QMessageBox.Warning)
                return
            save_location = self.save_location

        except AttributeError:
            self.show_message("Error", "Samsung ID or save location not set.", QMessageBox.Critical)
            return

        url = f"http://sbuservice.samsungmobile.com/BUWebServiceProc.asmx/GetContents?platformID={samsung_id}&PartNumber=AAAA"
        max_retries = 10
        retry_delay = 1

        for attempt in range(max_retries):
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    content = response.text
                    match = re.search(r'<FilePathName>(.*?)</FilePathName>', content)
                    version=re.search(r'<Version>(.*?)</Version>',content)
                    if (match):
                        file = match.group(1)
                    if version:
                        ver = version.group(1)
                        self.show_message("Version", f"The File Version is: {ver}")
                        
                        for_download = f"http://sbuservice.samsungmobile.com/upload/BIOSUpdateItem/{file}"
                        file_path = os.path.join(save_location, file)

                        if os.path.exists(file_path):
                            file_size = os.path.getsize(file_path)
                            headers = requests.head(for_download).headers
                            expected_size = int(headers.get('Content-Length', 0))

                            if file_size < expected_size:
                                #self.show_message("Download", "Resuming download...")
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
                                self.show_message("Sucess", f"File {file} downloaded successfully")
                                self.open_explorer(save_location)
                                #self.show_message("Download", f"File {file} resumed downloading.")
                            else:
                                self.show_message("Sucess", "File already fully downloaded.")
                                self.open_explorer(save_location)
                        else:
                            response = requests.get(for_download, stream=True)
                            expected_size = int(response.headers.get('Content-Length', 0))
                            self.progressBar.setMaximum(expected_size)
                            self.progressBar.setValue(0)
                            with open(file_path, 'wb') as f:
                                for chunk in response.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                                        self.progressBar.setValue(self.progressBar.value() + len(chunk))
                                        QApplication.processEvents()
                            self.show_message("Sucess", f"File {file} downloaded successfully")
                            self.open_explorer(save_location)
                        break
                    else:
                        self.show_message("Error", "File not found", QMessageBox.Warning)
                        break
                else:
                    self.show_message("Error", "Failed to connect to server", QMessageBox.Warning)
            except requests.exceptions.RequestException as e:
                self.show_message("Error", f"Error occurred during attempt {attempt + 1}: {e}", QMessageBox.Warning)
            except IOError as e:
                self.show_message("Error", f"Error occurred while handling files: {e}", QMessageBox.Critical)
            if attempt < max_retries - 1:
                #self.show_message("Retry", f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                self.show_message("Error", "Maximum retries reached. Exiting...", QMessageBox.Critical)
                break

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
