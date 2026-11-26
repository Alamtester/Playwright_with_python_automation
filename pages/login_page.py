
from playwright.async_api import Page
from utils.common_actions import CommonActions


class LoginPage:

     def __init__(self,page:Page):
        self.page = page
        self.actions = CommonActions(page)


        self.username = page.get_by_placeholder("username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button" , name="Login")
        self.error_message = page.locator("p.oxd-alert-content-text")
       # <span data-v-7b563373="" data-v-957b4417="" class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message">Required</span>
        self.required_field_error_message = page.locator("span.oxd-input-field-error-message")
        self.dashboard_text = page.locator(".oxd-topbar-header-breadcrumb-module")



     async def navigate(self):
       await  self.actions.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 


     async def enter_username(self, username):
       await self.actions.enter_text(self.username,username)    


     
     async def enter_password(self, password):
       await self.actions.enter_text(self.password,password)

     async def click_login_btn(self):
        await self.actions.click(self.login_btn)

    # def error_message(self):
    #     self.error_message

    # def required_error_message(self):
    #     self.required_error_message

    

    