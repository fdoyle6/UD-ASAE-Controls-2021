# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PyQt5 import QtWidgets # import PyQt5 widgets
import sys
from LoadScreen import Ui_LoadScreen

# Create the application object
app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QMainWindow()
# Create the form object
ui = Ui_MainWindow()
ui.setupUi(first_window)
# Set window size


# Set the form title


# Show form
first_window.show()

# Run the program
sys.exit(app.exec())
