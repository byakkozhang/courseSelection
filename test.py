d = {'tony':123}        #数据库字典，所有用户的用户名密码存储在此

name = input("请输入您的用户名：")
if name in d:
    password = input("请输入您的密码")
    if d[name] == password:
        print('进入系统')
    else:
        print('您输入的密码错误，请重新输入')
else:
    print('您输入的用户名不正确，请重新输入')

