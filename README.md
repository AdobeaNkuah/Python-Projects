# Python Projects
## Black Scholes Option Pricing Calculator ##
This python project can be used to determine the ideal pricing for a european call/put of an stock option through the Black-Scholes model.

### Black Scholes Formula ###
The Black and Scholes formula for the Call European Options is defined as follows:
![chapter9-8b1](https://user-images.githubusercontent.com/48498666/158127746-1463646d-a923-4f30-b0fe-b7af53b6f913.jpg)
![chapter9-8b](https://user-images.githubusercontent.com/48498666/158128832-cd739922-930f-4b40-8a74-b5aa64f7ebef.jpg)

Where:
N(x) is the cumulative distribution function of the standard normal distribution (the probability that a value less than (d) occurs)
- T – t is the time to maturity expressed as a fraction of the year
- S is the spot price of the underlying asset
- K is the strike price
- r is the risk-free interest rate (annual rate, expressed in terms of continuous compounding)
- σ is the volatility in the log-returns of the underlying
- μ is the mean
- ert (PV) is the discount factor

### Assumptions ###
•	It also makes assumptions that risk-free rates and volatility are constant over time, which doesn’t reflect real life. Volatility can fluctuate according to supply and demand, so you should keep all of these limits in mind as you work out your price.
•	The option only works with European options that come with a firm expiration date.
•	To begin with, it’s only applicable to European options because U.S. call options can be exercised before the contract’s expiration date. It doesn’t take transaction fees or taxes into account, nor does the original model factor in dividends.
•	Markets are efficient and liquid.
•	No transaction costs are included.
•	The volatility and risk-free rate of the underlying asset are both constant.
•	The underlying asset’s returns follow a lognormal distribution.
•	The model works with the assumption that asset prices can’t be negative, because zero is used as a boundary. This is why stock prices must follow a normal pattern of distribution
•	This model’s iteration Black Scholes model also assumes that no dividends are paid out during the option’s lifespan.
