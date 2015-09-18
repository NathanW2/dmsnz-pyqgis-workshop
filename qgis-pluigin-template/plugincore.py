from PyQt4.QtGui import *
from PyQt4.QtCore import *


class PluginCore:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction("Go!", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        QMessageBox.information(None, "Minimal plugin", "Do something useful here")

