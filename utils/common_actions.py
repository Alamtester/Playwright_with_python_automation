from playwright.async_api import Page



class CommonActions:

    def __init__(self,page: Page):
        self.page = page

    async def click(self,locator):
        await locator.click()

    async def enter_text(self,locator,text):
        await locator.fill(text)

    async def clear_field(self,locator):
        await locator.clear()

    async def get_text(self,locator):
        await locator.inner_text()

    async def is_visible(self,locator):
        return await locator.is_visible()

    async def open_url(self,url):
        await self.page.goto(url) 

    async def wait_for_element(self,locator):
        return await locator.wait_for(state='Visible')                          
