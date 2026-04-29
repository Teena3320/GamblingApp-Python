# Gambling App – Dev Branch

## Overview
This **dev branch** contains the complete modular implementation of the Gambling App, covering **all 7 use cases**.  
The system simulates a calculative gambler with strict stake control, validated betting logic, session management, and detailed analytics, following clean Object‑Oriented and service‑layer design.

---

## Implemented Use Cases

### UC1: Gambler Profile Management
Manages gambler identity, financial state, preferences, and statistics.

**Key Capabilities**
- Create, update, retrieve, validate, and reset gambler profiles
- Track initial/current stake and win/loss thresholds
- Maintain betting history and statistics

**Core Components**
- `GamblerProfile`
- `BettingPreferences`
- `GamblerStatistics`
- `GamblerProfileService`

---

### UC2: Stake Management Operations
Handles real‑time stake updates and boundary enforcement.

**Key Capabilities**
- Initialize and track stake balance
- Apply bet results, deposits, and withdrawals
- Enforce upper/lower boundaries
- Generate stake history reports

**Core Components**
- `StakeTransaction`
- `TransactionType`
- `StakeBoundary`
- `StakeMonitor`
- `StakeManagementService`

---

### UC3: Betting Mechanism
Implements betting execution and strategy handling.

**Key Capabilities**
- Place single or consecutive bets
- Validate bet amounts and probabilities
- Apply multiple betting strategies
- Automatically settle bets

**Strategies Included**
- Fixed Amount
- Percentage
- Martingale
- Reverse Martingale
- Fibonacci
- D’Alembert

**Core Components**
- `Bet`
- `BettingStrategy`
- `BettingSession`
- `BettingService`

---

### UC4: Game Session Management
Controls session lifecycle and game flow.

**Key Capabilities**
- Start, continue, pause, resume, and end sessions
- Auto‑end on win/loss thresholds
- Track game count and durations

**Core Components**
- `GamingSession`
- `SessionStatus`
- `SessionEndReason`
- `GameRecord`
- `GameSessionManager`

---

### UC5: Win/Loss Calculation
Performs outcome determination and analytics.

**Key Capabilities**
- Probability‑based outcome generation
- Flexible odds calculation
- Real‑time win/loss tracking
- Streak and performance metrics

**Core Components**
- `OutcomeStrategy`
- `OddsConfiguration`
- `GameResult`
- `WinLossStatistics`
- `WinLossCalculator`

---

### UC6: Input Validation & Error Handling
Ensures system safety and correctness.

**Key Capabilities**
- Validate stakes, bets, limits, and probabilities
- Prevent invalid numeric values
- Centralized rule configuration
- Graceful exception handling

**Core Components**
- `InputValidator`
- `ValidationConfig`
- `ValidationResult`
- Custom exception hierarchy

---

### UC7: User Interaction
Provides an interactive console interface.

**Key Capabilities**
- Display real‑time status and outcomes
- Menu‑driven user flow
- Safe input handling with feedback
- End‑of‑session reporting

**Core Components**
- `UserInterface`
- `InteractiveMenu`
- `GameStatusDisplay`
- `SessionSummary`
- `SimpleGameEngine`

---

## Design Principles
- Object‑Oriented Design (Encapsulation, Polymorphism, Inheritance)
- Service‑layer architecture
- Strategy pattern for betting logic
- DTO pattern for safe data exposure
- Full auditability and validation‑first approach


