class ResearchClass:
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        #print(self.var1)
        #print(self.var2)

#### Duplicate value Fuction
    def FindDuplicate(self):
        list = self.var1
        dict = {}
        listDuplicate = []
        for val in list:
            dict[val] = val
        for val1 in dict.keys():
            cnt = list.count(val1)
            if (cnt > 1):
                listDuplicate.append(val1)
        return listDuplicate

