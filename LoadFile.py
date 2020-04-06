from algorithms import *
from KB import *

#Xử lý file input và nạp dữ liệu vào biến KB (đã được định nghĩa trong class KB)
def Input(fileName, KB):
    #menh de alpha
    a = []
    #so menh de
    so = 0
    #Danh sach menh de
    listTemp = []

    # t_line: dem so dong trong file
    t_line = 0
    listTemp = []
    with open(fileName, "r") as fd:
        for line in fd:
            line = line.strip()
            t_line += 1  # So dong cua file txt
            # Nếu đọc dòng đầu tiên của file chứa mệnh đề alpha
            if t_line == 1:
                for num in line.strip().split(' '):
                    s = num
                    if (s != 'OR'):
                        a.append(s)

            # Số mệnh đề trong file
            if t_line == 2:
                so = int(line)
            # Thêm các mệnh đề vào list
            if t_line > 2:
                list = []
                # Đọc dòng tới dấu " " và lưu giá trị vào biến s
                for num in line.strip().split(' '):
                    s = num
                    if (s != 'OR'):
                        list.append(s)
                listTemp.append(list)
        # Cập nhật vào KB
    KB.setKB(a,so,listTemp)
    fd.close()

#Xuất nội dung file ra ngoài màn hình
def printFile(inputFile):
    f = open(inputFile)
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()

#Thêm vào cuối file "fileName" với nội dung đầu vào string.
def addOutput(fileName, string):
    with open(fileName, 'a+', encoding='utf-8') as f:
        f.write(string)
    f.close()

#Xuất file output
def Output(fileName, KB):
    listNewClause = []
    listClause = KB.getList()
    listClause += negativeAlpha(KB.getAlpha())
    listNewClause = createNewList(listClause)
    while (len(listNewClause) > 0):
        s = convertToString(listNewClause)
        addOutput(fileName, s)
        listClause = listClause + listNewClause
        listNewClause = createNewList(listClause)

        if (is_stop(listClause) == 1):
            addOutput(fileName, convertToString(listNewClause))
            addOutput(fileName, "{}\n")
            addOutput(fileName, "YES\n")
            break
    if (is_stop(listClause) == 0):
        addOutput(fileName, "0\n")
        addOutput(fileName, "NO\n")





