#!/usr/bin/python -tt
# -*- coding: iso-8859-15 -*-

__version__="1.0"

import pymetar
import sys

#print "pymet v%s using pymetar lib v%s"%(__version__,pymetar.__version__)

if len(sys.argv)<2 or sys.argv[1]=="--help":
    sys.stderr.write("Usage: %s <station id>\n"% sys.argv[0])
    sys.stderr.write("Station IDs can be found at: http://www.nws.noaa.gov/tg/siteloc.shtml\n")
    sys.exit(1)
elif (sys.argv[1] == "--version"):
    print "pmw v%s using pymetar lib v%s"%(__version__,pymetar.__version__)
    sys.exit(0)
else:
    station=sys.argv[1]

try:
    rf=pymetar.ReportFetcher(station)
    rep=rf.FetchReport()
except Exception, e:
    sys.stderr.write("Something went wrong when fetching the report.\n")
    sys.stderr.write("These usually are transient problems if the station ")
    sys.stderr.write("ID is valid. \nThe error encountered was:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

rp=pymetar.ReportParser()
pr=rp.ParseReport(rep)

print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (pr.getStationName(), pr.getISOTime(), pr.getTemperatureCelsius(), pr.getHumidity(), pr.getWindSpeed(), pr.getWindSpeedBeaufort(), pr.getWindCompass(), pr.getPressure(), pr.getDewPointCelsius(), pr.getWeather(), pr.getSkyConditions())
