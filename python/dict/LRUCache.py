class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mapp=collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.mapp:
            ret=self.mapp[key]
            self.mapp.pop(key)
            self.mapp[key]=ret
            return ret
        else: return -1

    def put(self, key: int, value: int) -> None:
        temp=''
        self.mapp.pop(key,None)
        self.mapp[key]=value
        if len(self.mapp)>self.capacity:
            self.mapp.popitem(last=False)
