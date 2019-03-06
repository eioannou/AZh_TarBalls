import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/a/aioannou/GenProductions/genproductions/bin/MadGraph5_aMCatNLO/FixingStation/bbAToZhToNuNuBB_gridpacks/bbAToZhToNuNubbbb_4f_M500_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#
  
#from Configuration.Generator.Pythia8CommonSettings_cfi import *
#from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
#from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

#generator = cms.EDFilter("Pythia8HadronizerFilter",
#    maxEventsToPrint = cms.untracked.int32(1),
#    pythiaPylistVerbosity = cms.untracked.int32(1),
#    filterEfficiency = cms.untracked.double(1.0),
#    pythiaHepMCVerbosity = cms.untracked.bool(False),
#    comEnergy = cms.double(13000.),
#    PythiaParameters = cms.PSet(
#        pythia8CommonSettingsBlock,
#        pythia8CUEP8M1SettingsBlock,
#        processParameters = cms.vstring(
#            'JetMatching:setMad = off',
#            'JetMatching:scheme = 1',
#            'JetMatching:merge = on',
#            'JetMatching:jetAlgorithm = 2',
#            'JetMatching:etaJetMax = 5.',
#            'JetMatching:coneRadius = 1.',
#            'JetMatching:slowJetPower = 1',
#            'JetMatching:qCut = 20.', #this is the actual merging scale
#            'JetMatching:qCutME = 10.',#this must match the ptj cut in the lhe generation step (note: default PYTHIA8 = 10 GeV)
#            'JetMatching:nQmatch = 4', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
#            'JetMatching:nJetMax = 1', #number of partons in born matrix element for highest multiplicity
#            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
#            'TimeShower:mMaxGamma = 10.0', # switch back to default PYTHIA8 value, DYJet uses 4.0
#            #'SLHA:useDecayTable = off',
#            '25:m0 = 125.0',
#            '25:onMode = off',
#            '25:onIfMatch = 5 -5'
#        ),
#        parameterSets = cms.vstring('pythia8CommonSettings',
#                                    'pythia8CUEP8M1Settings',
##                                    'pythia8aMCatNLOSettings',
#                                    'processParameters',
#                                    )
#    )
#)
