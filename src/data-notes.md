---
title: Data Notes
---

## What is a Living Wage?

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
<br>
<br>

## Cleaning Baltimore City Employee Salary Data

This little report is a sequel to a more exploratory analysis I put out last year that examined the entire city employee salary dataset
available at the time. You can view that [here](https://citysalaries.johnwmathena.com) if you like. 

This round, I only analyzed data for
fiscal year 2024. Narrowing the data set made data storage and cleaning much easier. Additionally, you can only access MIT's living wage data
from their site a year at a time. I built a little lookup for the MIT living wages by family type and downloaded a CSV of the city salary
data for FY2024. However, the city salary data needed a bit of massaging after I took a look at it in Google Sheets.

I will detail the issues I noticed below and what I decided to do about them.
<br>
<br>

## AnnualSalary or GrossSalary?

The city salaries data set includes two salary fields: AnnualSalary and GrossSalary. To me, annual salary is the base salary an employee
earns in a given year, while gross is what a company actually paid out to an employee. For example, if my salary for DPW is $50k a year but
I start in October, the money I earn from DPW that year will likely be less than the $50k.

Unfortunately, numerous records in the set conflict with my definition above. I noticed records with an annual salary of zero and a non-zero
value for gross salary and vice-versa. Perhaps an employee starting a new job in the final pay period of a year would have an annual
salary and no gross salary. However, if an employee's annual salary is zero (perhaps an elected position or non-paid board position), why
would they have a gross salary? 

The data set did not come with a data dictionary that I could find, so I chose to excluded records like this. The `Environmental Control Board`, in particular, had multiple such records.
<br>
<br>

## Temporary and Part-time work not explicitly marked

Several city agencies employ many part-time and/or temporary workers to carry out their mission. These agencies include
- `Election Board`
- `Environmental Control Board`
- `Mayor's Office of Employment Development` (MOED)
- `Rec & Parks`, Administration and Recreation departments
- `Transportation`
- `Zoning and Appeals Board`

I presumed part-time or temporary status by looking at the salary values and their position titles. The Board of Elections sitting members
and election judges are not full time positions and their annual salaries ranged from zero to a couple hundred dollars. MOED and Rec & Parks
employ lots of seasonal workers through Youthworks and class instructors and aides. Their annual salaries often appeared to be hourly wages;
$15 or so depending on the class and level of experience perhaps. Transportation employs the crossing guards across the city, who I believe
only work during the school year.
<br>
<br>

## Only Annual Salaries Above $200

Lastly, I noticed a lot of the records appearing to be part time or temporary workers clustered between zero and $200 a year. After
that $200 mark, there was another cluster around $10k or $12k. So, I made a blanket decision to exclude records with an annual salary. 
