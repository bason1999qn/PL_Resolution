import copy
from KB import *

#Phủ định mệnh đề đơn biến. vd phủ định của -A là A
def negative(clause):
    if len(clause) > 1 and clause[0] == '-':
        return clause[1]
    return ('-' + clause)

#Phủ định mệnh đề alpha
def negativeAlpha(clause):
    newClause = []
    for i in range(len(clause)):
        l = []
        l.append(negative(clause[i]))
        newClause.append(l)
    return newClause


#xác định 2 mệnh đề đối nhau. Trả về bool. vd A đối -A trả về 1.
def is_neg(s1,s2):
    if s1 == '-' + s2 or s2 == '-' + s1:
        return 1
    return 0

#Xác định mệnh đề vô ích. vd A v B v -B là vô ích hay A v A v C là vô ích.
def is_meaningless(clause):
    if len(clause) > 1:
        for i in range(len(clause)):
            for j in range(len(clause)):
                if (i != j):
                    if is_neg(clause[i], clause[j]) == 1:
                        return 1
                    if (clause[i] ==  clause[j]):
                        return 1
    return 0

#Xác định 2 mệnh đề có trùng nhau hay không. vd A v B v -C với A v -C v B trả về 1
def is_sample(clauseA, clauseB):
    tempA = copy.deepcopy(clauseA)
    tempA.sort()
    tempB = copy.deepcopy(clauseB)
    tempB.sort()
    if tempA == tempB:
        return 1
    return 0

#Xác định mệnh đề đã tồn tại trong danh sách mệnh đề hay không (trước khi thêm vào).
def is_exist(clause, listClause):
    for i in range(len(listClause)):
        if is_sample(listClause[i], clause) == 1:
            return 1
    return 0

#điều kiện dừng vòng lặp, khi tồn tại mệnh đề rỗng
def is_stop(listClause):
    for i in range(len(listClause)):
        if len(listClause[i]) == 1:
            for j in range(len(listClause)):
                if len(listClause[j]) == 1:
                    if is_neg(listClause[i][0],listClause[j][0]) == 1:
                        return 1
    return 0



#Hàm xác định tính logic của 2 mệnh đề và đưa ra mệnh đề mới được suy ra (nếu có).
def logic(clauseA, clauseB):
    newClause = []
    newClause = copy.deepcopy(clauseA)
    tempClause = copy.deepcopy(clauseB)
    for i in range(len(newClause)):
        for j in range(len(tempClause)):
            if is_neg(newClause[i], tempClause[j]) == 1:
                newClause.pop(i)
                tempClause.pop(j)
                newClause = newClause + tempClause
                return 1, newClause
    return 0, newClause

#Hàm tạo ra danh sách mệnh đề mới từ listClause (danh sách mệnh đề đều vào).
def createNewList(listClause):
    listNewClause = []
    t = 0
    for i in range(len(listClause) - 1):
        for j in range(i + 1, len(listClause)):
            t, clauseTemp = logic(listClause[i], listClause[j])
            if t == 1 and is_meaningless(clauseTemp) == 0 and is_exist(clauseTemp, listClause) == 0 and is_exist(clauseTemp, listNewClause) == 0 and len(clauseTemp) > 0:
                listNewClause.append(clauseTemp)
    return listNewClause

#Hàm xử lý KB với đầu vào là thuộc tính KB
def PL_resolution(KB):
    listNewClause = []
    listClause = KB.getList()
    listClause += negativeAlpha(KB.getAlpha())
    listNewClause = createNewList(listClause)
    while (len(listNewClause) > 0):
        print(listNewClause)

        listClause = listClause + listNewClause
        listNewClause = createNewList(listClause)
        if (is_stop(listClause) == 1):
            print(listNewClause)
            s = "YES"
            return s
    s = "NO"
    return s

#Chuyển mệnh đề từ dạng danh sách sang dạng string
def convertToString(listClause):
    s = str(len(listClause)) + "\n"
    for i in range(len(listClause)):
        if int(len(listClause[i])) > 1:
            for j in range(len(listClause[i])):
                if (j == len(listClause[i]) - 1):
                    s += listClause[i][j]
                else:
                    s += str(listClause[i][j]) + " OR "
            s += "\n"
        else:
            s += str(listClause[i][0]) + "\n"
    return s







