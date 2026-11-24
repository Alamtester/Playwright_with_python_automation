from playwright.async_api import Page



class Dashboard_page:

 def __init__(self, page: Page):
    self.page = page


    self.admin_menu = page.get_by_role("link",name="Admin")
    self.pim_menu = page.get_by_role("link",name="PIM")
    self.leave_menu = page.get_by_role("link",name="Leave")
    self.time_menu = page.get_by_role("link",name="Time")
    self.recruitment_menu = page.get_by_role("link",name="Recruitment")
    self.my_info_menu = page.get_by_role("link",name="My Info")
    self.performance_menu = page.get_by_role("link",name="Performance")
    self.dashboard_menu = page.get_by_role("link",name="Dashboard")
    self.directory_menu = page.get_by_role("link",name="Directory")
    self.maintenance_menu = page.get_by_role("link",name="Maintenance")
    self.claim_menu = page.get_by_role("link",name="Claim")
    self.buzz_menu = page.get_by_role("link",name="Buzz")



 async def menu_click(self,menu_name):
   menu = self.page.get_by_role("link",name=menu_name,exact=True)
   await menu.click()
