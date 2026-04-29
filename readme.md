# Use Case 2: Stake Management Operations

## Overview
Handles real‑time tracking, validation, and reporting of a gambler’s stake.  
Ensures all stake changes are auditable, within defined boundaries, and accurately reflected throughout a gaming session.

---

## Goals
- Initialize and validate starting stake
- Track stake balance in real time
- Process stake changes after bets
- Enforce upper and lower stake limits
- Monitor stake fluctuations
- Generate detailed stake history reports

---

## Core Use Cases

### Initialize Stake
- Sets starting stake for a session  
- Validates against configured boundaries

### Track Stake
- Real‑time balance updates
- Full audit trail of all changes

### Calculate Stake
- Updates stake after bet win/loss
- Supports deposits, withdrawals, and adjustments

### Monitor Fluctuations
- Tracks peak and lowest stake
- Calculates volatility during the session

### Validate Boundaries
- Enforces upper and lower stake limits
- Issues warnings when approaching limits

### Generate Reports
- Complete transaction history
- Net profit/loss summary
- Transaction‑type breakdowns

---

## Key Components

- **StakeTransaction** – Records every stake change with timestamp and type
- **TransactionType (Enum)** – INITIAL, BET_WIN, BET_LOSS, DEPOSIT, WITHDRAWAL, RESET
- **StakeBoundary** – Defines min/max limits and warning thresholds
- **StakeMonitor** – Tracks live balance, peaks, lows, and volatility
- **StakeHistoryReport** – Generates summarized and detailed reports
- **StakeManagementService** – Central service implementing all operations

---

## Key Features
- Full transaction audit trail
- Automatic boundary validation and warnings
- Volatility and fluctuation analysis
- Support for deposits and withdrawals
- Thread‑safe, session‑ready design

---

## Validation & Errors
- Stake must never be negative
- Initial stake must fall within boundaries
- Boundary violations handled gracefully
- Custom stake‑specific exceptions used

