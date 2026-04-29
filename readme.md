# Use Case 7: User Interaction

## Overview
Handles all user‑facing interactions in the Gambling App.  
Provides real‑time status updates, collects user inputs safely, displays outcomes, and presents comprehensive session summaries.

---

## Goals
- Display current stake and game status
- Prompt and validate user inputs
- Show game outcomes and updated balances
- Present end‑of‑session summaries
- Provide an interactive menu for all operations

---

## Core Use Cases

### Display Current Status
- Shows current stake
- Session state (active, paused, ended)
- Games played and win/loss stats

### Prompt for Bet Input
- Interactive bet amount input
- Integrated validation and retry handling

### Display Game Outcome
- Win/loss result
- Bet amount and payout
- Updated stake balance

### Display Session Summary
- Total games played
- Wins, losses, win rate
- Net profit/loss
- Session duration breakdown

### Interactive Menu
- Start new session
- Place bet / auto‑play
- Pause or resume session
- View status
- End session
- Exit application

---

## Key Components

- **GameStatusDisplay** – Centralized display of live game status
- **InteractiveMenu** – Menu‑driven navigation and user choices
- **SessionSummary** – Formatted end‑of‑session reporting
- **UserInterface** – Coordinates input/output flow
- **SimpleGameEngine** – Demonstration driver for all interactions

---

## Key Features
- Clear, user‑friendly console output
- Safe input handling with validation feedback
- Real‑time updates after every action
- Consistent formatting for all displays
- Clean session closure and exit handling

---

## Validation & Errors
- Prevents invalid inputs from reaching core logic
- Reuses centralized validation and exception handling
- Provides actionable error messages to users

