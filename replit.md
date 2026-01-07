# Snackautomaat Project

## Overview
A Python educational project containing programming exercises and a final assignment (Eindopdracht) that simulates a snack vending machine with a GUI interface.

## Project Structure
- `Eindopdracht/` - Final assignment containing the snackautomaat GUI application
  - `main.py` - Main application using appJar GUI library
- `Opdrachten/` - Programming exercises organized by chapter
  - `Hoofdstuk 6/` - Chapter 6 exercises
  - `Hoofdstuk 8/` - Chapter 8 exercises
- `tricks.py` - Sample Python script

## Technology Stack
- **Language**: Python 3.11
- **GUI Library**: appJar (tkinter wrapper)
- **Display**: VNC (for desktop GUI applications)

## Running the Application
The project runs as a desktop GUI application using VNC output. The "Snackautomaat GUI" workflow launches the main application which displays a simulation window.

## Features
The snackautomaat (snack vending machine) simulates:
- 4 products with different prices and stock
- Customer payment processing
- Finite State Machine (FSM) for handling transactions
- Error handling for insufficient payment or out-of-stock items
- Sales statistics and logging
