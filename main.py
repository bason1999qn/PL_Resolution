from LoadFile import *
from KB import *
import copy
def main():
    kb = KB()
    choice ='0'
    while choice =='0':
        print("Danh sách file:")
        print("1. input1.txt")
        print("2. input2.txt")
        print("3. input3.txt")
        print("4. input4.txt")
        print("5. input5.txt")
        print("6. Chọn file khác")
        choice = input("chọn file chạy (q: thoát khỏi menu): ")

        if choice == "1":
            print("Nội dung file input1.txt:")
            printFile("input1.txt")
            print("Kết quả thuật toán: ")
            Input("input1.txt", kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào output1.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("output1.txt", 'w') as f:
                    f = Output("output1.txt", kb)
                printFile("output1.txt")
                main()
            if (choice == "0"):
                main()
        elif choice == "2":
            print("Nội dung file input2.txt:")
            printFile("input2.txt")
            print("Kết quả thuật toán: ")
            Input("input2.txt", kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào output2.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("output2.txt", 'w') as f:
                    f = Output("output2.txt", kb)
                printFile("output2.txt")
                main()
            if (choice == "0"):
                main()

        elif choice == "3":
            print("Nội dung file input3.txt:")
            printFile("input3.txt")
            print("Kết quả thuật toán: ")
            Input("input3.txt", kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào output3.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("output3.txt", 'w') as f:
                    f = Output("output3.txt", kb)
                printFile("output3.txt")
                main()
            if (choice == "0"):
                main()
        elif choice == "4":
            print("Nội dung file input4.txt:")
            printFile("input4.txt")
            print("Kết quả thuật toán: ")
            Input("input4.txt", kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào output4.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("output4.txt", 'w') as f:
                    f = Output("output4.txt", kb)
                printFile("output4.txt")
                main()
            if (choice == "0"):
                main()
        elif choice == "5":
            print("Nội dung file input5.txt:")
            printFile("input5.txt")
            print("Kết quả thuật toán: ")
            Input("input5.txt", kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào output5.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("output5.txt", 'w') as f:
                    f = Output("output5.txt", kb)
                printFile("output5.txt")
                main()
            if (choice == "0"):
                main()
        elif choice == "6":
            print("Nhập tên file input (vd input6.txt): ")
            s = input()
            print("Nội dung file ", s, ":")
            printFile(s)
            print("Kết quả thuật toán: ")
            Input(s, kb)
            print(PL_resolution(kb))
            print("1. Xuất kết quả vào outputX.txt")
            print("0. Trở lại menu.")
            choice = input("Chọn:")
            if (choice == "1"):
                with open("outputX.txt", 'w') as f:
                    f = Output("outputX.txt", kb)
                printFile("outputX.txt")
                main()
        else:
            print("I don't understand your choice.")



main()

