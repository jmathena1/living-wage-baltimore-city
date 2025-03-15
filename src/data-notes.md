---
title: Data Notes
---

## What is a Living Wage?
<br>

From the team of MIT researchers that created it:  
> A living wage is what one full time-worker must earn on an hourly basis to help cover the cost of their family's minimum basic needs
where they live while still being self-sufficient. 

I decided to use a living wage rather than a poverty wage for this analysis because I wanted to:
1. emphasize that public sector workers do essential work for our communities and their salary should reflect that
2. reinforce that we should expect **any and every** full-time to pay us a wage that allows us to lead a dignified life
and not merely survive

MIT researchers update living wage measures across the US annually and their measures include expenses like child care, entertainment, and
basic savings.

You can learn more about the methodology at [livingwage.mit.edu](https://livingwage.mit.edu).

## Cleaning Baltimore City Employee Salary Data
<br>

This little report is a sequel to a more exploratory analysis I put out last year that examined the entire city employee salary dataset
available at the time. You can view that [here](https://citysalaries.johnwmathena.com) if you like. 

This round, I only analyzed data for
fiscal year 2024. Narrowing the data set made data storage and cleaning much easier. Additionally, you can only access MIT's living wage data
from their site a year at a time. I built a little lookup for the MIT living wages by family type and downloaded a CSV of the city salary
data for FY2024. However, the city salary data needed a bit of massaging after I took a look at it in Google Sheets.

I will detail the issues I noticed below and what I decided to do about them.

### Annual Salary or Gross Salary?
<br>


