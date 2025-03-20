def calculate_loan(principal, period, rate):
    interest = (principal * period * rate) / 100
    total_amount = principal + interest
    monthly_emi = total_amount / (period * 12)
    return interest, total_amount, monthly_emi
