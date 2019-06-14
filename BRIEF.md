# Max Profit Calculator

## Scenario:

Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 10:00am local time.
The values are the price in dollars of a company's financial stock at that time.
So if the stock cost $5 at 11:00am, stock_prices_yesterday[60] = 5.
Write an efficient function that takes an array of stock prices and returns the max profit I could have made from 1 purchase and 1 sale of 1 financial stock yesterday.

You must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

For example:

var stock_prices_yesterday = [10, 7, 5, 8, 11, 9];

get_max_profit(stock_prices_yesterday)
returns 6 (buying for $5 and selling for $11)

## Expectation:

Implement a solution in any language.
Provide code that runs and prove it works (i.e. show something that can be run / or automated tests).
Include any comments that you think will be relevant to provide any context around the approach taken / solution developed.



