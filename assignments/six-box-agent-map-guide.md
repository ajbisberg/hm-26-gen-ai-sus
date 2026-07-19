# Six-Box Agent Map — Team Guide and Worksheet

**Monday, July 20 · Team Agent-Design Workshop · one copy per team**

Use this guide to turn your Week 1 interview findings into **three specific agent use cases**. Complete one six-box map for each use case, then choose one interaction to prototype for Thursday.

## Start with a use case, not a technology

Write each use case as a concrete interaction:

> **When** [a specific user is in a specific situation], **the agent helps them** [complete one bounded task], **so that** [the user receives a clear benefit].

Example: *When a student needs a place for focused work, the agent helps them find a suitable available room, so that they spend less time searching and avoid disturbing active classes.*

Before mapping it, check that the use case:

- responds to a need found in your Week 1 interviews;
- creates clear value for a specific user;
- is feasible with identifiable data or tools;
- can be bounded enough to review, test, and explain;
- avoids unnecessary personal data; and
- contains one interaction your team could demonstrate Thursday.

## The six boxes

| Box | Question to answer | A strong entry names... |
|-----|--------------------|-------------------------|
| **1 · User input** | What arrives, and from whom? | a specific request, signal, or event and its source |
| **2 · Agent decision** | What does the model decide or infer? | one bounded judgment, classification, plan, or recommendation |
| **3 · Tools / data** | What may the agent read or call? | named data sources or APIs, plus access limits |
| **4 · Output** | What comes out? | a small, checkable suggestion, draft, alert, or proposed action |
| **5 · Human approval** | Who confirms what, and before which action? | the responsible person and a meaningful approval point |
| **6 · Failure mode** | What is the most likely harmful or incorrect outcome, and who catches it? | a concrete failure, detection method, and recovery |

The basic flow is **input → decision → tools/data → output**. Human approval is a gate before consequential action. The failure box sits underneath the whole flow: it explains how the system can go wrong and how people recover.

## Worked example — Room adaptation agent

**Use case:** When a team begins a workshop, the agent proposes a suitable room setup so that the space can adapt quickly without taking control away from its occupants.

| Box | Entry |
|-----|-------|
| **1 · User input** | A team member taps “workshop mode” on the room panel. |
| **2 · Agent decision** | Infer suitable layout, light, and air settings from the selected mode, occupancy, and CO₂ level. |
| **3 · Tools / data** | Read-only occupancy and noise sensors; room-control API may prepare a proposal but may not actuate it. |
| **4 · Output** | “Brighten the front, notify the shared display, and flag whiteboards for clearing.” |
| **5 · Human approval** | A person in the room reviews and confirms the proposed changes on the panel before anything changes. |
| **6 · Failure mode** | The agent chooses the wrong scene during active use; occupants notice immediately and restore the previous state with one-tap undo. |

## Map 1

**Agent name:** ________________________________________________

**Use case:** When ______________________________________________________________________

the agent helps _________________________________________________________________________

so that _________________________________________________________________________________

| Box | Your entry |
|-----|------------|
| **1 · User input** | |
| **2 · Agent decision** | |
| **3 · Tools / data** | |
| **4 · Output** | |
| **5 · Human approval** | |
| **6 · Failure mode + recovery** | |

## Map 2

**Agent name:** ________________________________________________

**Use case:** When ______________________________________________________________________

the agent helps _________________________________________________________________________

so that _________________________________________________________________________________

| Box | Your entry |
|-----|------------|
| **1 · User input** | |
| **2 · Agent decision** | |
| **3 · Tools / data** | |
| **4 · Output** | |
| **5 · Human approval** | |
| **6 · Failure mode + recovery** | |

## Map 3

**Agent name:** ________________________________________________

**Use case:** When ______________________________________________________________________

the agent helps _________________________________________________________________________

so that _________________________________________________________________________________

| Box | Your entry |
|-----|------------|
| **1 · User input** | |
| **2 · Agent decision** | |
| **3 · Tools / data** | |
| **4 · Output** | |
| **5 · Human approval** | |
| **6 · Failure mode + recovery** | |

## Choose Thursday's prototype interaction

Your prototype does not need to implement the whole agent. It should make **one important interaction** visible and testable.

**Chosen map:** 1 / 2 / 3

**The interaction we will demonstrate:** __________________________________________________

**What the user provides:** _______________________________________________________________

**What the prototype returns or changes:** _________________________________________________

**What we want feedback on:** _____________________________________________________________

## Final quality check

Before the 2:30 share-out, confirm:

- [ ] Each map addresses a named Week 1 interview need.
- [ ] Each agent has one bounded job rather than several unrelated jobs.
- [ ] Inputs, tools, and data sources are specific; “the internet” is not a source.
- [ ] Access is limited to what the agent actually needs.
- [ ] Outputs are small enough for a person to inspect.
- [ ] Human approval protects a consequential action without creating approval fatigue.
- [ ] Each failure mode names who or what detects the problem.
- [ ] Each failure mode includes a recovery, such as undo, correction, escalation, or safe shutdown.
- [ ] One interaction is feasible to demonstrate Thursday.

**Rule of thumb:** a precisely mapped, limited agent is stronger than an impressive but vague one.
