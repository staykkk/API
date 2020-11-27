class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
        return Chain( '%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
    def __call__(self, user):
        return Chain('%s/%s' %(self._path,user))
    __repr__=__str__
print('GET',Chain().users('michael').repos)
print('GET',Chain().status.user.timeline.list)
