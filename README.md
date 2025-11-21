# Password Generator

This project is a simple yet flexible password generator written in Python. It provides three types of passwords:

* **PIN**: Generates numeric PIN codes.
* **Random Password**: Generates random strings based on selected character sets.
* **Memorable Password**: Generates passwords using random words, optionally with mixed casing.

---

## 🚀 Features

### 🔢 PIN Password

* Generates a numeric password.
* First digit is always non-zero.
* Remaining digits are chosen randomly.

### 🔐 Random Password

* You can choose to include:

  * Digits (`0-9`)
  * Letters (`a-z`, `A-Z`)
  * Special characters (`!@#$%^&*` etc.)
* Fully customizable output.

### 🧠 Memorable Password

* Generates passwords based on a list of words imported from `word.py`.
* Words are joined with a separator (default: `-`).
* Randomly capitalizes some words for extra uniqueness.

---

## 📦 Project Structure

```
project-folder/
|── src
|  │── main.py
|  │── word.py
│── README.md
```

`word.py` must contain a list variable named `words`:

```python
words = ["apple", "river", "moon", "storm", ...]
```

---

## 📚 Usage

The main class for generating passwords is `PasswordGenerator`.

Example:

```python
generated_obj = PasswordGenerator()

# PIN
pin = generated_obj.generate_password(type='pin', length=4)

# Random Password
random_pass = generated_obj.generate_password(type="random", length=4)

# Memorable Password
memorable = generated_obj.generate_password(type="memorable", length=4)

print('pin password= ', pin)
print('random password= ', random_pass)
print('memorable password= ', memorable)
```

---

## 🛠 How It Works

### Factory Pattern

`FactoryPasswordType` determines which password type should be created:

* `pin` → `Pin_pass`
* `random` → `Random_pass`
* `memorabel` → `Memorabel_pass`

Each class implements the abstract `PasswordType` and has its own `generate()` method.

---

## ✨ Future Improvements

* Return password strings instead of printing them.
* Add strength evaluation for generated passwords.
* Add CLI or GUI interface.
