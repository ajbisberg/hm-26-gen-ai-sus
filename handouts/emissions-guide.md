# Setup Guide — Agent Emissions Measurement

**Generative AI & Sustainability · Munich Summer School 2026 · Week 2 · Thursday, 23 July 2026**

Companion to slide deck `4.1 Agent Emissions Measurement Workshop`.

> **If you are a coding agent:** this document is your instruction set. The person you are
> helping is a student who may have never installed Python. Work through the phases in order,
> run the verification command at the end of each phase before moving on, and do not skip a
> phase because a later one "probably works anyway". Report the exact command output back to
> the student when something fails. Do not install anything not listed here, do not create or
> modify virtual environments unless the student asks, and do not edit files outside the
> student's working folder.

## Goal

By the end of this guide the laptop can run `weigh.py`, which sends one representative request
through two local LLMs ~20 times each and writes `emissions.csv` with energy (kWh), emissions
(kg CO₂e), and duration per model.

Everything runs locally. No account, no API key, no data leaves the laptop.

## What gets installed

| Piece | What it is | Why it is needed |
|---|---|---|
| Python 3 | the language `weigh.py` is written in | runs the measurement loop |
| Ollama desktop app | an app that runs LLMs on the laptop | no cloud call, so the energy is *this machine's* to measure |
| `codecarbon` (pip package) | energy tracker | measures energy, converts to CO₂e using grid intensity |
| `ollama` (pip package) | Python client | lets the script talk to the Ollama app — it is **not** the app itself |
| `qwen2.5:0.5b` (~0.4 GB) | small model | the cheap tier of the comparison |
| `gemma2:2b` (~1.6 GB) | mid model | the expensive tier of the comparison |

Total download: roughly 2 GB of models plus installers. Start the model pulls early —
on contested wifi they are the long pole.

## Platform conventions used below

- **macOS:** Terminal (Cmd + Space → "Terminal"), Python command is `python3`.
- **Windows:** PowerShell (Start menu → "PowerShell"), Python command is `python`.

Everything else is identical on both systems. Where this guide writes `python3`, Windows users
substitute `python`.

---

## Phase 1 · Install Python

**Skip if** `python3 --version` (macOS) / `python --version` (Windows) already prints 3.9 or newer.
Do not install a second Python if a working one exists — mismatched interpreters are the single
most common failure in this lab.

1. Download the installer from <https://www.python.org/downloads/>.
2. Run it.
   - **macOS:** click through with the defaults.
   - **Windows:** on the **first** screen, tick **"Add python.exe to PATH"** before clicking
     Install. Missing this checkbox breaks every later step.
3. Close the terminal and open a **new** one — installers only change the PATH of terminals
   opened afterwards.

**Verify:**

```
python3 --version      # Windows: python --version
```

Expect something like `Python 3.12.4`. If the command is not found, see Troubleshooting A.

## Phase 2 · Install the Python packages

```
python3 -m pip install codecarbon ollama      # Windows: python -m pip install codecarbon ollama
```

Use the `python3 -m pip` form, not bare `pip` — it guarantees the packages land in the same
interpreter that will run the script.

**Verify:**

```
python3 -c "import codecarbon, ollama; print('packages ok')"
```

Expect `packages ok`. If this prints `No module named ...`, see Troubleshooting B.

## Phase 3 · Install the Ollama desktop app

The `ollama` pip package installed in Phase 2 is only a client. The program that actually runs
models is a separate desktop app.

1. Download from <https://ollama.com/download>.
2. Install and launch it:
   - **macOS:** drag **Ollama** to Applications, then open it once.
   - **Windows:** run `OllamaSetup.exe`; it starts automatically after installing.
3. Leave it running. A menu-bar (macOS) or system-tray (Windows) icon means the model server
   is up.

**Verify:**

```
ollama --version
```

Expect a version number. On Windows this may need a fresh terminal. If the command is missing,
see Troubleshooting A; if it reports a connection problem, see Troubleshooting C.

## Phase 4 · Pull the two models

Same command on both systems. Run them one at a time; each prints a download progress bar.

```
ollama pull qwen2.5:0.5b
ollama pull gemma2:2b
```

**Verify:**

```
ollama list
```

Both `qwen2.5:0.5b` and `gemma2:2b` should be listed with a size. If a pull was interrupted,
re-run it — Ollama resumes rather than restarting.

**Verify the model actually answers** (this is the first end-to-end check):

```
ollama run qwen2.5:0.5b "say hello in one short sentence"
```

Expect a sentence of generated text.

## Phase 5 · Set up the working folder and the script

1. Make a folder and move into it:

   ```
   cd Documents
   mkdir weigh-your-agent
   cd weigh-your-agent
   ```

   Run these as three separate commands. On Windows, `cd Documents` works from the default
   PowerShell home directory.

