import argparse
import codecs
import datetime
import json
import sys
import types
try:
    BrokenPipeError
except NameError:
    import socket
    BrokenPipeError = socket.error

import fitparse

class RecordJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, types.GeneratorType):
            return list(obj)
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, fitparse.DataMessage):
            return {
                "type": obj.name,
                "data": {
                    data.name: data.value for data in obj
                }
            }
        # Fall back to original to raise a TypeError
        return super(RecordJSONEncoder, self).default(obj)



def readfitfile(fname):
    # print(options)
    fitfile = fitparse.FitFile(
        fname,
        data_processor=fitparse.StandardUnitsDataProcessor(),
        check_crc = not(None),
    )
    records = fitfile.get_messages(
        name=None,
        with_definitions=False,
        as_dict=False

    )
    return records

filelist = [ '9BF94538.FIT','9BEA1514.FIT']


for fname in filelist:
  print("="*20)
  print(fname)
  records=readfitfile(fname)
  for r in records:
      json.dump(r, fp=sys.stdout, cls=RecordJSONEncoder)
