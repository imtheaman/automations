import puppeteer, { Keyboard } from "puppeteer-core";
import dotenv from "dotenv";
const envProcess = dotenv.config();
const searchQuery = "react";

(async () => {
  const browser = await puppeteer.launch({
    executablePath:
      "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    headless: false,
  });
  const page = await browser.newPage();
  await page.goto("http://github.com/login");
  const username = "#login_field";
  await page.waitForSelector(username);
  await page.type(username, envProcess?.parsed?.github_username!, {
    delay: 100,
  });
  const password = "#password";
  await page.waitForSelector(password);
  await page.type(password, envProcess?.parsed?.github_password!, {
    delay: 100,
  });
  await page.keyboard.press("Enter");
  //   await page.waitForNavigation();
  const searchField = "input[data-hotkey='s,/']";
  const followBtns = "input[value='Follow']";
  await page.waitForSelector(searchField);
  await page.type(searchField, searchQuery);
  await page.keyboard.press("Enter");
  await page.waitForTimeout(4000);
  await page.$$eval(".menu-item", async (items: any) => await items[9].click());
  const page100 = 'a[aria-label="Page 100"]';
  await page.waitForTimeout(4000);
  await page.waitForSelector(page100);
  await page.$eval(page100, (a: any) => a.click());
  while (true) {
    await page.waitForTimeout(4000);
    await page.$$eval(followBtns, (btns) => {
      btns.forEach(async (btn: any) => {
        await btn.click();
        await page.waitForTimeout(200)
      });
    });
    await page.waitForTimeout(4000)
    const prevPage = ".previous_page";
    const nextPage = ".next_page";
    await page.$eval(prevPage, async (btn: any) => await btn.click());
  }
})();
