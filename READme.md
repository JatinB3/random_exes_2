# Random Data Generator Application

A Python-based application that generates random numbers, letters, and alphanumeric strings concurrently using multiprocessing. Includes built-in user authentication for secure access.

**Author:** Jatin  
**Date:** 28 Jan 2026

## Features

✨ **Concurrent Data Generation**
- Generates random numbers, letters, and alphanumeric strings simultaneously
- Uses multiprocessing for true parallel execution
- Updates every 2 seconds

🔐 **User Authentication**
- Password-protected application access
- 3-attempt limit for incorrect passwords
- Secure password input without echo

🔧 **Modular Architecture**
- Separated concerns with dedicated modules for each data type
- Easy to extend and maintain
- Clean separation between authentication and core logic

📦 **PyInstaller Ready**
- Includes `.spec` files for standalone executable creation
- Supports Windows multiprocessing freezing

## Prerequisites

- **Python 3.6+** (3.8+ recommended)
- **pip** (Python package manager)
- Windows, macOS, or Linux

## Installation

### 1. Clone or Download the Project
```bash
git clone https://github.com/JatinB3/random_exes_2.git
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
if you want to make exe file then install pyinstaller
```bash
pip install pyinstaller
```

## Usage

### Run with Authentication
```bash
python user_auth.py
```

**Default Password:** `123`

The application will:
1. Prompt for password
2. Allow 3 attempts
3. Start the random data generators upon successful authentication
4. Display random numbers, letters, and alphanumeric strings every 2 seconds

### Run Main Application Directly
```bash
python data_processor.py
```

This skips authentication and launches the generators directly.

### Run Individual Generators
```bash
# Random numbers only
python random_nums.py

# Random letters only
python random_letters.py

# Random alphanumeric strings only
python random_alphanum.py
```

### Stop the Application
Press `Ctrl+C` to gracefully shut down all processes.

## Module Documentation

### `user_auth.py`
Entry point with password authentication.
- Prompts user for password
- Maximum 3 attempts
- Launches `data_processor.run_main()` on success

### `data_processor.py`
Main application orchestrating concurrent data generation.
- Creates 3 separate processes
- Uses `multiprocessing.Event()` for clean shutdown
- Runs generator functions periodically every 2 seconds

### `random_nums.py`
Generates random integers between 1 and 100.
- `generate_random_numbers()` - Returns list of 10 random numbers

### `random_letters.py`
Generates random ASCII letters.
- `generate_random_letters()` - Returns list of 10 random letters

### `random_alphanum.py`
Generates random alphanumeric characters.
- `generate_random_alphanumeric()` - Returns list of 10 random alphanumeric chars

## Authentication

Default credentials:
- **Username:** N/A (password only)
- **Password:** `123`

To change the password, edit `user_auth.py`:
```python
correct_password = "123"  # Change this value
```

## Building Executables with PyInstaller

### Prerequisites
```bash
pip install pyinstaller
```

### Build Main Application with Authentication
```bash
pyinstaller --onefile --console -n random_gen_protected .\user_auth.py
```

### Build Individual Generators
```bash
pyinstaller --onefile -c -n random_gen .\data_processor.py
pyinstaller --one-file --console .\random_letters.py
```

Output executables will be in the `dist/` folder.

## Example Output

```
Generated random numbers: [45, 82, 19, 91, 7, 63, 38, 54, 21, 77]
Generated random letters: ['A', 'k', 'Q', 'w', 'P', 'x', 'M', 'j', 'C', 'f']
Generated random alphanumeric string: ['4', 'R', '9', 'h', 'E', '2', 'M', 'w', '7', 'L']
Generated random numbers: [33, 88, 12, 67, 55, 29, 42, 85, 11, 73]
...
```

## Technical Details

### Multiprocessing Pattern
- Uses `multiprocessing.Process` for concurrent execution
- Implements `multiprocessing.Event()` for coordinated shutdown
- Daemon processes ensure cleanup on exit
- Windows-compatible with `multiprocessing.freeze_support()`

### Dependencies
All imports are from Python's standard library:
- `multiprocessing` - Process management
- `random` - Random data generation
- `string` - Character pools
- `getpass` - Secure password input
- `time` - Timing intervals
- `sys` - System operations

### Threading Note
Multiprocessing was chosen over threading to:
- Achieve true parallelism (bypass Python's GIL)
- Provide better isolation between generators
- Enable independent process management

## Troubleshooting

### Authentication Issues
If you forget the password, edit `user_auth.py` and change the `correct_password` variable.

### Process Hangs
Press `Ctrl+C` to trigger graceful shutdown of all child processes.

### Windows Multiprocessing Error
If you get multiprocessing errors on Windows, ensure `multiprocessing.freeze_support()` is called (already included in the code).


## License

Open source - Feel free to use and modify as needed.

---

**Created:** 28 Jan 2026  
**Last Updated:** 29 Jan 2026
