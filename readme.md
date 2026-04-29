# Use Case 5: Win/Loss Calculation

## Overview
Handles game outcome determination and comprehensive win/loss analytics.  
Calculates winnings and losses, updates running totals, and produces performance metrics at both game and session levels.

---

## Goals
- Determine game outcomes using probability
- Calculate winnings based on odds
- Deduct losses accurately from stake
- Maintain real‑time win/loss totals
- Track streaks and performance metrics

---

## Core Use Cases

### Determine Outcome
- Uses random or weighted‑probability strategies
- Supports house‑edge simulation

### Calculate Winnings
- Computes payout using configurable odds:
  - Fixed
  - Probability‑based
  - American
  - Decimal

### Calculate Losses
- Deducts bet amount from stake on loss
- Records loss details for reporting

### Maintain Running Totals
- Tracks cumulative wins, losses, and balance
- Updates after every game

### Compute Win/Loss Ratios
- Win rate and loss rate
- Net profit/loss
- ROI and profit factor

### Track Streaks
- Current and longest win/loss streaks
- Performance trend analysis

---

## Key Components

- **OutcomeStrategy** – Random and weighted probability implementations
- **OddsConfiguration** – Supports FIXED, PROBABILITY, AMERICAN, DECIMAL odds
- **GameResult** – Per‑game outcome, payout, and stake changes
- **WinLossStatistics** – Aggregated performance metrics and ratios
- **RunningTotals** – Real‑time balance and profit tracking
- **WinLossCalculator** – Central service for all calculations

---

## Key Features
- Multiple outcome strategies with house‑edge support
- Flexible odds systems
- Real‑time statistics and balance tracking
- Automatic streak detection
- Detailed performance metrics (win rate, ROI, profit factor)

---

## Validation & Errors
- Probability must be between 0 and 1
- Bet amount must be valid and available
- Safe handling of floating‑point edge cases
- Custom win/loss calculation exceptions
