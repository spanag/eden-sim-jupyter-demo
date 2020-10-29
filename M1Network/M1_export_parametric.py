import M1  # import parameters file
from netpyne import sim  # import netpyne sim module
import math
import sys
import time

import netpyne
netpyne.__gui__ = False



net_scale = 0.01
do_simulate = False
disable_output = True

argv = sys.argv

if argv[1] == '-python':
    argv = argv[3:]

net_scale = float( argv[1] )
if not ( 0 < net_scale and net_scale <= 1 ):
    raise ValueError('wrong scale')

if len(argv) >= 3:
    if argv[2] == 'sim':
        print('Simulation selected...')
        do_simulate = True

netparms = M1.netParams
netparms.scale = net_scale
netparms.sizeX = 300*math.sqrt(netparms.scale) # x-dimension (horizontal length) size in um
netparms.sizeZ = 300*math.sqrt(netparms.scale) # z-dimension (horizontal depth) size in um

netparms = M1.netParams
print("********************\n*\n*  Note: setting noise to 1, since noise can only be 0 or 1 in NeuroML export currently!\n*\n********************")
netparms.stimSourceParams['background_E']['noise'] = 1
netparms.stimSourceParams['background_I']['noise'] = 1

if disable_output:
    M1.simConfig.analysis = {}
    M1.simConfig.recordTraces = {}
    M1.simConfig.recordCellsSpikes = []


if do_simulate:
    tic = time.time()
    sim.create(netparms, M1.simConfig, output=False)
    sim.runSim()
    
    print( sim.simData, len(sim.simData['spkid'] ) )
    
    print( sim.timingData )
    # print( len(sim.simData) )
    # print( len( sim.simData['V']['cell_10'] ) )
    # print( M1.simConfig.analysis )
    # print( sim.simData['spkid'] )
    # print( len( sim.simData['spkid'] ) )
    # print( [ x for x in sim.simData['V']['cell_10'] ] )
else:
    sim.createExportNeuroML2(netParams = netparms, 
        simConfig = M1.simConfig,
        reference = ('M1_p_%dpercent') % ( int(net_scale * 100) ),
        connections=True,
        stimulations=True,
        #format='hdf5'  
    )  # create and export network to NeuroML 2


