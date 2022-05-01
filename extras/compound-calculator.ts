const calculate = (initial: number, rate: number, days: number) => {
  let a = initial;
  for (let i = 0; i < days; i++) {
    a += a * (rate / 100);
    console.log(a);
  }
};

calculate(140, 5, 180)
// console.log(912434* 78);