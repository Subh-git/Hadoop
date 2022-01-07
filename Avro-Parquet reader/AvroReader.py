# Python 3 with `avro-python3` package available
 
import copy
import json
import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader


# Read data from an avro file
with open('AvroSample.avro', 'rb') as f:
    reader = DataFileReader(f, DatumReader())
    metadata = copy.deepcopy(reader.meta)
    schema_from_file = json.loads(metadata['avro.schema'])
    users = [user for user in reader]
    reader.close()


print(f'Users:\n {users}')