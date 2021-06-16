from datetime import datetime
from hashlib import sha256
from bson import json_util
import json

class Bloque:
    def __init__(self, index, cor, mot, hashArc, hashAnt, timestamp, zero_count):
        self.nonce = 0
        self.index = index
        self.correo = cor
        self.motivo = mot
        self.hashArc = hashArc
        self.hashAnt = hashAnt
        self.timestamp = timestamp
        self.hashBloque = self.crearHash(zero_count)

    def crearHash(self, zero_count):
        if zero_count == 0:
            zero_count = 2 if (datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M:%S').day % 2 == 0 ) else 1
        while True:
            newHash = self.hash()
            if newHash[0:zero_count] == '0' * zero_count:
                break
            else:
                self.nonce += 1
        return newHash

    def hash(self):
        hash = json.dumps(self.__dict__, sort_keys=True, default=json_util.default)
        return sha256(hash.encode()).hexdigest()