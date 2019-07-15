'''

纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

读excel xlrd

'''


import json
from collections import OrderedDict
import xlrd
import xlwt



def read_exel():
    workbook = xlrd.open_workbook('student.xls')
   # print(workbook.sheet_names()[0])
    sel_name = workbook.sheet_names()[0]
    sel2 = workbook.sheet_by_index(0)
    sel2 = workbook.sheet_by_name('student')
    print(sel2.name, sel2.nrows, sel2.ncols)



if __name__ == "__main__":
    read_exel()

# with open('student.txt','r',encoding='utf-8') as f:
#     file = f.read()
#     print(file)

# with open('student.txt',  'r', encoding='GBK') as f:
#     students_dict = json.load()
#
#     # file = f.read()
#     # print(students_dict)
#     for i in students_dict:
#         print(i)
#     #print(students_dict)

    # print(file)

# with open('student.txt',  'r', encoding='GBK') as f:
#     students_dict2 = OrderedDict(json.load(f))
#     for i in students_dict2:
#         print(i)
# wb = xlwt.Workbook()  #创建一个工作簿
# ws = wb.add_sheet('student') #创建一个sheet
#
# row = 0
# for k,v in students_dict.items():
#     ws.write(row,0,k)
#     col = 1
#     for item in v:
#         ws.write(row,col,item)
#         col += 1
#     row +=1
# wb.save('student.xls')  #保存
