# Module 2 Checkpoint 1: Quick Checks Answers

**2.1: Q1 b, Q2 b, Q3 b, Q4 a, Q5 b, Q6 200 tokens in 3.5 seconds**
*Note for Q6:* The duration `3_500_000_000` divided by `1_000_000_000` gives exactly 3.5, and `:.1f` ensures one decimal place.

**2.2: Q1 b, Q2 b, Q3 b, Q4 a, Q5 b, Q6 ['sys', 'u2', 'a2', 'u3'] 6**
*Note for Q6:* `[history[0]]` keeps the first item ('sys'). `history[-3:]` slices the last 3 items. The total length of the original list remains 6.

**2.3: Q1 b, Q2 c, Q3 b, Q4 b, Q5 b, Q6 {'cupcake': 7, 'brownie': 0, 'donut': 8} 3 True**
*Note for Q6:* 'cupcake' becomes 12 - 5 = 7. 'donut' is added. Total items (len) are now 3. 'brownie' exists in the dictionary, so `in` returns True.

**2.4: Q1 b, Q2 b, Q3 b, Q4 b, Q5 b, Q6 2: complaint \n 3**
*Note for Q6:* The `continue` skips the empty review without incrementing the count. It prints "2: complaint" for the word "late", and the final `count` printed on the next line is 3.