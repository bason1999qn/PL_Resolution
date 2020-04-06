class KB:
    def __init__(self):
        #câu mệnh alpha
        self.alpha = 0
        #Số mệnh đề trong KB
        self.soMenhDe = 0
        #Lưu các mệnh đề mà input đã cho
        self.List = 0
    def getAlpha(self):
        return self.alpha
    def getSoMenhDe(self):
        return self.soMenhDe
    def getList(self):
        return self.List
    def setKB(self, alpha, soMenhDe, List):
        self.alpha = alpha
        self.soMenhDe = soMenhDe
        self.List = List








