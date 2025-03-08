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
const calculatedHourlyLivingWage = USDollar.format(livingWages[adults][children]);
const calculatedAnnualLivingWage = USDollar.format(livingWages[adults][children] * 2080);
```
### ${calculatedHourlyLivingWage} per hour or ${calculatedAnnualLivingWage} annually

<br>

## Here are the Median Salaries for each Baltimore City government agency...

```js
const filteredMedianSalaries = (await FileAttachment("./data/all-median-salaries.csv").csv()).map(salary => ({
    agency: salary["AgencyName"],
    medianSalary: salary["AnnualSalary"]
    }));
display(filteredMedianSalaries);
```
