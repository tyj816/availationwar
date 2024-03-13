#输出四位整数的各位
a = int(input('请输入一个四位数:'))
b=a % 10
c=int((a / 10) % 10)
d=int((a / 100) % 10)
e=int(a / 1000)
print(str(a)+'='+str(b)+'+'+str(c)+'*10+'+str(d)+'*100+'+str(e)+'*1000')
