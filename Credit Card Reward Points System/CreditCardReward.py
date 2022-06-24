# By: Brenda Adobea Nkuah
from MaxPoints import points_earned

# Assuming that each $1 spend is only counted once, implement a method that takes the customer
# transactions as an input (Merchant Code → Purchase Amount) and calculates the total maximum
# rewards points earned for the month , the maximum reward points applied for each transaction.

# ● Rule 1: 500 points for every $75 spend at Sport Chek, $25 spend at Tim Hortons and $25 spend at Subway
# ● Rule 2: 300 points for every $75 spend at Sport Chek and $25 spend at Tim Hortons
# ● Rule 3: 200 points for every $75 spend at Sport Chek
# ● Rule 4: 150 points for every $25 spend at Sport Chek, $10 spend at Tim Hortons and $10 spend at Subway
# ● Rule 5: 75 points for every $25 spend at Sport Chek and $10 spend at Tim Hortons
# ● Rule 6: 75 points for every $20 spend at Sport Chek
# ● Rule 7: 1 point for every $1 spend for all other purchases (including leftover amount)


# given dictionary of transactions under a customer's reward account
transactions = {
    "T01": {"date": "2021-05-01", "merchant_code": "sportchek", "amount_cents": 21000},
    "T02": {"date": "2021-05-02", "merchant_code": "sportchek", "amount_cents": 8700},
    "T03": {"date": "2021-05-03", "merchant_code": "tim_hortons", "amount_cents": 323},
    "T04": {"date": "2021-05-04", "merchant_code": "tim_hortons", "amount_cents": 1267},
    "T05": {"date": "2021-05-05", "merchant_code": "tim_hortons", "amount_cents": 2116},
    "T06": {"date": "2021-05-06", "merchant_code": "tim_hortons", "amount_cents": 2211},
    "T07": {"date": "2021-05-07", "merchant_code": "subway", "amount_cents": 1853},
    "T08": {"date": "2021-05-08", "merchant_code": "subway", "amount_cents": 2153},
    "T09": {"date": "2021-05-09", "merchant_code": "sportchek", "amount_cents": 7326},
    "T10": {"date": "2021-05-10", "merchant_code": "tim_hortons", "amount_cents": 1321}
}

# transactions = {
#     'T1': {'date': '2021-05-09', 'merchant_code': 'sportchek', 'amount_cents': 2500},
#     'T2': {'date': '2021-05-10', 'merchant_code': 'tim_hortons', 'amount_cents': 1000},
#     'T3': {'date': '2021-05-10', 'merchant_code': 'the_bay', 'amount_cents': 500},
#     'T4': {'date': '2021-05-11', 'merchant_code': 'sportchek', 'amount_cents': 2000}
# }

# code written with the assumption given transactions all occur in the same month and does not verify date
# Max reward points per transaction
sport_chek_amount = 0
tim_hortons_amount = 0
subway_amount = 0
general_amount = 0  # For any merchant codes other than Sport Chek, Tim Hortons, and Subway
single_trans_points = []  # list containing total points per transaction
max_monthly_points = 0
i = 0  # iterator for string list items


# iterate through dictionary
for key, value in transactions.items():
    if value.get("merchant_code") == "sportchek":
        sport_chek_amount = value.get("amount_cents") // 100  # convert amount to dollars with floor division
        single_trans_points.append(points_earned(sport_chek_amount, 0, 0, 0))
    elif value.get("merchant_code") == "tim_hortons":
        tim_hortons_amount = value.get("amount_cents") // 100
        single_trans_points.append(points_earned(0, tim_hortons_amount, 0, 0))
    elif value.get("merchant_code") == "subway":
        subway_amount = value.get("amount_cents") // 100
        single_trans_points.append(points_earned(0, 0, subway_amount, 0))
    else:
        general_amount = value.get("amount_cents") // 100
        single_trans_points.append(points_earned(0, 0, 0, general_amount))

    # Calculate and display the total maximum rewards points for each transaction
    print("The maximum reward points for transaction " + str(key) + ": " + str(single_trans_points[i]))
    i += 1

# Calculate and display the total maximum rewards points earned for the month
max_monthly_points = sum(single_trans_points)
print("\nThe maximum reward points for the month " + str(max_monthly_points))
