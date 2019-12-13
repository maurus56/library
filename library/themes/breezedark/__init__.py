import warnings
import logging

def _logger():
    return logging.getLogger('breezelight')

def load_stylesheet():
    """
    Load the stylesheet for use in a pyqt5 application.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt5() will be deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and "
        "use load_stylesheet()",
        PendingDeprecationWarning
    )

    # Smart import of the rc file
    import themes.breezedark.breeze_resources

    # Load the stylesheet content from resources
    from PyQt5.QtCore import QCoreApplication, QFile, QTextStream
    from PyQt5.QtGui import QColor, QPalette

    f = QFile(":/breezedark/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()

        # Apply OS specific patches
        # stylesheet = _apply_stylesheet_patches(stylesheet)
        return stylesheet