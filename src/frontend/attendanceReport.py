import sys
from PyQt5 import QtWidgets  
from PyQt5 import QtCore, QtGui 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import pandas as pd
import openpyxl



from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import QStandardPaths
import os

import sys
sys.path.insert(0, "src\\frontend\\attendanceReport.ui")


class Report(QMainWindow):

    def __init__(self, homepage):
        super(Report, self).__init__()

        uic.loadUi("src\\frontend\\attendanceReport.ui", self)
        self.file_name = ""
        
        self.load_data(self.tableWidget, self.file_name) #loads data in table
        self.pushButton.clicked.connect(self.roomInfo) #links back to info page
        self.pushButton_2.clicked.connect(self.download_report) #downloads report in excel format
        
        self.show()


    #Function for downloading Excel Sheet
    def download_report(self, file_name):
        columnHeaders = []

        # create column header list
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # create dataframe object recordset
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()
        
        df.to_excel('Dummy File XYZ.xlsx', index=False)
        print('Excel file exported')

    #displays data on the report table
    def load_data(self, tableWidget, file_name):
        path = "src\\frontend\dummy.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        list_values = list(sheet.values)

        self.tableWidget.setRowCount(len(list_values))
        self.tableWidget.setColumnCount(len(list_values))

        if path:
            # Read Excel file using pandas
            df = pd.read_excel(path)

            # Set number of rows and columns in the table
            self.tableWidget.setRowCount(df.shape[0])
            self.tableWidget.setColumnCount(df.shape[1])

            # Populate the table with data
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iat[row, col]))
                    self.tableWidget.setItem(row, col, item)
       
        self.file_name = path

    #Loads Download Report Page
    def roomInfo(self):
       uic.loadUi("src\\frontend\\roomInfo.ui", self)
    

def main():
    app = QApplication([])
    homepage = QtWidgets.QDialog()
    window = Report(homepage)
    app.exec()  


if __name__ == '__main__':
    main()
 