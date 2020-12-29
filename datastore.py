import threading 
import time
from cachetools import TTLCache
import os
import json
import uuid

class Data :

    def __init__(self, filename = '####') :
        if filename == '####' :
            self.filename = 'DataStore/datastore_' + uuid.uuid4().hex + '.json'
            self.timefile = 'DataStore/timestore_' + uuid.uuid4().hex + '.json'

        if os.path.exists(filename) :
            self.lock = threading.Lock()
        else :
            self.filename = 'DataStore/'+ filename + '.json'
            self.timefile = 'DataStore/timestore.json'
            self.hashmap = dict()
            self.timetolive = dict()
            self.lock = threading.Lock()
            with open(self.filename, 'w') as fp :
                json.dump(self.hashmap, fp, indent=4)
                fp.close()

            with open(self.timefile, 'w') as sp :
                json.dump(self.timetolive, sp, indent=4)
                sp.close()
        
    def create(self, key, value, sec=25) :
        self.lock.acquire()

        with open(self.filename) as fp :
            data = json.load(fp)
            fp.close()

        with open(self.timefile) as sp :
            time_data = json.load(sp)
            sp.close()

        key = str(key)

        data[key] = value
        time_data[key] = (time.time(), sec)

        with open(self.filename, 'w') as fp :
            json.dump(data, fp, indent=4)
            fp.close()

        with open(self.timefile, 'w') as sp :
            json.dump(time_data, sp, indent=4)
            sp.close()

        self.lock.release()
        return key

    def delete(self, key) :
        self.lock.acquire()
        with open(self.filename) as fp :
            data = json.load(fp)
            fp.close()

        with open(self.timefile) as sp :
            time_data = json.load(sp)
            sp.close()

        key = str(key)

        if data.get(key) == None :
            self.lock.release()
            raise Exception(f'{key} not found in the data-store!!')

        if (time.time() - time_data[key][0]) > time_data[key][1] :
            del data[key]
            
            with open(self.filename, 'w') as fp :
                json.dump(data, fp, indent=4)
                fp.close()

            self.lock.release()
            raise Exception(f'{key} not found in the data-store!!')

        del data[key]

        with open(self.filename, 'w') as fp :
            json.dump(data, fp, indent=4)
            fp.close()

        with open(self.timefile, 'w') as sp :
            json.dump(time_data, sp, indent=4)
            sp.close()

        self.lock.release()
        return key

    def read(self, key) :
        self.lock.acquire()
        with open(self.filename) as fp :
            data = json.load(fp)
            fp.close()

        with open(self.timefile) as sp :
            time_data = json.load(sp)
            sp.close()

        key = str(key)

        if data.get(key) == None :
            self.lock.release()
            raise Exception(f'no value found for {key} !!')
        
        if (time.time() - time_data[key][0]) > time_data[key][1] :
            del data[key]

            with open(self.filename, 'w') as fp :
                json.dump(data, fp, indent=4)
                fp.close()

            self.lock.release()
            raise Exception(f'no value found for {key} !!')
        
        self.lock.release()
        return data[key]
