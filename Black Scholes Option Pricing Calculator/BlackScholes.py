"""
Variable definitions:
	S: current asset stock price
	K: strike price
	r: risk-free interest rate
	t: time to expiration expressed as fraction of year
	μ, mew: mean
	σ, sigma: asset volatility (standard deviation of log returns)
	***N(d1):
		For call option: future value of stock given stock_price >= strike_price at option expiration
		For put option: future value of stock given stock_price < strike_price at option expiration
	***N(d2):
		For call option: P(stock_price >= strike_price) at option expiration
		For put option: P(stock_price < strike_price) at option expiration
"""
import math
from scipy.stats import norm

val = 0.1
# Prompt user to enter variable values
while val is not float:
    try:
        S = float(input("Type stock price, S:  "))  # test entered value using typecast to ensure it's a number
        val = S
    except ValueError:
        print("That's not a number")

while K is not float:
    try:
        K = float(input("Type strike price, K:  "))
    except ValueError:
        print("That's not a number")

while r is not float:
    try:
        r = float(input("Type risk-free interest rate (floating point ratio), r:  "))
    except ValueError:
        print("That's not a number")

while σ is not float:
    try:
        σ = float(input("Type asset volatility (floating point ratio), σ:  "))
    except ValueError:
        print("That's not a number")

while t is not float:
    try:
        t = float(input("Type time to expiration (fraction of year), t:  "))
    except ValueError:
        print("That's not a number")


# def normal_pdf(x, μ, σ):
#     numerator = math.exp(-0.5 * math.pow((x - μ)/σ, 2))
#     denominator = math.sqrt(2 * math.pi) * σ
#     return numerator / denominator


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
    C = S*N(d1, μ, σ) - PV*N(d2, μ, σ)
    return C


def put_price(S, K, r, μ, σ, t, PV,  d1, d2):
    P = PV*N(-d2, μ, σ) - S*N(-d1, μ, σ)
    return P

#def main():
