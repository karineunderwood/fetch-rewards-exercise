# Fetch Rewards Coding Exercise - Backend Software Engineering
## Summary





A web service that accepts HTTP requests and return responses based on the conditions outlined in the section below.

- Users have points in their account from multiple payers
- Payers submit their transactions to add/subtract points from user.
All the transactions will be stored in memory on the backend.
Payer's total points cannot go negative.
- Users can spend their points.
Oldest points are spent first accordingly in their transaction's timestamp, regardless of payer.

## Technologies
**Tech Stack:**

- Python
- Flask
- Jinja2
- HTML
- Bootstrap (only used for readability of the routes)

## Features

Show all routes

![All Routes](README-img/Routes-fetchrewards.jpg)


Add Transactions

![Add Transactions](README-img/add-transaction-route.jpg)

Add Response:

![Add Response](README-img/add-response.jpg)

Spend Points

![Spend Points](README-img/spend-route.jpg)

Spend Points Response:

Here you can see a list from the spend call

![Spend Response](README-img/spend-response.jpg)

Show Remainder Balance

Here is the final balance

![Show Remainder Balance](README-img/final-balance.jpg)