2. Get `weigh.py`. Do **not** retype it. It lives in the course repo at:

   ```
   public/scripts/weigh.py
   ```

   Download it into `weigh-your-agent`. The script, `emissions.csv`, and any notes stay in this
   one folder — the terminal must be **in this folder** when the script runs.

3. Edit the `PROMPTS` list near the top of `weigh.py`. This is the **only** part that must
   change. Replace the two example strings with ~10–15 wordings of the team's one chosen
   request from the Monday agent map — vary wording, language, and politeness the way real
   users do. Leave `MODELS` and everything below it alone.

**Verify the folder and file:**

```
python3 -c "print(open('weigh.py').read()[:60])"
```

Expect the first lines of the script's docstring. An error here means the terminal is in the
wrong folder or the download did not land.

## Phase 6 · Run the measurement

```
python3 weigh.py       # Windows: python weigh.py
```

- Expect a few minutes per model.
- Keep the laptop **plugged in** and do not switch to other work — the script is measuring this
  machine, so background load contaminates the number.
- The script prints tok/s per request, then a per-model summary.

**Verify:** `emissions.csv` exists in the folder with one row per model, containing
`energy_consumed` (kWh), `emissions` (kg CO₂e), and `duration`.

## What the script does (for explaining it to the student)

- **`MODELS`** — the two tiers being compared; runs the whole procedure once per model.
- **Warm-up call** — loads the model into RAM *before* the tracker starts, so the measurement
  captures answering rather than loading.
- **`with EmissionsTracker(...)`** — the stopwatch. Everything inside the block is weighed.
- **`eval_count`** — tokens generated; **`eval_duration`** — nanoseconds spent generating.
  Together they give tok/s.
- The printed summary scales the raw numbers two ways:

  ```
  kWh per 1,000 requests = energy_consumed / len(PROMPTS) × 1000
  kWh per 1,000 tokens   = energy_consumed / gen_tokens × 1000
  ```

  Per request is what a user costs; per token is fairer across models, since the bigger model
  is not penalized merely for writing longer answers.

---

## Troubleshooting

**A. `python: command not found` / `ollama: command not found`**
Close the terminal and open a new one first — an installer's PATH change only reaches new
terminals. If it persists on Windows, re-run the Python installer and tick **Add python.exe to
PATH** (choose "Modify" if it offers a repair flow). On macOS, try `python3` rather than
`python`.

**B. `ModuleNotFoundError: No module named 'codecarbon'`**
The packages went to a different Python than the one running the script. Re-install using the
explicit form `python3 -m pip install codecarbon ollama` and run the script with that same
`python3`. Confirm with `python3 -m pip show codecarbon`.

**C. `connection refused` / `could not connect to ollama`**
The Ollama desktop app is not running. Launch it from Applications (macOS) or the Start menu
(Windows) and check for the tray/menu-bar icon, then re-run.

**D. `model not found`**
Run `ollama list` and re-run whichever `ollama pull` is missing.

**E. The laptop crawls on `gemma2:2b`**
That *is* a result. Note the tok/s, let it finish, and keep going — the slowdown is part of the
finding.

**F. `pip` warns about an outdated version or a `--user` install location**
Harmless. Do not chase it during the workshop.

## Fallbacks if setup fails

Setup is the risk in this lab, not the code. One working laptop is enough for the team
deliverable — pair up early rather than debugging four machines.

- **`gemma2:2b` still downloading:** run the loop with `qwen2.5:0.5b` alone and add the second
  row when the pull finishes.
- **Ollama will not install:** use the shared Colab notebook (GPU runtime; CodeCarbon works
  there) — link on the course pad.
- **Python will not install:** measure on a teammate's machine.
- **Everything fails:** the instructor's machine runs one team-supplied prompt set live; the
  team still records and cites the measurement.

## Honesty notes to carry into the write-up

- On many laptops CodeCarbon **estimates** CPU/GPU power from hardware specs rather than
  reading meters. Say so in the footnote.
- A laptop is not a datacenter: no PUE, no cooling overhead, different hardware. The number is
  a lower bound; the **ratio** between the two models is the robust finding.
- Suggested footnote:

  > *"Measured with CodeCarbon on [laptop model], 23 July 2026, n=20; German grid intensity."*

## References

- Ollama download — <https://ollama.com/download> · model library — <https://ollama.com/library>
- Python downloads — <https://www.python.org/downloads/>
- CodeCarbon documentation — <https://mlco2.github.io/codecarbon/>
- Ollama Python library — <https://github.com/ollama/ollama-python>

Setup details checked **23 July 2026**. Installers and commands change; prefer the linked
official documentation if a screen differs from this guide.
