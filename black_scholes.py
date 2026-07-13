import numpy as np
from scipy.stats import norm

def black_scholes_call(
    stock_price,
    strike_price,
    risk_free_rate,
    volatility,
    T
):
    d1 = (
        np.log(stock_price / strike_price)
        +
        (
            risk_free_rate
            +
            0.5 * volatility**2
        ) * T
    ) / (
        volatility * np.sqrt(T)
    )

    d2 = d1 - volatility * np.sqrt(T)

    N_d1 = norm.cdf(d1)
    N_d2 = norm.cdf(d2)

    call_price = (
    stock_price * N_d1
    -
    strike_price * np.exp(-risk_free_rate * T) * N_d2)

    return call_price