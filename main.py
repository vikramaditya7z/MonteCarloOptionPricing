import numpy as np
import matplotlib.pyplot as plt

from monte_carlo import (
    run_monte_carlo,
    simulate_path_for_plot
)

from black_scholes import (
    black_scholes_call
)

# Parameters

initial_price = 100
strike_price = 100
volatility = 0.20
days = 100
risk_free_rate = 0.05
drift = risk_free_rate

T = days / 252

# Convergence Analysis

simulation_counts = [
    100,
    500,
    1000,
    5000,
    10000,
    50000,
    100000
]

monte_carlo_prices = []

for simulation_count in simulation_counts:

    average_payoff, _ = run_monte_carlo(
        initial_price,
        strike_price,
        drift,
        volatility,
        days,
        simulation_count
    )

    option_price = average_payoff * np.exp(
        -risk_free_rate * T
    )

    monte_carlo_prices.append(option_price)

# Black-Scholes

callprice = black_scholes_call(
    initial_price,
    strike_price,
    risk_free_rate,
    volatility,
    T
)

print("Monte Carlo")
print("Option Price Today:", option_price)

print("-----------------------------------")

print("Black Scholes")
print("Call Price:", callprice)

print("-----------------------------------")

print("Difference:", abs(option_price - callprice))

# Convergence Graph

plt.style.use("dark_background")

plt.figure(figsize=(10, 6), facecolor="black")

plt.plot(
    simulation_counts,
    monte_carlo_prices,
    marker="o",
    linewidth=2,
    color="#00ff41",
    label="Monte Carlo"
)

plt.axhline(
    y=callprice,
    linestyle="--",
    linewidth=2,
    color="#ff3131",
    label="Black-Scholes"
)

plt.xscale("log")
plt.grid(alpha=0.3, color="#00ff41")

plt.xlabel("Number of Simulations", color="#00ff41")
plt.ylabel("Option Price", color="#00ff41")
plt.title(
    "Monte Carlo Convergence",
    color="#00ff41",
    fontsize=18
)

plt.legend()

plt.savefig(
    "images/convergence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Stock Path Visualization

plt.figure(figsize=(10, 6), facecolor="black")

for _ in range(10):

    path = simulate_path_for_plot(
        initial_price,
        drift,
        volatility,
        days
    )

    plt.plot(
        path,
        linewidth=1.5
    )

plt.grid(alpha=0.3, color="#00ff41")

plt.xlabel("Days", color="#00ff41")
plt.ylabel("Stock Price", color="#00ff41")
plt.title(
    "Simulated GBM Stock Price Paths",
    color="#00ff41",
    fontsize=18
)

plt.savefig(
    "images/stock_paths.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()