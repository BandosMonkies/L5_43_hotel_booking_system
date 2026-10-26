# Static Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Dynamic expression evaluation | Security | 39 | `eval` executes caller-controlled text and can run arbitrary Python code. | Replace the expression string with a validated numeric surge multiplier. |
| Shell command construction | Security | 56 | `os.system` passes a filename into a shell command, allowing command injection. | Use `Path.write_text` and a normal Python `print`. |
| Weak guest hashing | Security | 45 | MD5 is unsuitable for security-sensitive identifiers because it is cryptographically broken. | Use SHA-256 with explicit UTF-8 encoding. |
| Predictable booking references | Security | 49 | The standard `random` generator is predictable and is not appropriate for reference values. | Use `secrets.randbelow` while retaining four-digit references. |
| Mutable default argument | Reliability | 16 | A default list is shared across calls, causing reservations to leak between callers. | Use `None` and create a list for each call when needed. |
| Bare exception handler | Reliability | 26 | A bare `except` hides programming errors and silently reports failed cancellations as successful. | Use dictionary lookup and return an explicit success value. |
| Resource handling | Quality | 59 | The file is manually opened and closed, which can leak the handle if writing fails. | Use `Path.write_text`, which manages the file resource. |
| Missing entry-point guard | Quality | 69 | Importing the module unexpectedly runs the demonstration and writes a ledger file. | Call `main()` only under `if __name__ == "__main__"`. |

