# ---- 1 ----
total_seconds = 42 * 60 + 42
print("1.", total_seconds, "seconds")

# ---- 2 ----
miles = 10 / 1.61
print(f"2. {miles:.2f} miles")

# ---- 3 ----
pace_seconds = total_seconds / miles
pace_minutes = int(pace_seconds // 60)
pace_secs = int(pace_seconds % 60)
print(f"3. Pace: {pace_minutes} minutes {pace_secs} seconds per mile")

total_hours = total_seconds / 3600
avg_speed = miles / total_hours
print(f"   Speed: {avg_speed:.2f} miles per hour")