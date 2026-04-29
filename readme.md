# Use Case 4: Game Session Management

## Overview
Manages the full lifecycle of a gambling session.  
Controls session state, enforces stake boundaries, tracks gameplay activity, and automatically ends sessions on win or loss conditions.

---

## Goals
- Start and manage gambling sessions
- Continue play while stake remains within limits
- Pause and resume sessions safely
- Automatically end sessions on win/loss thresholds
- Track duration, games played, and session statistics

---

## Core Use Cases

### Start Session
- Initializes session with parameters
- Validates stake and boundary limits
- Sets session status to ACTIVE

### Continue Session
- Executes games sequentially
- Checks stake boundaries after each game

### Pause & Resume
- Allows pausing with reason tracking
- Accurately records pause durations
- Resumes gameplay safely

### Auto‑End Session
- Ends session on:
  - Upper limit reached (WIN)
  - Lower limit reached (LOSS)
  - Manual or timeout stop

### Track Session Metrics
- Total session duration
- Active vs paused time
- Number of games played
- Win/loss statistics

---

## Key Components

- **SessionStatus (Enum)** – INITIALIZED, ACTIVE, PAUSED, ENDED_WIN, ENDED_LOSS
- **SessionEndReason (Enum)** – UPPER_LIMIT, LOWER_LIMIT, MANUAL, TIMEOUT
- **GameRecord** – Records each game’s bet, outcome, stake change, duration
- **SessionParameters** – Configurable limits, bet ranges, probabilities
- **PauseRecord** – Tracks pause/resume cycles and durations
- **GamingSession** – Core session logic and state management
- **GameSessionManager** – Manages multiple sessions per gambler

---

## Key Features
- Automatic boundary detection and enforcement
- Multiple pause/resume cycles with full tracking
- Accurate duration breakdown (active vs paused)
- Detailed per‑game and session‑level audit trail
- Prevention of overlapping active sessions

---

## Validation & Errors
- Stake boundaries validated continuously
- Session state transitions strictly enforced
- Graceful handling of invalid actions (e.g., betting while paused)

