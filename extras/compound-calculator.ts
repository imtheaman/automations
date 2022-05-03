import inquirer from "inquirer";
const calculate = (initial: number, rate: number, days: number): void => {
  let a = initial;
  for (let i = 0; i < days; i++) {
    a += a * (rate / 100);
    console.log(Math.round(a));
  }
};

const questions = [
  {
    type: "input",
    name: "Principle",
    message: "Enter your principle",
  },
  {
    type: "input",
    name: "Rate",
    message: "Enter your % rate/day",
  },
  {
    type: "input",
    name: "Days",
    message: "Enter your time in days",
  },
];
// const initial = userinput.question(
//   "Enter your principle",
//   (principle) => principle
// );
// const rate = userinput.question("Enter your % rate", (rate) => rate);
// const days = userinput.question("Enter your time in days", (days) => days);

inquirer
  .prompt(questions)
  .then((ans: { Principle: string; Rate: string; Days: string }) => {
    calculate(+ans.Principle, +ans.Rate, +ans.Days);
  });
