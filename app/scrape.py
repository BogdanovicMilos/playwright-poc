import asyncio
from playwright.async_api import async_playwright
 
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True
        )
        page = await browser.new_page()
        await page.goto('https://www.nasa.gov/')
        items = await page.content()
        await page.wait_for_timeout(5000)
        print(items)
        return items
        
if __name__ == '__main__':
    asyncio.run(main())
    
