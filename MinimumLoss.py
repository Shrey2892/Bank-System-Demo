def minimize_loss():
    # Input: number of years
    n = int(input("Enter the number of years: "))
    
    # Input: prices for each year
    print(f"Enter the prices for {n} years separated by space:")
    prices = list(map(int, input().split()))
    
    if len(prices) != n:
        print(f"Error: You must enter exactly {n} prices.")
        return
    
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1

    # Check all buy-sell pairs
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1  # year index starts from 1
                    sell_year = j + 1

    if min_loss == float('inf'):
        print("No valid buy-sell pair with a loss found.")
    else:
        print(f"Buy in year {buy_year} and sell in year {sell_year} with minimum loss = {min_loss}")

# Run the function
minimize_loss()
