import os

filename='student2.txt'
def main():
    while True:
        menu()
        chioce = int(input("请选择："))
        if chioce in [0, 1, 2, 3, 4, 5, 6 ,7]:
            if chioce == 1 :
                insert()
            if chioce == 2 :
                delete()
            if chioce == 3 :
                modify()
            if chioce == 4 :
                search()
            if chioce == 5 :
                total()
            if chioce == 6 :
                sort()
            if chioce == 7:
                show()
            if chioce == 0:
                anwser=input("您确定退出系统吗？y/n:")
                if anwser == 'y' or anwser == 'Y':
                    print("谢谢您的使用！！！")
                    break
                else:
                    continue
        else:
            print("您的输入有误，请重新输入！！！")
            continue

def menu():
    print("===========================学生成绩管理系统====================================")
    print("---------------------------功能菜单-------------------------------------------")
    print("\t\t\t1.录入学生信息")
    print("\t\t\t2.删除学生信息")
    print("\t\t\t3.修改学生信息")
    print("\t\t\t4.查询学生信息")
    print("\t\t\t5.统计学生人数")
    print("\t\t\t6.排列学生成绩")
    print("\t\t\t7.显示所有学生信息")
    print("\t\t\t0.退出系统")
    print("-----------------------------------------------------------------------------")

def insert():
    student_list=[]
    while True:
        id = input("请输入学生的学号(如1001)：")
        if not id:
            break
        name = input("请输入学生的名字：")
        if not name:
            break
        try:
            english=int(input("请输入英语成绩："))
            python=int(input("请输入python成绩："))
            java=int(input("请输入java成绩："))
        except:
            print("您的输入有误，不是整数，请重新输入！")
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input("是否继续添加？y/n:")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print("录入完毕！")

def save(list):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoing='utf-8')
    for item in list:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def delete():
    while True:
        student_id=input("请输入要删除的学生的id：")
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'已删除ID为{student_id}的学生!')
                    else:
                        print(f'未找到ID为{student_id}的学生！')
            else:
                print("无学生信息！")
                break
        answer=input('是否继续删除学生信息？y/n:')
        if answer =='y' or answer == 'Y':
            continue
        else:
            break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student_list=rfile.readlines()
    else:
        return
    student_id = input("请输入您想修改的学生的id:")
    with open(filename,'w',encoding='utf-8')as wfile:
        d={}
        for item in student_list:
            d=dict(eval(item))
            if d['id'] == student_id:
                while True:
                    print('找到这名学生了，可以修改他的信息了！')
                    try:
                        d['name']=input('请输入姓名:')
                        d['english']=input('请输入英语成绩:')
                        d['python']=input('请输入python成绩:')
                        d['java']=input('请输入java成绩:')
                    except:
                        print('您的输入有误重新输入！！！')
                        continue
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功！")
            else:
                wfile.write(str(d) + '\n')
        answer = input("是否继续修改其他学生的信息？y/n:")
        if answer == 'y' or answer == 'Y':
            modify()
def search():
    student_query=[]
    while True:
        name=''
        id=''
        if os.path.exists(filename):
            mode=input("按姓名查询输1，按ID查询输2：")
            if mode == '1':
                name=input("请输入姓名：")
            elif mode == '2':
                id = input("请输入ID：")
            else:
                print("输入有误，请重新输入！")
                search()
            with open(filename,'r',encoding='utf-8')as rfile:
                student_old=rfile.readlines()
                for item in student_old:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    if name!='':
                        if d['name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input("是否继续查询其他学生的信息？y/n：")
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print("暂未保存学生信息！")
            return
def show_student(lst):
    if len(lst)==0:
        print("暂未保存学生信息！")
        return
    format_title='{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(format_title.format('id','姓名','english','python','java','总成绩'))
    format_data='{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
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
        with open(filename,'r',encoding='utf-8')as rfile:
            student_list=rfile.readlines()
            if len(student_list)!=0:
                print(f'一共有{len(student_list)}名学生')
            else:
                print("还未保存学生信息！")
    else:
        print('暂无学生信息！')
def sort():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
        student_list = []
        for item in students:
            student_list.append(eval(item))
    else:
        return
    asc_or_desc=input("请选择1.升序，0.降序:")
    if asc_or_desc=='0':
        asc_or_desc_bool = False
    elif asc_or_desc=='1':
        asc_or_desc_bool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode=input("请选择您的排序方式：1.按英语成绩，2.按python成绩，3.按java成绩，0.按总成绩：")
    if mode=='1':
        student_list.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_list.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_list.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_bool)
    elif mode =='0':
        student_list.sort(key=lambda x: int(x['english'])+int(x['java'])+int(x['python'])+int(x['english']), reverse=asc_or_desc_bool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_list)

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
    else:
        print("暂未保存学生信息！")
        return


if __name__=='__main__':
    main()