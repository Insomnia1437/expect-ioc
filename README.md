# expect-ioc

Use `pexpect` to interact with epics IOC

```shell
$ ~/.local/python3/bin/python3 ioc.py
before:
#!/home/sdcswd/epics/R7.0.8/base/bin/linux-x86_64/softIocPVA
dbLoadRecords "test.db"
coreRelease()
############################################################################
## EPICS R7.0.8
## Rev. 2024-03-27T10:23+0100
## Rev. Date build date/time:
############################################################################

after:
epics>
before:
 dbl
ai1
ao1

after:
epics>
before:
 help
#               ClockTime_Report                asDumpHash      asInit
asSetFilename   asSetSubstitutions              ascar           asdbdump
asphag          aspmem          asprules        aspuag          astac
callbackParallelThreads         callbackQueueShow
callbackSetQueueSize            casr            cd              coreRelease
date            dbCreateAlias   dbDumpBreaktable                dbDumpDevice
dbDumpDriver    dbDumpField     dbDumpFunction  dbDumpLink      dbDumpMenu
dbDumpPath      dbDumpRecord    dbDumpRecordType
dbDumpRegistrar dbDumpVariable  dbLoadDatabase  dbLoadGroup     dbLoadRecords
dbLoadTemplate  dbLockShowLocked                dbNotifyDump    dbPutAttribute
dbPvdDump       dbPvdTableSize  dbReportDeviceConfig            dbStateClear
dbStateCreate   dbStateSet      dbStateShow     dbStateShowAll  dba
dbap            dbb             dbc             dbcar           dbd
dbel            dbgf            dbgl            dbgrep          dbhcr
dbior           dbjlr           dbl             dbla            dbli
dblsr           dbnr            dbp             dbpf            dbpr
dbpvar          dbs             dbsr            dbstat          dbtgf
dbtpf           dbtpn           dbtr            dlload          echo
eltc            epicsEnvSet     epicsEnvShow    epicsEnvUnset
epicsMutexShowAll               epicsParamShow  epicsPrtEnvParams
epicsThreadResume               epicsThreadShow epicsThreadShowAll
epicsThreadSleep                errlog          errlogInit      errlogInit2
exit            generalTimeReport               gft             help
installLastResortEventProvider  iocBuild        iocInit         iocLogInit
iocLogPrefix    iocLogShow      iocPause        iocRun          iocshCmd
iocshLoad       iocshRun        on              pft             postEvent
pval            pvasr           pwd             refdiff         refmon
refsave         refshow         registerAllRecordDeviceDrivers
registryDeviceSupportFind       registryDriverSupportFind       registryDump
registryFunctionFind            registryRecordTypeFind
scanOnceQueueShow               scanOnceSetQueueSize            scanpel
scanpiol        scanppl         setIocLogDisable
softIocPVA_registerRecordDeviceDriver           startPVAServer  stopPVAServer
system          taskwdShow      tpn             var

Type 'help <command>' to see the arguments of <command>.  eg. 'help db*'

after:
epics>
```