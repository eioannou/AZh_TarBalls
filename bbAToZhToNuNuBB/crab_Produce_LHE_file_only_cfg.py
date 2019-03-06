from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "LHEProduction_M1000"
config.General.workArea = 'crab_LHEProduction'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Produce_LHE_file_only.py'
#config.JobType.generator = 'lhe'
config.JobType.inputFiles = ['../GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh','bbAToZhToNuNubbbb_4f_M1000_tarball.tar.xz' ]
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
#config.Data.outputPrimaryDataset = 'privateMCProductionLHEGEN'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 100000
config.Data.publication = False
#config.Data.outputDatasetTag = 'eventLHEGEN-AToZhToNuNuBB_01j_4f_M225_tarball.tar-2017060614061496751112'
#config.Data.outLFNDirBase = '/store/group/phys_higgs'

config.section_("Site")
#config.Site.storageSite = 'T2_DE_DESY'
#config.Site.storageSite = 'T2_CN_Beijing'
#config.Site.whitelist = ['T2_*']
config.Site.storageSite = 'T2_CH_CERN'

#config.section_("User")
## only german users
#config.User.voGroup = "dcms"

