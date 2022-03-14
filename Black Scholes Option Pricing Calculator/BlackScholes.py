"""
Variable definitions:
 S: current asset stock price
 K: strike price
 r: risk-free interest rate
 t: time to expiration expressed as fraction of year
 μ: mean
 σ: asset volatility (standard deviation of log returns)
 ***N(d1):
    For call option: future value of stock given stock price >= strike price at option expiration
    For put option: future value of stock given stock price < strike price at option expiration
 ***N(d2):
    For call option: P(stock_price >= strike_price) at option expiration
    For put option: P(stock_price < strike_price) at option expiration
"""
import math
from scipy.stats import norm

# initialize variables
S = 0  # Test ex S = 100
K = 0  # K = 100
r = 0  # r = 0.05
t = 0  # t = 0.5
μ = 0  # μ = 0
σ = 0  # σ = 0.3


# Prompt user to enter variable values
# Error handling for input data
while type(S) is not float:
    try:
        S = float(input("Type stock price, S:  "))  # test entered value using typecast to ensure it's a number
        print(S)
    except ValueError:
        print("Value error, entered value must be a number")

while type(K) is not float:
    try:
        K = float(input("Type strike price, K:  "))
    except ValueError:
        print("Value error, entered value must be a number")

while type(r) is not float:
    try:
        r = float(input("Type risk-free interest rate (floating point ratio), r:  "))
    except ValueError:
        print("Value error, entered value must be a number")

while type(σ) is not float:
    try:
        σ = float(input("Type asset volatility (floating point ratio), σ:  "))
    except ValueError:
        print("Value error, entered value must be a number")

while type(t) is not float:
    try:
        t = float(input("Type time to expiration (fraction of year), t:  "))
    except ValueError:
        print("Value error, entered value must be a number")


# Calculate the normal cumulative distribution
def N(x, μ, σ):
    return norm.cdf(x, μ, σ)


# Calculate the discount factor
def PV(K, r, t):
    return K*math.exp(-r * t)


def d1(S, K, r, σ, t):
    numerator = math.log(S / K) + (r + math.pow(σ, 2) / 2) * t
    denominator = σ * math.sqrt(t)
    return numerator / denominator


def d2(d1, t, σ):
    return d1 - σ*math.sqrt(t)


def call_price(S, K, r, μ, σ, t, PV,  d1, d2):
    C = S*N(d1, μ, σ) - PV(K, r, t)*N(d2, μ, σ)
    return C


def put_price(S, K, r, μ, σ, t, PV,  d1, d2):
    P = PV(K, r, t)*N(-d2, μ, σ) - S*N(-d1, μ, σ)
    return P


print("Call Price: " + call_price(S, K, r, μ, σ, t, PV, d1, d2))
print("Put Price: " + put_price(S, K, r, μ, σ, t, PV,  d1, d2))


# def main():
