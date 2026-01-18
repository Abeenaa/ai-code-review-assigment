## Task 1 — Average Order Value

### 1. Issues identified in the original code and explanation

- **Incorrect calculation:** The code computes the sum of non-cancelled orders but divides by the total number of orders, including cancelled ones. This skews the average whenever there are cancelled orders in the list.
- **Division by zero risk:** If there are no orders, or if all orders are cancelled, the count remains nonzero (total length of orders), which can result in dividing by zero or returning the wrong result.
- **Incomplete exclusion:** The original explanation claims non-cancelled orders are “correctly excluded”, but only the sum excludes them, not the divisor.
- **Missing data safety:** The code does not guard against missing "amount" keys in the order dictionaries.

---

### 2. Description of the fixes

- Updated the function to only sum and count non-cancelled orders. The average is now correctly calculated using only those orders.
- Added a check to return `0` if there are no non-cancelled orders (avoiding division by zero and signaling the absence of valid data).
- Used `.get` to safely access the 'amount' value with a default of 0 in case it's missing.
- The function now robustly reflects standard business logic for average order value.

---

### 3. Correct explanation for the revised code

This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of those orders. If all orders are cancelled or there are no orders, the function returns 0 to indicate that there is no valid average.

---

### 4. Engineering judgment (approve / request changes / reject) and rationale

**Request changes.**  
The original solution does not correctly handle the average when cancelled orders are present, resulting in misleading values. It also fails to handle the edge case when there are no valid orders to average. The revised version addresses both of these issues and is safer for production use.
