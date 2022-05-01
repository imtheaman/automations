import puppeteer from "puppeteer";
import dotenv from "dotenv";
import { type Page } from "puppeteer";
const process = dotenv.config();

// const username = process?.parsed?.target_username! || '';
const email = process?.parsed?.email!;
const password = process?.parsed?.password!;

async function endorse(profileLink: string, page: Page) {
  await page.goto(`${profileLink}/details/skills`);
  let lastHeight = await page.evaluate("document.body.scrollHeight");
  while (true) {
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)");
    await page.waitForTimeout(2000); // sleep a bit
    let newHeight = await page.evaluate("document.body.scrollHeight");
    if (newHeight === lastHeight) {
      break;
    }
    lastHeight = newHeight;
  }
  await page.$$eval(".pv2 button", (btns) => {
    btns.forEach(async (btn: any) => {
      if (btn.textContent.trim() === "Endorse") await btn.click();
    });
  });
}

const getConnections = async (email: string, password: string) => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(`https://linkedin.com/login`);
  await page.waitForSelector("#username");
  await page.focus("#username");
  await page.keyboard.type(email, { delay: 50 });
  await page.waitForSelector("#password");
  await page.focus("#password");
  await page.keyboard.type(password, { delay: 50 });
  await page.keyboard.press("Enter");
  await page.waitForNavigation();

  // now you're logged in
  const gotoProfile = ".feed-identity-module__actor-meta a";
  await page.$eval(gotoProfile, (a: any) => a.click());
  const connections = ".pv-top-card--list li a";
  await page.waitForSelector(connections);
  await page.$$eval(connections, (btns: any) => btns[1].click());
  const disabledNextBtn = 'button[aria-label="Next"][disabled]';
  const nextBtn = ".artdeco-pagination__button--next";
  while (true) {
    await page.waitForTimeout(10000);
    if (await page.$(disabledNextBtn)) break;
    const profileLink = ".entity-result__item a";
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)");

    await page.$$eval(profileLink, (links) =>
      links.forEach((link: any) => console.log(link.href))
    );

    await page.$eval(nextBtn, (a: any) => a.click());
  }
};
getConnections(email, password);
