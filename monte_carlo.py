import numpy as np

def simulate_path(initial_price, drift, volatility, days):
    stockprice = initial_price
    dt = 1/252
    for _ in range(days):
        shock = np.random.normal()
        return_rate = ( (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * shock)
        stockprice = stockprice * np.exp(return_rate)

    return stockprice

def simulate_path_for_plot(
    initial_price,
    drift,
    volatility,
    days
):
    stockprice = initial_price
    prices = [stockprice]
    dt = 1/252
    for _ in range(days):
        shock = np.random.normal()
        return_rate = ( (drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * shock)
        stockprice = stockprice * np.exp(return_rate)
        prices.append(stockprice)
    return prices

def calculate_payoff(final_price, strike_price):
    return max(final_price - strike_price, 0)

def run_monte_carlo(
    initial_price,
    strike_price,
    drift,
    volatility,
    days,
    simulations
):
    finalprices = []
    payoffs = []

    for simulation in range(simulations):

        final_price = simulate_path(
            initial_price,
            drift,
            volatility,
            days
        )

        payoff = calculate_payoff(
            final_price,
            strike_price
        )

        finalprices.append(final_price)
        payoffs.append(payoff)

    average_payoff = np.mean(payoffs)

    return average_payoff, finalprices