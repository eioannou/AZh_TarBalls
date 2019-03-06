import FWCore.ParameterSet.Config as cms

process = cms.Process("LHE")

process.load("IOMC.RandomEngine.IOMC_cff")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.EventContent.EventContent_cff')

process.source = cms.Source("EmptySource"
                            )

process.load("GeneratorInterface.LHEInterface.ExternalLHEAsciiDumper_cfi")
process.externalLHEAsciiDumper.lheFileName = cms.string('output.lhe')
#process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = 21
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )

process.load("Configuration.GenProduction.LHE_Producer_bbAToZhToNuNuBB_M1000_cff")

process.externalLHEProducer.nEvents = process.maxEvents.input.value()
process.externalLHEProducer.outputFile = cms.string('cmsgrid_final.lhe')

process.externalLHEProducer.args = cms.vstring('../bbAToZhToNuNubbbb_4f_M1000_tarball.tar.xz')

process.out = cms.OutputModule("PoolOutputModule",
                               splitLevel = cms.untracked.int32(0),
                               eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                               outputCommands = process.LHEEventContent.outputCommands,
                               fileName = cms.untracked.string('lheoutputfile.root'),
                               dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
        )
                               )

process.lhe_step = cms.Path(process.externalLHEProducer)
process.endjob_step = cms.EndPath(process.externalLHEAsciiDumper)
process.LHE_output = cms.EndPath(process.out)

#process.schedule = cms.Schedule(process.lhe_step,process.endjob_step)

