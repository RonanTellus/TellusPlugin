# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TellusProcessing
                                 A QGIS plugin
 Module de traitement de données
                             -------------------
        begin                : 2018-03-12
        copyright            : (C) 2018 by ISTIC
        email                : dimas.espinasse@etudiant.univ-rennes1.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TellusProcessing class from file TellusProcessing.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .tellus_processing import TellusProcessing
    return TellusProcessing(iface)
