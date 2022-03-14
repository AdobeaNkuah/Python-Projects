# Python Projects
## Black Scholes Option Pricing Calculator ##
This python project can be used to determine the ideal pricing for a european call/put of an stock option through the Black-Scholes model.

### Black Scholes Formula ###
The Black and Scholes formula for European Call Options is defined as follows:
<br>
![chapter9-8b1](https://user-images.githubusercontent.com/48498666/158127746-1463646d-a923-4f30-b0fe-b7af53b6f913.jpg)
<br>
![chapter9-8b](https://user-images.githubusercontent.com/48498666/158128832-cd739922-930f-4b40-8a74-b5aa64f7ebef.jpg)

Where:
- N(x) is the cumulative distribution function of the standard normal distribution (the probability that a value less than (d) occurs)
- T – t is the time to maturity expressed as a fraction of the year
- S is the spot price of the underlying asset
- K is the strike price
- r is the risk-free interest rate (annual rate, expressed in terms of continuous compounding)
- σ is the volatility in the log-returns of the underlying
- μ is the mean
- ert (PV) is the discount factor

### Assumptions ###
- This pricing model works for European options exclusively as European call options can only be excersised on the expiration date, unlike the U.S where call options can be exercised before the contract’s expiration date
- Assumes risk-free rates and volatility are constant over time, which doesn’t reflect real life fluctuation of supply and demand
- Does not take transaction fees, dividends, or taxes into account.
- Assumes Markets are efficient and liquid.
- The underlying asset’s returns follow a lognormal distribution.
- Assumes that asset prices can’t be negative, because zero is used as a boundary
