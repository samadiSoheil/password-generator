# 🔐 Password Generator

This project is a **modular and extensible password generator** implemented using the **Factory Design Pattern**.

It supports three types of passwords:

- **PIN** — Numeric PIN code with a non-zero first digit  
- **Random Password** — Fully customizable random string  
- **Memorable Password** — Password generated using readable words  

---

## 🚀 Features

### 🔢 PIN Password
- Contains only digits  
- First digit is always non-zero  
- Customizable length (default: `8`)

---

### 🔐 Random Password
- Fully configurable  
- Supports:
  - Digits (`0–9`)
  - Letters (`a–z`, `A–Z`)
  - Special characters (`!@#$%^&*...`)
- Options are controlled via `kwargs`  
- Customizable length (default: `8`)

Available parameters:

```python
digits=True
letters=True
specific_chars=False
length=8
```

--- 

### 🧠 Memorable Password

- Generates passwords based on random words
- Random capitalization for added uniqueness
- Customizable:
    - Number of words (`length`)
    - Word separator (`separator`)
    - Custom word list (`words`)

--- 

## 📁 Project Structure

```
project-folder/
|── src
|  │── main.py
|  │── word.py
│── README.md
```

## 🧬 Architecture (Factory Pattern)

Each password type has its own class:

- `PinPass`
- `RandomPass`
- `MemorablePass`

Each type also has a corresponding factory:

- `PinPassFactory`
- `RandomPassFactory`
- `MemorablePassFactory`

The `password_selector()` function chooses the correct factory based on `pass_type`, creates an object, and generates the password.

---


## 🧪 Usage

```python
from main import main

# PIN
pin = main('pin', length=4)
print("PIN:", pin)

# Random Password
rand_pass = main('random', length=10, letters=True, digits=True, specific_chars=True)
print("Random:", rand_pass)

# Memorable Password
memorable = main(
    'memorable',
    length=3,
    words=['ali', 'reza', 'jafar', 'hamid'],
    separator='-'
)
print("Memorable:", memorable)
```


## ⚙️ Main Function

```python
main(pass_type, **kwargs)
```

Supported password types:
- `"pin"`
- `"random"`
- `"memorable"`