---
toc: false
---

```js
const livingWages = FileAttachment("./data/living-wage-2024.json").json();
```

# Can you afford to work for the City of Baltimore?

---

## What's your family look like?

Your choices will determine your living wage for Baltimore City.

```js
const adultOptions = ["1 adult", "2 adults, 1 working", "2 adults, both working"];
const childOptions = ["0 children", "1 child", "2 children" , "3 children"];

const adults = view(Inputs.select(adultOptions, {value: "1 adult", label: "# of Adults"}));
const children = view(Inputs.select(childOptions, {value: null, label: "# of Children"}));
```

<br>

## Let's calculate your living wage...

With a family of **${adults}** and **${children}**, your living wage in Baltimore city is:

```js
const USDollar =  new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});
const calculatedHourlyLivingWage = livingWages[adults][children];
const calculatedAnnualLivingWage = livingWages[adults][children] * 2080;

const formattedHourlyLivingWage = USDollar.format(calculatedHourlyLivingWage);
const formattedAnnualLivingWage = USDollar.format(calculatedAnnualLivingWage);
```
<div class="grid grid-cols-2">
    <div class="card">
        <div class="big">${formattedHourlyLivingWage} per hour or ${formattedAnnualLivingWage} annually</div>
    </div>
</div>

<br>

## Here are the Median Salaries for each Baltimore City government agency...

```js
const filteredMedianSalaries = (await FileAttachment("./data/all-median-salaries.csv").csv({typed: true})).map(salary => ({
    agency: salary["AgencyName"],
    medianSalary: salary["AnnualSalary"]
    }));
const allMedianSalariesPlot = Plot.plot({
    marginLeft: 10,
    width: width,
    x: {
        axis: "top",
        transform: (s) => s / 1000,
        label: "Median Annual Salary (thousands)"
    },
    marks: [
        Plot.barX(filteredMedianSalaries, {
            x: "medianSalary",
            y: "agency",
            fill: (s) => (s.medianSalary >= calculatedAnnualLivingWage ? "green" : "red"), 
            sort: {y: "-x"}
        }),
        Plot.ruleX([calculatedAnnualLivingWage], {stroke: "yellow"}),
        Plot.axisY({
            label: null,
            fill: "black", 
            textAnchor: "start",
            dx: 14,
            tickSize: 0
        })
    ]
});
display(allMedianSalariesPlot)
```
