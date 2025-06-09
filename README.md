# OOP Python World Simulation

This project implements a simple virtual world written in Python.  The GUI
is built with **PyQt5** and allows the user to control a human character on a
board populated with various organisms.

## Setup

1. Install Python 3.8 or newer.
2. Install dependencies:

```bash
pip install PyQt5
```

## Running the Program

Start the simulation by executing `main.py`:

```bash
python main.py
```

A window will appear allowing you to create a new game or load a saved one.

## Controls

* **Arrow keys** – move the human.  Pressing any movement key will also
  advance the simulation by one turn.
* **Q** – activate the human's special ability.  After activation the ability
  has a cooldown period of several turns.
* Options in the menu allow starting a new game, saving the current state or
  loading a previously saved world.

The goal is simply to observe how organisms interact on the board.  Each turn
organisms act in order of initiative and may move, reproduce or fight
according to their species rules.
