#!usr/bin/env python3
#Copyright QTRAC Corp. wrote by Podmogilniy Ivan

""" Let to convert incidents from one filtype to other """

import pickle
import struct
import gzip
import datetime

GZIP_MAGIC = b"\x1F\x8B"

class IncidentError(Exception): pass

class Incident:

    def __init__(self, report_id, date, airport, aircraft_id,
                 aircraft_type, pilot_percent_hours_on_type,
                 pilot_total_hours, midair, narrative=""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1, \
               "Invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative

    @property
    def report_id(self):
    	return self.__report_id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        assert isinstance(date, datetime.date), "invalid date"
        self.__date = date

    @property
    def airport(self):
    	return self.__airport
    @airport.setter
    def airport(self, airport):
    	self.__airport = airport

    @property
    def aircraft_id(self):
    	return self.__aircraft_id
    @aircraft_id.setter
    def airport(self, aircraft_id):
    	self.__aircraft_id = aircraft_id

    @property
    def airport(self):
    	return self.__airport
    @airport.setter
    def airport(self, airport):
    	self.__airport = airport

    @property
    def aircraft_id(self):
        return self.__aircraft_id
    @aircraft_id.setter
    def aircraft_id(self, aircraft_id):
        self.__aircraft_id = aircraft_id

    @property
    def aircraft_type(self):
        return self.__aircraft_type
    @aircraft_type.setter
    def aircraft_type(self, aircraft_type):
        self.__aircraft_type = aircraft_type

    @property
    def pilot_percent_hours_on_type(self):
        return self.__pilot_percent_hours_on_type
    @pilot_percent_hours_on_type.setter
    def pilot_percent_hours_on_type(self, pilot_percent_hours_on_type):
        self.__pilot_percent_hours_on_type = pilot_percent_hours_on_type

    @property
    def pilot_total_hours(self):
        return self.__pilot_total_hours
    @pilot_total_hours.setter
    def pilot_total_hours(self, pilot_total_hours):
        self.__pilot_total_hours = pilot_total_hours

    @property
    def midair(self):
        return self.__midair
    @midair.setter
    def midair(self, midair):
        self.__midair = midair

    @property
    def narrative(self):
        return self.__narrative
    @narrative.setter
    def narrative(self, narrative):
        assert len(narrative) >= 5, 'Narrative length must be more than 5'
        self.__narrative = narrative

class IncidentCollection(dict):
    """docstring for IncidentCollection"""

    def values(self):
        for report_id in self.keys():
            yield self[report_id]

    def items(self):
        for report_id in self.keys():
            yield (report_id, self[report_id])

    def __iter__(self):
        for report_id in sorted(super().keys()):
            yield report_id

    keys = __iter__

    def export_pickle(self, filename, compress = False):
        "Doctstring for export_pickle"
        fh = None
        try:
            if compress:
                fh = gzip.open(filename, 'wb')
            else:
                fh = open(filename, 'wb')
                pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
                return True
        except (EnvironmentError, pickle.picklingError) as err:
            print('{0}: export error: {1}'.format(os.path.basename
                                            (sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_pickle(self, filename):
        "Doctstring for import_pickle"
        fh = None
        try:
            fh = open(filename, 'rb')
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename, 'rb')
            else:
                fh.seek(0)
                self.clear()
                self.update(pickle.load(fh))
            return True
        except (EnvironmentError, pickle.UnpicklingError) as err:
            print("{0}: import error: {1}". format(
			    os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def export_binary(self, filename, compress = False):
	"Doctstring for export_binary"

	def pack_string(string):
	    data = string.encode('utf-8')
	    format = '<H{0}s'.format(len(data))
	    return struct.pack(format, len(data), data)
	fh = None
	try:
            if compress:
                fh = gzip.open(filename, 'wb')
            else:
                fh = open(filename, 'wb')
            fh.write(MAGIC)
            fh.write(FORMAT_VERSION)
            for incident in self.values():
                data = bytearray()
                data.extend(











