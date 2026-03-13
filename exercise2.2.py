import math

# ---- 1 ----
volume = (4/3) * math.pi * 5**3
print(f"1. Volume: {volume:.2f}")

# ---- 2 ----
price = 24.95 * 0.60
shipping = 3 + 0.75 * 59
total = price * 60 + shipping
print(f"2. Total wholesale cost: ${total:.2f}")

# ---- 3 ----
start = 6 * 60 + 52
time_run = 1*8*60+1*15 + 3*7*60+3*12 + 1*8*60+1*15
end = (start + time_run // 60) // 60
minutes = (start + time_run // 60) % 60
print(f"3. Home at: {end}:{minutes:02d} am")