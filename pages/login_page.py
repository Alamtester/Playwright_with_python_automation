
from playwright.async_api import Page


class LoginPage:

     def __init__(self,page:Page):
        self.page = page


        self.username = page.get_by_placeholder("username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button" , name="Login")
        self.error_message = page.locator("p.oxd-alert-content-text")
       # <span data-v-7b563373="" data-v-957b4417="" class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message">Required</span>
        self.required_field_error_message = page.locator("span.oxd-input-field-error-message")



     async def navigate(self):
       await  self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  


     async def login(self, username, password):
       await  self.username.fill(username)
       await self.password.fill(password)
       await self.login_btn.click() 

    # def error_message(self):
    #     self.error_message

    # def required_error_message(self):
    #     self.required_error_message

    

    