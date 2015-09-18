from plugincore import PluginCore


def classFactory(iface):
    """
    Main entry point for the QGIS plugin.  QGIS calls me and passes an instance of the interface object which
    can be used to talk to the main QGIS interface.
    :param iface: The API interface object used to talk to QGIS
    :return: A instance of the main class used by your plugin
    """
    return PluginCore(iface)


