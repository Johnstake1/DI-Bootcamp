# Daily challenge

class Pagination:
    def __init__(self, items = None, pagesize = 10):
        if items is None:
            items = []
        self.items = items
        self.pageSize = pagesize
        self.currentPage = 1
        self.totalPages = (len(self.items) + self.pageSize - 1) // self.pageSize


    # def getVisibleItems(self):
        # return self.items[self.items/self.pageSize] I dont know what is wrong here. maybe a float?
    
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1

    def nextPage(self):
        self.currentPage += 1

    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = self.lastPages
    
    # def goToPage(pageNum):


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)     

# p.getVisibleItems()
p.nextPage()
     
