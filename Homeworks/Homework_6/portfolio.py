__all__ = ['calculate_portfolio_value', 'calculate_portfolio_return', 'get_most_profitable_stock']


_start_price_portfolio = {}


# цена портфеля
def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _start_price_portfolio
    _start_price_portfolio = prices.copy()
    portfolio_price: float = 0
    for key, value in stocks.items():
        portfolio_price += value * prices.get(key)
    return portfolio_price


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round((current_value - initial_value) / initial_value * 100, 2)


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    max_profit: float = 0
    for key, value in prices.items():
        if key in stocks:
            if value - _start_price_portfolio[key] > max_profit:
                stock_name, max_profit = key, value - _start_price_portfolio[key]
    return stock_name


if __name__ == '__main__':
    my_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices_first = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    prices_second = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    initial_value_ = calculate_portfolio_value(my_stocks, prices_first)
    current_value_ = calculate_portfolio_value(my_stocks, prices_first)
    print(initial_value_)
    print(calculate_portfolio_return(initial_value_, current_value_))
    print(get_most_profitable_stock(my_stocks, prices_second))