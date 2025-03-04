# Loan Payment Calculator

def calculate_monthly_payment(principal, annual_interest_rate, years):
    
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = years * 12
    if monthly_interest_rate > 0:
        monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    else:
        monthly_payment = principal / total_payments

    return monthly_payment

def main():
    principal = float(input("Enter the loan amount (Principal): $"))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term in years: "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    print(f"The monthly payment for a loan of ${principal:.2f} with an annual interest rate of {annual_interest_rate}% over {years} years is: ${monthly_payment:.2f}")
    
if __name__ == "__main__":
    main()

