
class Container:
    def __init__(self, key, value):
        self.__key, self.__value = key, value
        self.__location = None
        self.__metadata = {}
        
        # TODO

    def get_kv(self):
        return self.__key, self.__value

    def get_location(self):
        return self.__location

    def set_metadata(self, meta):
        assert type(meta) is dict, 'Metadata should be a dictionary'

        for key in meta:
            self.__metadata['key'] = meta['key']

    def get_metadata(self, key):
        return self.__metadata.get(key) # Return None if not exists

    
