from builtins import range
from mupif import Application
from mupif import TimeStep
from mupif import APIError
from mupif import PropertyID
from mupif import FieldID
from mupif import Mesh
from mupif import Field
from mupif import ValueType
from mupif import Vertex
from mupif import Cell
from mupif import PyroUtil
from mupif import Property
from mupif import IntegrationRule

class DemoApplication (Application.Application):
    """
    Simple application that computes min and max values of the field
    """
    def __init__(self, file, workdir):
        super(DemoApplication, self).__init__(file, workdir)
        self.count = 0
        self.daemonRunning = True

    def setProperty(self, property, objectID=0):
        propID = property.getPropertyID()
        if (propID == PropertyID.PID_Demo_Value):
            self.count = property
        else:
            raise APIError.APIError ('Unknown property ID')

    def solveStep(self, tstep, stageID=0, runInBackground=False):
        arry = [];
        val = 0
        for i in range (10000):
            arry.append(i)
        for i in range (self.count.getValue()):
            for j in range (10000):
                val = val+arry[j]

    def getProperty(self, propID, time, objectID=0):
        if (propID == PropertyID.PID_Demo_Value):
            return Property.ConstantProperty(self.count, PropertyID.PID_Demo_Value, ValueType.Scalar, PQ.getDimensionlessUnit())
        else:
            raise APIError.APIError ('Unknown property ID')

    def getApplicationSignature(self):
        return "DemoApplication, ver 1.0"
    
