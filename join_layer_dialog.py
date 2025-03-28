# -*- coding: utf-8 -*-
"""
/***************************************************************************
 JoinLayerDialog
                                 A QGIS plugin
 This code is a QGIS plugin that functions to split polygon layers using a line layer as the cutting centerline. The plugin works by identifying polygon and centerline layers loaded in QGIS, then using GeoPandas and Shapely to process the geometry.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-17
        git sha              : $Format:%H$
        copyright            : (C) 2025 by Muhammad Ihsan
        email                : muhammad.ihsan@upi.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'join_layer_dialog_base.ui'))


class JoinLayerDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(JoinLayerDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
