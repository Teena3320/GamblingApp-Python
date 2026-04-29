# Use Case 3: Betting Mechanism

## Overview
Implements the core betting logic of the Gambling App.  
Handles bet placement, outcome determination, stake updates, and supports multiple betting strategies during a gaming session.

---

## Goals
- Place and validate bets
- Determine win/loss outcomes using probability
- Apply bet results to current stake
- Support multiple betting strategies
- Handle consecutive bets within a session

---

## Core Use Cases

### Place Bet
- Accepts bet amount and win probability
- Validates bet against current stake and limits

### Determine Outcome
- Uses probability‑based random simulation
- Produces win or loss result

### Settle Bet
- Updates stake after win or loss
- Records stake before and after the bet

### Strategy‑Based Betting
Supports multiple strategies:
- Fixed Amount
- Percentage of Stake
- Martingale
- Reverse Martingale
- Fibonacci
- D’Alembert

### Consecutive Bets
- Executes multiple bets in sequence
- Tracks results within a betting session

---

## Key Components

- **Bet** – Tracks bet ID, amount, odds, probability, outcome, stake before/after
- **BettingStrategy (Interface)** – Common contract for all strategies
- **Strategy Implementations** – Fixed, Percentage, Martingale, etc.
- **BettingSession** – Groups multiple bets with session stats
- **BettingService** – Central service handling all betting operations

---

## Key Features
- Probability‑based outcome generation
- Automatic stake updates on settlement
- Strategy pattern for easy extensibility
- Comprehensive validation on every bet
- Full audit trail of all bets in a session

---

## Validation & Errors
- Bet amount must be positive
- Bet must not exceed current stake
- Probability must be between 0 and 1
- Custom bet‑specific exceptions used

