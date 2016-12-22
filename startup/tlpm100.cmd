require tlpm100

epicsEnvSet("PREFIX",   "PM100")

#var streamDebug 1

# usbtmcConfigure(port, vendorNum, productNum, serialNumberStr, priority, flags)
usbtmcConfigure("PM100")
asynSetTraceIOMask("PM100",0,0xff)
#asynSetTraceMask("PM100",0,0xff)

# Load record instances
dbLoadRecords("tlPM100.template","P=$(PREFIX):,R=,PORT=$(PREFIX)")
dbLoadRecords("asynRecord.db",   "P=$(PREFIX):,R=asyn,PORT=$(PREFIX),ADDR=0,OMAX=100,IMAX=100")
