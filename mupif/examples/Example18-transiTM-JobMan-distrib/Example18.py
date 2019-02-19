#!/usr/bin/env python3
import sys
sys.path.extend(['..', '../../..'])
from mupif import *
import argparse
import mupif.Physics.PhysicalQuantities as PQ

#Read int for mode as number behind '-m' argument: 0-local (default), 1-ssh, 2-VPN 
mode = argparse.ArgumentParser(parents=[Util.getParentParser()]).parse_args().mode
from Config import config
cfg=config(mode)

import logging
log = logging.getLogger()

class Demo18(Workflow.Workflow):
   
    def __init__ (self, targetTime=PQ.PhysicalQuantity(0.,'s')):
        super(Demo18, self).__init__(targetTime=targetTime)

    def initialize(self):
        #locate nameserver
        ns = PyroUtil.connectNameServer(nshost=cfg.nshost, nsport=cfg.nsport, hkey=cfg.hkey)
        #connect to JobManager running on (remote) server and create a tunnel to it
        self.thermalJobMan = PyroUtil.connectJobManager(ns, cfg.jobManName, cfg.hkey)
        self.thermal = None
        self.mechanical = None
        
        try:
            self.thermal = PyroUtil.allocateApplicationWithJobManager( ns, self.thermalJobMan, cfg.jobNatPorts[0], cfg.hkey, PyroUtil.SSHContext(sshClient=cfg.sshClient, options=cfg.options, sshHost=cfg.sshHost ) )
            log.info('Created thermal job')
        except Exception as e:
            log.exception(e)

        appsig=self.thermal.getApplicationSignature()
        log.info("Working thermal server " + appsig)
        
        self.mechanical = PyroUtil.connectApp(ns, 'mechanical', cfg.hkey)
        appsig=self.mechanical.getApplicationSignature()
        log.info("Working mechanical server " + appsig)


    def solveStep(self, istep, stageID=0, runInBackground=False):

        self.thermal.solveStep(istep)
        f = self.thermal.getField(FieldID.FID_Temperature, self.mechanical.getAssemblyTime(istep))
        data = f.field2VTKData().tofile('T_%s'%str(istep.getNumber()))
        
        self.mechanical.setField(f)
        sol = self.mechanical.solveStep(istep) 
        f = self.mechanical.getField(FieldID.FID_Displacement, istep.getTime())
        data = f.field2VTKData().tofile('M_%s'%str(istep.getNumber()))
        
        self.thermal.finishStep(istep)
        self.mechanical.finishStep(istep)

    def getCriticalTimeStep(self):
        # determine critical time step
        return min (self.thermal.getCriticalTimeStep(), self.mechanical.getCriticalTimeStep())

    def terminate(self):
        #self.thermalAppRec.terminateAll()
        self.thermal.terminate()
        self.thermalJobMan.terminate()
        self.mechanical.terminate()
        super(Demo18, self).terminate()

    def getApplicationSignature(self):
        return "Demo18 workflow 1.0"

    def getAPIVersion(self):
        return "1.0"
    
if __name__=='__main__':
    try:
        demo = Demo18(targetTime=PQ.PhysicalQuantity(2.,'s'))
        demo.initialize()
        demo.solve()
        log.info("Test OK")
    except:
        log.info("Test FAILED")


