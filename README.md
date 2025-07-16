# 🧠 Tic-Tac-Toe Minimax Implementation

This project is a Python implementation of the classic **Tic-Tac-Toe (Jogo da Velha)** game using the **Minimax algorithm**, developed as part of a learning activity for the **Oracle Next Education** program.

It explores basic AI techniques for turn-based games and reinforces key concepts such as game state representation, recursion, decision trees, and evaluation functions.

---

## 🎯 Objective

Build a Tic-Tac-Toe AI that:
- Analyzes all possible game states.
- Chooses the optimal move using **Minimax**.
- Plays perfectly against any opponent.

---

## 🚀 Features

- ✅ Functional Minimax algorithm with depth tracking
- 🎮 Console-based game state rendering
- 🧠 AI always chooses the best move
- ♻️ Full simulation of game states and outcomes

---

## 📂 File Overview

| File              | Description                              |
|-------------------|------------------------------------------|
| `main.py`         | Core logic of the game and AI decision   |
| `imprimirTabu()`  | Displays board in human-readable format  |
| `minimax()`       | Returns the optimal move using Minimax   |

---

## 🧩 How It Works

- The board is represented as a 1D list of 9 elements:
  - `0` = empty
  - `1` = player X
  - `-1` = player O

- Game logic functions:
  - `estadoObjetivo()`: checks for a winner or draw
  - `playerVez()`: determines whose turn it is
  - `acaoSucessora()`: generates all valid moves
  - `proxEstado()`: returns a new board after a move
  - `geradorEstados()`: recursively evaluates outcomes
  - `minimax()`: chooses the best move based on Minimax
