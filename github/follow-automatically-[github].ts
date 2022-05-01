import puppeteer, { Keyboard } from "puppeteer";
import dotenv from "dotenv";
const envProcess = dotenv.config();
const searchQuery = "react";

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
  });
  const page = await browser.newPage();
  await page.goto("http://github.com/login");
  const username = "#login_field";
  await page.waitForSelector(username);
  await page.type(username, envProcess?.parsed?.username!, {
    delay: 50,
  });
  const password = "#password";
  await page.waitForSelector(password);
  await page.type(password, envProcess?.parsed?.password!, {
    delay: 50,
  });
  await page.keyboard.press("Enter");
  const searchField = "input[data-hotkey='s,/']";
  const followBtns = "input[value='Follow']";
  await page.waitForSelector(searchField);
  await page.type(searchField, searchQuery);
  await page.keyboard.press("Enter");
  await page.waitForNavigation();
  await page.$$eval(".menu-item", async (items: any) => await items[9].click());
  const page100 = 'a[aria-label="Page 100"]';
  await page.waitForNetworkIdle();
  await page.waitForSelector(page100);
  await page.$eval(page100, (a: any) => a.click());
  while (true) {
    await page.waitForNetworkIdle();
    await page.$$eval(followBtns, (btns) => {
      btns.forEach(async (btn: any) => {
        await btn.click();
        await page.waitForNetworkIdle();
      });
    });
    await page.waitForNetworkIdle();
    const prevPage = ".previous_page";
    const nextPage = ".next_page";
    await page.$eval(prevPage, async (btn: any) => await btn.click());
  }
})();
