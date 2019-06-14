class BuySell(object):
    def max_profit_buy_sell_once(self, prices):
        """
        compare_profit - Get the max profit by computing the difference
        between the current item in the list and the minimum amount so far.
        max_profit - Use the compare_profit value to compare with the max profit
        so far and get the max out of the two values.
        """
        message = ''
        max_profit = 0.0
        min_price = float('inf')

        d = {}
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            compare_profit = price - min_price
            d[i] = compare_profit
            max_profit = max(max_profit, compare_profit)

        if max_profit > 0:
            index_of_max_profit = max(d, key=d.get)
            dict_of_zero_profit = {
                k: v for (k, v) in d.items() if v == 0 and k < index_of_max_profit
            }
            buy = prices[max(dict_of_zero_profit, key=int)]
            sell = prices[index_of_max_profit]
            message = f'(Buying for ${buy} and Selling for ${sell})'

        return max_profit, message
