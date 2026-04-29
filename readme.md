# Use Case 1: Gambler Profile Management

## Overview
Manages gambler identity, financial state, betting preferences, and statistics.  
This is the foundation for all other gambling app use cases.

---

## Goals
- Create and initialize a gambler profile
- Update personal info and betting preferences
- Retrieve financial status and statistics
- Validate gambler eligibility
- Reset profile for a new session

---

## Core Use Cases

### Create Profile
- Initial stake
- Win (upper) and loss (lower) thresholds
- Betting preferences  
**Validates:** minimum stake, threshold order, stake within limits

### Update Profile
- Personal info
- Preferences (min/max bet, strategy, auto‑play)
- Thresholds (validated)

### Retrieve Status
- Current & initial stake
- Wins, losses, total bets
- Net profit/loss, win rate
- Threshold alerts

### Validate Eligibility
- Stake meets requirements
- Loss threshold not breached
- Profile is active

### Reset Profile
- Reset stake to initial value
- Clear session stats
- Recalculate thresholds (optional)
- Preserve audit history

---

## Key Components

- **GamblerProfile** – Stores personal info, stakes, thresholds, history
- **BettingPreferences** – Encapsulates betting rules and settings
- **GamblerStatistics (DTO)** – Read‑only performance snapshot
- **GamblerProfileService** – Business logic for all operations
- **Demo App** – Shows lifecycle, validation, and reset flow

---

## Validation & Errors
- Positive, finite stake values
- Win threshold > loss threshold
- No negative stake
- Custom exceptions for clear, safe error handling



