# -*- coding: utf-8 -*-
"""
/***************************************************************************
 URockPostprocessor
                                 A QGIS plugin
 Post process results of URock plugin
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-01-19
        copyright            : (C) 2022 by Jérémy Bernard, University of Gothenburg
        email                : jeremy.bernard@zaclys.net
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

__author__ = 'Jérémy Bernard, University of Gothenburg'
__date__ = '2022-01-19'
__copyright__ = '(C) 2022 by Jérémy Bernard, University of Gothenburg'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load URockPostprocessor class from file URockPostprocessor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .urock_postprocessor import URockPostprocessorPlugin
    return URockPostprocessorPlugin()
