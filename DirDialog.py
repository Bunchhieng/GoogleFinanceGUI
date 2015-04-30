from PyQt4 import QtGui
import os
from PyQt4.QtGui import QFileDialog, QWidget

__author__ = 'Bunchhieng'

class DirDialog(QWidget):
    def __init__(self):
        super(DirDialog, self).__init__()
        self.onClicked_open_dir()

    def onClicked_open_dir(self):
        self.foldername = QFileDialog.getExistingDirectory(self,
                                         "Select Directory",
                                         os.path.expanduser("~"),
                                         QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks,)