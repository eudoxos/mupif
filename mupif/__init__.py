#
#               MuPIF: Multi-Physics Integration Framework 
#                   Copyright (C) 2010-2015 Borek Patzak
#
#       Czech Technical University, Faculty of Civil Engineering,
#       Department of Mechanics, 166 29 Prague, Czech Republic
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#

"""
This is a MuPIF module (Multi-Physics Integration Framework)
"""
# Major.Minor.Patch
__version__ = '2.1.0'
__author__ = 'Borek Patzak and Vit Smilauer'

from .fieldID import FieldID
from .propertyID import PropertyID
from .functionID import FunctionID
from .valueType import ValueType

from . import APIError
from . import Application
from . import BBox
from . import CellGeometryType
from . import Cell
from . import EnsightReader2
from . import Field
from . import Function
from . import IntegrationRule
from . import JobManager
from . import SimpleJobManager
from . import Localizer
from . import Mesh
from . import Octree
from . import operatorUtil
from . import Property
from . import PyroUtil
from . import Timer
from . import TimeStep
from . import Util
from . import Vertex
from . import VtkReader2
from . import RemoteAppRecord
from . import PyroFile
from . import MupifObject
from . import Workflow
from . import MetadataKeys
from . import Physics


# List all submodules, so they can all be imported: from mupif import *
__all__ = ['APIError', 'Application', 'BBox', 'CellGeometryType', 'Cell', 'EnsightReader2', 'FieldID', 'Field',
           'FunctionID', 'Function', 'IntegrationRule', 'JobManager', 'SimpleJobManager', 'Localizer', 'Mesh', 'Octree',
           'operatorUtil', 'PropertyID', 'Property', 'PyroUtil', 'Timer', 'TimeStep', 'Util', 'ValueType', 'Vertex',
           'VtkReader2', 'RemoteAppRecord', 'PyroFile', 'MupifObject','Workflow', 'MetadataKeys', 'Physics']

from . import Util
import logging
import os

# Create default logger
Util.setupLogger(fileName='mupif.log', level=logging.DEBUG if 'TRAVIS' in os.environ else logging.DEBUG)

# # temporarily disabled (does not work on travis, even though future is installed there??)
# # more helpful error message
# try: import future, builtins
# except ImportError:
# 	print("ERROR: mupif requires builtins and future modules; install both via 'pip install future'")
# 	raise
