#  Static Code Analysis – Reflection

**Name:** Nidhi Sanjay  
**USN:** PES1UG23CS391  
**Semester:** 5G  
**Lab:** Software Engineering – Lab 05  

---

##  Issue Summary

| **Issue** | **Type / Severity** | **Line(s)** | **Description** | **Fix Approach** |
|------------|--------------------|--------------|------------------|------------------|
| Use of `eval()` | Security / Medium (Bandit B307) | 59 | The `eval()` function executes arbitrary code and creates serious security risks. | Removed `eval()` entirely to eliminate unsafe execution. |
| Bare `except:` block | Logic / Medium (Bandit B110, Pylint W0702) | 19 | Catches all exceptions without specifying the type, which can hide real errors. | Replaced with specific exception handling (`except KeyError:`). |
| Mutable default argument `[]` | Bug / Medium (Pylint W0102) | 8 | Using a mutable default argument can retain unwanted state between function calls. | Replaced with `None` as default and initialized inside the function. |
| Missing file encoding | Maintainability / Medium (Pylint W1514) | 26, 32 | Files opened without specifying encoding can cause issues across different systems. | Added `encoding="utf-8"` in all file operations. |
| Missing input validation | Logic / Medium | Multiple | Functions accepted invalid or negative data, leading to potential runtime errors. | Added type and range checks for parameters in all functions. |
| Missing docstrings | Documentation / Low | Multiple | Several functions lacked descriptive docstrings, reducing readability. | Added short, clear docstrings explaining each function’s purpose. |
| Global variable usage | Maintainability / Low (Pylint W0603) | 27 | Use of `global` can make data flow harder to trace. | Modified dictionary in place to reduce reliance on the `global` keyword. |

---

##  Reflection

### 1️ Issue Difficulty Analysis

#### Easiest Fixes
The simplest fixes involved **formatting and minor style adjustments**, such as:
- Adding missing blank lines between function definitions (`E302`, `E305`).
- Ensuring a newline at the end of the file (`C0304`).

These were quick to resolve and did not affect functionality.

####  Hardest Fixes
The more complex issues included:
- Replacing generic `except:` blocks with specific exceptions like `KeyError`.
- Implementing proper input validation in functions like `add_item()` and `remove_item()`.
- Removing insecure use of `eval()` and rewriting file handling with `with open(...)`.

These required careful logic review to maintain both functionality and security.

---

### 2️ False Positives

Pylint raised a **`W0603: global-statement`** warning for using a global variable (`stock_data`).  
While technically valid, this warning was acceptable in this **small, single-module program** where the global variable simplifies operations.

---

### 3️ Integration of Static Analysis Tools

####  Local Development
Static analysis tools can be integrated into daily development by:
- Setting up **pre-commit hooks** (using the `pre-commit` library) to automatically check code before commits.  
- Using **IDE integrations** (like VS Code or PyCharm) to highlight issues in real time.

####  Continuous Integration (CI)
For long-term projects, these tools should be part of a **CI workflow** (e.g., GitHub Actions, GitLab CI):  
- Each pull request can automatically trigger linting and security checks.  
- Ensures that **code quality and security standards** remain consistent across all contributions.

---

### 4️ Observed Improvements

####  Code Quality
- Improved consistency, readability, and adherence to **PEP 8** guidelines.  
- Clearer naming conventions and structured function definitions.

####  Readability
- Added **docstrings** and **f-strings** for more expressive, human-readable output.  
- Simplified logic with better error messages and clear type handling.

####  Robustness & Security
- Removed unsafe functions like `eval()`.  
- Added **safe file handling** with UTF-8 encoding.  
- Implemented **specific exception handling** to prevent hidden bugs.  
- Strengthened **input validation** and eliminated potential logical errors.

---

###  Overall Outcome

After refactoring, the `inventory_system.py` script evolved from a basic procedural program into a **clean, secure, and production-ready module**.  

 **Final Pylint Score:** `10.00 / 10`  
 **Bandit Security Warnings:** `0`  

The refactored code now demonstrates **high maintainability, readability, and reliability**, suitable for professional software engineering standards.

---
