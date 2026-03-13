import time

total_seconds = time.time()

days = int(total_seconds // (24 * 3600))
remaining = total_seconds % (24 * 3600)
hours = int(remaining // 3600)
minutes = int((remaining % 3600) // 60)
seconds = int(remaining % 60)

print(f"Days since epoch: {days} days")
print(f"Time of day: {hours:02d}:{minutes:02d}:{seconds:02d}")
