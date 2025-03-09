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
        <div class="big">
            ${formattedHourlyLivingWage} per hour 
            <br>or<br> 
            ${formattedAnnualLivingWage} annually
        </div>
    </div>
</div>

<br>

## Ok, who can afford to hire you?

```js
const filteredMedianSalaries = (await FileAttachment("./data/all-median-salaries.csv").csv({typed: true})).map(salary => ({
    agency: salary["MappedAgencyName"],
    medianSalary: salary["AnnualSalary"]
    }));
var affordableAgencies = filteredMedianSalaries
    .filter(salary => salary.medianSalary >= calculatedAnnualLivingWage)
    .length;
```
<div class="grid grid-cols-2">
    <div class="card">
        <div class="medium">
            <div style="color: green; font-weight: bold;">
                ${affordableAgencies} city agencies can afford to pay you a living wage
            </div>
            <br>
            <div style="color: red; font-weight: bold;">
                ${Object.keys(filteredMedianSalaries).length - affordableAgencies} city agencies cannot
            </div>
            </div>
    </div>
</div>

```js
const allMedianSalariesPlot = Plot.plot({
    style: { fontSize: "13px" },
    width: width,
    x: {
        axis: "top",
        tickFormat: s => `$${s}k`,
        transform: s => s / 1000,
        label: null
    },
    y: { axis: null },
    marks: [
        Plot.barX(filteredMedianSalaries, {
            x: "medianSalary",
            y: "agency",
            fill: (s) => (s.medianSalary >= calculatedAnnualLivingWage ? "green" : "red"), 
            sort: {y: "-x"}
        }),
        // for higher salaries
        Plot.text(filteredMedianSalaries, {
            filter: s => s.medianSalary >= 65000,
            text: s => `${s.agency} ($${Math.round(s.medianSalary / 1000)}k)`,
            textAnchor: "end",
            x: "medianSalary",
            y: "agency",
            dx: -3,
        }),
        // for lower salaries
        Plot.text(filteredMedianSalaries, {
            filter: s => s.medianSalary < 65000,
            text: s => `${s.agency} ($${Math.round(s.medianSalary / 1000)}k)`,
            textAnchor: "start",
            x: "medianSalary",
            y: "agency",
            dx: 4,
        })
    ]
});
```
<div class="card">${resize((width) => allMedianSalariesPlot)}</div>
