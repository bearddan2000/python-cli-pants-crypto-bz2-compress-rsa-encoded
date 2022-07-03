import bz2
import sys
class PasswordCompress:

    def compress(self, password):
        # password = bytes(password, encoding='utf-8')
        print("[COMPRESS] decompress size: ", sys.getsizeof(password))
        return bz2.compress(password)

    def decompress(self, password):
        #password = bytes(password, encoding='utf-8')
        print("[COMPRESS] compress size: ", sys.getsizeof(password))
        return bz2.decompress(password)
