#自定义的dict
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('\'Dcit\' object has no attribute \'%s\'' % key)
    
    def __setattr__(self, key, value):
        self[key] = value
