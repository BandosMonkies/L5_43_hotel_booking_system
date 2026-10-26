# Reflection

## 1. Which issue was the most serious, and why?

The unsafe `eval` call was the most serious issue. A caller could supply an expression containing arbitrary Python code rather than a pricing calculation, so a feature intended to calculate a rate could execute commands or disclose data. It was removed instead of merely filtering a few known strings.

## 2. What did the analysis tools reveal that manual inspection might miss?

Pylint and Flake8 consistently identified maintainability problems such as naming conventions, unused imports, missing documentation, and the mutable default argument. Bandit focused attention on security-specific patterns such as `eval`, weak hashing, shell execution, and non-cryptographic randomness. Using all three gave broader coverage than relying on one tool.

## 3. Which fix required the most thought?

Replacing `eval` required the most design consideration because the original interface accepted a string expression. The safe replacement accepts a numeric multiplier, validates that it is positive, and keeps the calculation deterministic without accepting executable input. The demonstration was updated to use the safer interface.

## 4. How will you prevent similar issues in future code?

I will run static analysis and tests before submitting changes, treat user-controlled strings as data rather than code, use secure standard-library APIs for security-sensitive values, and avoid mutable defaults. I will also keep demonstrations behind an entry-point guard so importing a module remains side-effect free.

