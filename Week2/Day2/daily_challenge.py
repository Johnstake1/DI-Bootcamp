# Daily challenge

class Pagination:
    def __init__(self, items = None, pagesize = 10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = pagesize

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
 
