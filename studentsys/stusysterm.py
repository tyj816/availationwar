

import os
filename = 'student1.txt'
def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 1:
                insert()
            elif choice == 2:
                delete()
            elif choice == 3:
                modify()
            elif choice == 4:
                search()
            elif choice == 5:
                total()
            elif choice == 6:
                show()
            elif choice == 7:
                sort()
            else:
                answer = input('您确定要退出系统?y/n:')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
        else:
            print('您的输入有误，请重新输入：')
            continue
def menu():
    print('==========================学生信息管理系统================================')
    print('-----------------------------功能菜单------------------------------------')
    print('\t\t\t\t  1.录入学生信息')
    print('\t\t\t\t  2.删除学生信息')
    print('\t\t\t\t  3.修改学生信息')
    print('\t\t\t\t  4.查询学生信息')
    print('\t\t\t\t  5.统计学生人数')
    print('\t\t\t\t  6.显示所有学生信息')
    print('\t\t\t\t  7.排序')
    print('\t\t\t\t  0.退出系统')
    print('-----------------------------------------------------------------------')
def insert():
    student_list = []
    while True:
        name = input('请输入学生的名字：')
        if not name:
            break
        id = input('请输入学生的学号(如1001)：')
        if not id:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入有误，不是整数，请重新输入')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？y/n：')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生成绩录入完毕！')
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()
def delete():
    while True:
        student_id = input('请输入要删除学生的学号：')
        #判断学号是否正确输入
        if student_id != '':
            # 判断文件是否存在
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8')as file:
                    student_old = file.readlines()#将文件中的内容读进列表中
            else:
                student_old = []
            flag = False#标记删除变量
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))#强制类型转换成字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')#写进文件
                        else:
                            flag = True
                    if flag:
                        print(f'已删除ID为{student_id}的学生信息!')
                    else:
                        print(f'未找到ID{student_id}的学生信息！')
            else:
                print('无学生信息')
                break
            show()#将学生信息显示出来
            answer = input('是否继续删除？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生的ID:')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到这名学生了，可以修改他的信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入java成绩：')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息？y/n：')
        if answer == 'y' or answer == 'Y':
            modify()
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('输入有误，请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否要继续查询学生信息？y/n：')
            if answer =='y' or answer =='Y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息！')
            return
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data ='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list=rfile.readlines()
            if student_list:
                print(f'一共有{len(student_list)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存信息！')
def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        student_list = []
        for item in students:
            student_list.append(eval(item))
    else:
        return
    asc_or_desc = input('排序方式：升序按0，降序按1：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方(1.按英语成绩排序，2.按python成绩排序，3.按Java成绩排序，0.按总成绩排序)：')
    if mode == '1':
        student_list.sort(key=lambda x: int(x['english']),reverse=asc_or_desc_bool)
    elif mode =='2':
        student_list.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode =='3':
        student_list.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode =='0':
        student_list.sort(key=lambda x: int(x['english'])+int(x['java'])+int(x['python'])+int(x['english']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_list)
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students=rfile.readlines()
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
    else:
        print('暂未保存数据信息！')

if __name__ == '__main__':
    main()
