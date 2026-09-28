# 🏸 Badminton Knockout Tournament

A simple **Python-based Badminton Knockout Tournament Management System** created as a **Class 12 Python project**.

The program creates a knockout tournament for **8, 16, 32, or 64 players**, generates the fixture, records the winner of every match, automatically moves winners to the next round, and finally displays the tournament champion.

---

## 📌 Project Overview

In a knockout tournament, two players compete in each match. The winner moves to the next round, while the loser is eliminated.

The tournament continues until only one player remains.

### Tournament Flow

```text
8 Players
   ↓
4 Matches
   ↓
4 Winners
   ↓
2 Matches
   ↓
2 Winners
   ↓
Final Match
   ↓
🏆 Champion
```

For different numbers of players:

| Players | Round 1 Matches | Total Rounds |
| ------: | --------------: | -----------: |
|       8 |               4 |            3 |
|      16 |               8 |            4 |
|      32 |              16 |            5 |
|      64 |              32 |            6 |

---

## ✨ Features

* 🏸 Supports **8, 16, 32, and 64 players**
* 👤 Allows users to enter player names
* 📋 Automatically creates the knockout fixture
* 🏆 Records the winner of each match
* ➡️ Automatically moves winners to the next round
* 🔄 Continues until the final match
* 🥇 Displays the final tournament winner
* ❌ Validates incorrect player/winner input
* 💻 Simple command-line interface
* 🎓 Suitable for a **Class 12 Python project**

---

## 🛠️ Technologies Used

* **Python 3**
* Command Line / Terminal

No external Python libraries are required.

---

## 📂 Project Structure

```text
badminton-knockout/
│
├── badminton.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/khushiraghuwanshi07/badminton-knockout.git
```

### 2. Open the project folder

```bash
cd badminton-knockout
```

### 3. Run the Python program

```bash
python badminton.py
```

---

## 🎮 How to Use

### Step 1 — Enter number of players

The program asks for the number of players.

```text
Enter number of players (8/16/32/64): 8
```

### Step 2 — Enter player names

```text
Player 1: Rahul
Player 2: Aman
Player 3: Riya
Player 4: Priya
Player 5: Arjun
Player 6: Neha
Player 7: Karan
Player 8: Simran
```

### Step 3 — Play the matches

The program displays each match:

```text
Match 1
Rahul VS Aman

Enter winner: Rahul
```

The selected winner automatically moves to the next round.

### Step 4 — Final Winner

After all rounds are completed:

```text
=======================================================
              TOURNAMENT WINNER
=======================================================

Congratulations!
Winner: Rahul

=======================================================
          TOURNAMENT COMPLETED
=======================================================
```

---

## 🧠 How the Program Works

The program uses a **list** to store player names.

For example:

```python
players = ["Rahul", "Aman", "Riya", "Priya"]
```

Players are taken two at a time:

```text
Player 1 VS Player 2
Player 3 VS Player 4
```

The winner of every match is stored in a new list.

For example:

```text
Round 1:
A vs B → A
C vs D → D
E vs F → E
G vs H → H

Round 2:
A vs D → A
E vs H → H

Final:
A vs H → H
```

The final remaining player becomes the **tournament champion**.

---

## 🔢 Number of Rounds

The number of rounds depends on the number of players.

### 8 Players

```text
8 → 4 → 2 → 1
```

### 16 Players

```text
16 → 8 → 4 → 2 → 1
```

### 32 Players

```text
32 → 16 → 8 → 4 → 2 → 1
```

### 64 Players

```text
64 → 32 → 16 → 8 → 4 → 2 → 1
```

---

## 📚 Python Concepts Used

This project demonstrates several important Python concepts:

* Variables
* Lists
* `input()` function
* `print()` function
* `for` loop
* `while` loop
* `if-else` statements
* Nested logic
* User input validation
* List manipulation
* String formatting

---

## 🎯 Objective

The main objective of this project is to demonstrate how Python can be used to create a simple **sports tournament management system**.

It also helps in understanding how loops, lists, conditions, and user input can work together to solve a real-world problem.

---

## 🚀 Future Improvements

The project can be extended with:

* [ ] Automatic BYE generation for any number of players
* [ ] Player points and statistics
* [ ] Match scores
* [ ] Match history
* [ ] Player ranking
* [ ] Automatic fixture saving
* [ ] File handling using CSV/Text files
* [ ] Graphical User Interface (GUI)
* [ ] Database support

---

## 👩‍💻 Project Information

**Project:** Badminton Knockout Tournament
**Language:** Python
**Level:** Class 12
**Type:** School Python Project
**Tournament Format:** Knockout

---

## ⭐ Acknowledgement

This project was created for educational purposes to understand the implementation of a knockout tournament using Python programming concepts.

---

## 📄 License

This project is intended for educational and learning purposes.
