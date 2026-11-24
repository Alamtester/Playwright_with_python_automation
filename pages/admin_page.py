from playwright.async_api import Page,expect


class AdminPage:

     def __init__(self,page: Page):

        self.page =page

        self.admin_menu = page.get_by_role("link",name="Admin")
        self.admin_header = page.locator(".oxd-topbar-header-breadcrumb")
        self.add = page.get_by_role("button",name="Add")
        self.user_role_field = page.locator(".oxd-select-wrapper").nth(0)
        self.employee_name_field = page.get_by_placeholder("Type for hints...")
        self.auto_emp_name = page.get_by_role("listbox").nth(0)
        self.status_field = page.locator(".oxd-select-wrapper").nth(1)
        self.username_field = page.locator(".oxd-input--active").nth(1)
        self.password_field = page.locator("input[type='password']").nth(0)
        self.confirm_password_field = page.locator("input[type='password']").nth(1)
        self.save_btn = page.locator("button[type='submit']")
        self.required_error_messsage= page.locator(".oxd-input-field-error-message")
        self.search_username_field = page.locator("input.oxd-input--active")
        self.search_btn = page.locator("button[type='submit']")

        #oxd-autocomplete-text-input oxd-autocomplete-text-input--active oxd-autocomplete-text-input--error    #.oxd-autocomplete-option
  

     async def admin_click(self):
         await self.admin_menu.click()

     async def create_admin(self):
         await self.add.click()

     async def click_user_role_field(self,role):
         await self.user_role_field.click()
         await self.page.get_by_role("option",name=role,exact=True).click()

     async def  employee_name_field_enter(self,employee_name):
         await self.employee_name_field.fill(employee_name)

     async def employee_name_field_autosugesstion(self): 

         await expect(self.auto_emp_name.first).to_be_visible()

         suggestions = await self.auto_emp_name.all_inner_texts()

         print("List of suggestions:", suggestions) 

         await self.auto_emp_name.filter(has_text="Charles Carter") .click()

     async def click_status(self,status):
         await self.status_field.click() 
         await self.page.get_by_role("option",name=status,exact=True).click() 

     async def enter_username(self):
         await self.username_field.fill("Charles Carter") 

     async def enter_password(self):
         await self.password_field.fill("charles123")

     async def enter_confirm_password(self):
         await self.confirm_password_field.fill("charles123") 

     async def click_save_btn(self):
         await self.save_btn.click()              

     





       

