N = int(input('请输入这本书有多少个字：'))
K = int(input('宝宝每分钟看多少个字：'))
M = int(input('看了多少分钟：'))
a = N - K * M
print('宝宝还剩'+str(a)+'个字没看完')