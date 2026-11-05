def find_max_profit(n):
    if n <= 4:
        return 0, [(0, 0, 0)]

    max_earnings = 0
    valid_combinations = []

    # Total build time must be strictly less than n so the last building operates for >= 1 unit
    max_t = (n - 1) // 5

    for t in range(max_t, -1, -1):
        rem_after_t = (n - 1) - (t * 5)
        max_p = rem_after_t // 4

        for p in range(max_p, -1, -1):
            rem_after_p = rem_after_t - (p * 4)
            max_c = rem_after_p // 10

            for c in range(max_c, -1, -1):
                current_time = 0
                total_earning = 0

                # 1. Build Theatres (5 units build time, $1500 per operational unit)
                for _ in range(t):
                    current_time += 5
                    total_earning += (n - current_time) * 1500

                # 2. Build Pubs (4 units build time, $1000 per operational unit)
                for _ in range(p):
                    current_time += 4
                    total_earning += (n - current_time) * 1000

                # 3. Build Commercial Parks (10 units build time, $2000 per operational unit)
                for _ in range(c):
                    current_time += 10
                    total_earning += (n - current_time) * 2000

                # Track maximum earnings and all tied combinations
                if total_earning > max_earnings:
                    max_earnings = total_earning
                    valid_combinations = [(t, p, c)]
                elif total_earning == max_earnings and total_earning > 0:
                    valid_combinations.append((t, p, c))

    return max_earnings, valid_combinations


# Validate against Test Cases (7, 8, 13, and 49)
for time_unit in [7, 8, 13, 49]:
    max_earn, combinations = find_max_profit(time_unit)
    print(f"Time Unit = {time_unit}")
    print(f"Max Earnings: {max_earn}\n")
    print("Valid Combinations:")
    for t, p, c in combinations:
        print(f"T: {t}, P: {p}, C: {c}")
    print("-" * 35)