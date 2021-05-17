
# Queue

from collections import deque

bank = deque(["Ashikur", "Rahman", "Rashid"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person left.")


