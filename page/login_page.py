import allure


class LoginPage:
    @allure.step(title="输入用户名")
    def input_user_name(self):
        print("输入了用户名")

    @allure.step(title="输入密码")
    def input_password(self):
        print("输入了密码")

    @allure.step(title="点击登录")
    def click_login(self):
        print("点击了登录按钮")
