"""
Mini-Lab — Weigh Your Agent
Generative AI & Sustainability · Munich Summer School 2026 · Wed 22 July

Runs one representative request from your agent map through two local models
and measures the energy each one costs.

Before running (see slide deck 3.4 for the full walkthrough):

    python3 -m pip install codecarbon ollama     # Windows: python -m pip install ...
    ollama pull qwen2.5:0.5b
    ollama pull gemma2:2b

The Ollama desktop app must be installed and running (ollama.com/download) —
the `ollama` pip package is only the client that talks to it.

Then, from the folder containing this file:

    python3 weigh.py                             # Windows: python weigh.py

Output: emissions.csv in this folder, one row per model, plus a printed
summary you can paste straight into your scorecard.

Edit the prompts listed below.
"""

import ollama
from codecarbon import EmissionsTracker

MODELS = ["qwen2.5:0.5b", "gemma2:2b"]

PROMPTS = [
    # ~5-10 realistic variants of YOUR chosen request, in your users' words.
    # Replace these two examples. Vary wording, language, and politeness the
    # way real users do — that variation is what keeps the measurement honest.
    "Ich suche einen ruhigen Lernplatz mit Steckdosen für 2 Stunden.",
    "Where can two of us study quietly near the library right now?",
]

for model in MODELS:
    print(f"\n=== {model} ===")

    # Load the model into RAM before the tracker starts, so we measure
    # answering and not loading.
    ollama.chat(model=model, messages=[{"role": "user", "content": "warm up"}])

    gen_tokens = 0
    speeds = []

    with EmissionsTracker(project_name=f"weigh-{model}") as tracker:
        for p in PROMPTS:
            r = ollama.chat(model=model, messages=[{"role": "user", "content": p}])
            gen_tokens += r["eval_count"]                          # tokens generated
            tok_per_s = r["eval_count"] / (r["eval_duration"] / 1e9)
            speeds.append(tok_per_s)
            print(f"{tok_per_s:6.1f} tok/s")

    # CodeCarbon returns kWh for the block above; emissions.csv has the details.
    kwh = tracker.final_emissions_data.energy_consumed
    kg_co2e = tracker.final_emissions_data.emissions

    print(f"\n{model} summary")
    print(f"  requests            : {len(PROMPTS)}")
    print(f"  tokens generated    : {gen_tokens}")
    print(f"  average tok/s       : {sum(speeds) / len(speeds):.1f}")
    print(f"  kWh / 1,000 req     : {kwh / len(PROMPTS) * 1000:.4f}")
    print(f"  g CO2e / 1,000 req  : {kg_co2e / len(PROMPTS) * 1000 * 1000:.2f}")
    print(f"  kWh / 1,000 tokens  : {kwh / gen_tokens * 1000:.4f}")

print("\nemissions.csv written to this folder — one row per model.")
print("Footnote your numbers: measured with CodeCarbon on [laptop model],")
print(f"22 July 2026, n={len(PROMPTS)}; German grid intensity.")
