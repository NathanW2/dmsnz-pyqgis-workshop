from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_templatedock import Ui_DockWidget

items = {
    "water pipe - 100mm":
        {
            "type": "water pipe",
            "size": 100
        },
    "sewer pipe - 200mm":
        {
            "type": "sewer pipe",
            "size": 200
        }
}


class TemplateDock(Ui_DockWidget, QDockWidget):
    templateApplied = pyqtSignal(str, dict)

    def __init__(self, parent=None):
        super(TemplateDock, self).__init__(parent)
        self.setupUi(self)
        self.applyButton.pressed.connect(self.apply_template)

    def apply_template(self):
        # Don't do anything if there is no selection text
        if not self.templatesList.currentItem():
            return

        name = self.templatesList.currentItem().text()

        # Get the fields from the items list
        fields = items[name]
        self.templateApplied.emit(name, fields)

    def load_items(self):
        self.templatesList.clear()
        for key in items:
            self.templatesList.addItem(key)


class PluginCore:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.dock = TemplateDock()
        self.dock.templateApplied.connect(self.apply_template)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.dock.hide()

        self.action = QAction("Go!", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def apply_template(self, name, fields):
        layer = self.iface.activeLayer()
        features = layer.selectedFeatures()
        for feature in features:
            for field, value in fields.iteritems():
                feature[field] = value
                layer.updateFeature(feature)

        self.iface.mapCanvas().refresh()

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
        self.iface.removeDockWidget(self.dock)

    def run(self):
        self.dock.load_items()
        self.dock.show()

