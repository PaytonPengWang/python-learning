"""
    作者：王鹏
    功能：判断一年中的第几天
    日期：5/1/2019
    
    简易版规则：
    1:密码长度至少8位
    2:密码含有数字
    3:密码含有字母

    长度判断：使用len()方法
    包含数字判断：使用isnumeric()方法
    包含字母判断：使用isalpha()方法

    v2.0: 新增 - 限制尝试次数
    v3.0: 新增 - 将密码保存在文件中
"""
def number_existed(password):
    for c in password:
        if c.isnumeric():
            return True
    
    return False

def letter_existed(password):
    for c in password:
        if c.isalpha():
            return True
    
    return False

def save_file(password):
    # 1: 打开文件
    # open(filename, mode)
    # filename : 文件名包含路径
    # mode 
    #   r readonly
    #   w writeonly , will create the file if it not is existed
    #   a append
    #   r+ read and write
    passwordfile = open("./password.txt",'a')
    

    # 2: 操作文件
    # write(): 将文本数据写入文件中
    # writelines(): 将字符串列表写入文件中
    passwordfile.write("{}\n".format(password))
    # passwordfile.writelines(password)


    # 3: 关闭文件
    # close()
    passwordfile.close()

def main():
    try_times= 5

    while try_times > 0:

        password = input("please input your password: ")
        strength_level = 0

        # the length of password need greather than or equal to eigth
        if len(password) >= 8:
            strength_level+=1
        else:
            print("the length of password need greather than or equal to eight")
        
        if number_existed(password):
            strength_level+=1
        else:
            print("the password need contain number")
        
        if letter_existed(password):
            strength_level+=1
        else:
            print("thie password need contain letter")
        
        if strength_level == 3:
            save_file(password)
            break
        else:
            try_times-=1
            

if __name__ == "__main__":
    main()