# linkedin-auto-endorse

Auto endorse using ts/js

usage guides
`git clone https://github.com/urtheaman/linkedin-auto-endorse.git`

`cd linkedin-auto-endorse`

`npm install`

change in index.js with your target username, your account email & your password respectively.

<img src="/before.png" alt="code block to change" />

`npm run build`

> developer tools usage

```
(() => {
let height = document.body.scrollHeight;
while(true) {
window.scrollTo(0, document.body.scrollHeight)
setTimeout(() => {}, 4000)
if (height === document.body.scrollHeight) break;
height = document.body.scrollHeight;
}

$$('.pv2 button').forEach(async (btn) => {if (btn.textContent.trim() === 'Endorse') {
    await btn.click()
    console.log('done')
}})
})()
```
