const calculate = (initial: number, rate: number, days: number) => {
  let a = initial;
  for (let i = 0; i < days; i++) {
    a += a * (rate / 100);
    console.log(a);
  }
};

calculate(130, 5, 360)