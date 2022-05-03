import puppeteer from "puppeteer";
import dotenv from "dotenv";
const process = dotenv.config();

const username = process?.parsed?.target_username!;
const email = process?.parsed?.email!;
const password = process?.parsed?.password!;

const x = async (username: string, email: string, password: string) => {
  const browser = await puppeteer.launch({
    headless: false,
    timeout: 3000,
  });
  const page = await browser.newPage();
  await page.goto(`https://linkedin.com/login`, {
    waitUntil: "networkidle2",
  });
  await page.waitForSelector("#username");
  await page.focus("#username");
  await page.keyboard.type(email, { delay: 75 });
  await page.waitForSelector("#password");
  await page.focus("#password");
  await page.keyboard.type(password, { delay: 75 });
  await page.keyboard.press("Enter");
  await page.waitForNetworkIdle();
  await page.goto(`https://linkedin.com/in/${username}/details/skills`);
  let lastHeight = await page.evaluate("document.body.scrollHeight");

  while (true) {
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)");
    await page.waitForNetworkIdle();
    let newHeight = await page.evaluate("document.body.scrollHeight");
    if (newHeight === lastHeight) {
      break;
    }
    lastHeight = newHeight;
  }
  await page.$$eval(".pv2 button", (btns: any) => {
    btns.forEach(async (btn: any) => {
      if (btn.textContent.trim() === "Endorse") {
        btn.click();
        await page.waitForNetworkIdle();
      }
    });
  });
  await browser.close();
};
x(username, email, password);
