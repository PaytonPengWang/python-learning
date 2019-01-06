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
    v4.0: 新增 - 面向对象
"""

# 密码工具类
class PasswordTool:
    
    # 构造函数
    def __init__(self,password):
        # 属性
        self.password = password
        self.strength_level = 0

    
    def number_existed(self):
        for c in self.password:
            if c.isnumeric():
                self.strength_level+=1
                return
        print("the password need contain number")

    def letter_existed(self):
        for c in self.password:
            if c.isalpha():
                self.strength_level+=1
                return
        print("thie password need contain letter")

    def check_length(self):
        if len(self.password) >= 8:
            self.strength_level+=1
            return
        print("the length of password need greather than or equal to eight")

    def check_strength(self):
        self.number_existed()
        self.letter_existed()
        self.check_length()

            

def main():
    try_times= 5

    while try_times > 0:

        password = input("please input your password: ")
        # 实例化对象
        passwordTool = PasswordTool(password)
        passwordTool.check_strength()

        
        if passwordTool.strength_level == 3:
            break
        else:
            try_times-=1
            

if __name__ == "__main__":
    main()