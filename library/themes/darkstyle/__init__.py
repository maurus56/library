from themes.darkstyle.palette import DarkPalette
import warnings
import logging

def _logger():
    return logging.getLogger('darkstyle')

def _apply_palette_fix(QCoreApplication, QPalette, QColor):
    """Apply application level fixes on the QPalette."""
    # See issue #139
    color = DarkPalette.COLOR_SELECTION_LIGHT
    qcolor = QColor(color)
    app = QCoreApplication.instance()

    if app:
        palette = app.palette()
        palette.setColor(QPalette.Normal, QPalette.Link, qcolor)
        app.setPalette(palette)

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
    import themes.darkstyle.pyqt5_style_rc

    # Load the stylesheet content from resources
    from PyQt5.QtCore import QCoreApplication, QFile, QTextStream
    from PyQt5.QtGui import QColor, QPalette

    # Apply palette fix. See issue #139
    _apply_palette_fix(QCoreApplication, QPalette, QColor)

    f = QFile(":/darkstyle/style.qss")
    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()

        return stylesheet