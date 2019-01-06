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

def main():
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
            

if __name__ == "__main__":
    main()