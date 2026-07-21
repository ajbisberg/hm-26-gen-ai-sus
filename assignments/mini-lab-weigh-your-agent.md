# Mini-Lab — Weigh Your Agent

**Wednesday, July 22 · first ~35 minutes of the afternoon workshop (A1) · one measurement per team**

Your sustainability scorecard currently contains *cited* numbers. In this lab you replace one of them with a number you **measured yourself**. Thursday, when an audience member asks "your energy numbers — measured how?", you will have an answer nobody else in the room has.

## The task

Pick **one representative request** from your Monday agent map — the single interaction your prototype demonstrates (e.g., "find me a quiet room with outlets"). Run it through three models and weigh each run with CodeCarbon:

- **Small:** `qwen2.5:0.5b` via Ollama
- **Mid:** `gemma2:2b` via Ollama
- **Larger:** `mistral:7b` — the biggest of the three; skip if your laptop won't tolerate it (see Fallbacks)

Repeat the request ~20 times per model (vary the wording slightly) so the measurement isn't noise.

## Setup (do this before 1:15 if you can)

```bash
pip install codecarbon ollama
ollama pull qwen2.5:0.5b
ollama pull gemma2:2b
ollama pull mistral:7b
```

## Starter code

```python
import ollama
from codecarbon import EmissionsTracker

PROMPTS = [
    # ~20 realistic variants of YOUR chosen request, in your users' words
    "Ich suche einen ruhigen Lernplatz mit Steckdosen für 2 Stunden.",
    "Where can two of us study quietly near the library right now?",
    # ...
]

for model in ["qwen2.5:0.5b", "gemma2:2b", "mistral:7b"]:
    ollama.chat(model=model, messages=[{"role": "user", "content": "warm up"}])  # load into RAM first, don't measure it

    gen_tokens = 0
    with EmissionsTracker(project_name=f"weigh-{model}") as tracker:
        for p in PROMPTS:
            r = ollama.chat(model=model, messages=[{"role": "user", "content": p}])
            gen_tokens += r["eval_count"]              # tokens this model generated
            tok_per_s = r["eval_count"] / (r["eval_duration"] / 1e9)
            print(f"{model}: {tok_per_s:.1f} tok/s")

    # emissions.csv now has one row per model:
    # energy_consumed (kWh), emissions (kg CO2e), duration
    print(f"{model}: {gen_tokens} tokens generated total")
```

Scale the results two ways:
- `kWh per 1,000 requests = energy_consumed / len(PROMPTS) * 1000`
- `kWh per 1,000 tokens  = energy_consumed / gen_tokens * 1000`  ← fairer across models: a 7B model isn't penalized just for writing longer answers.

**tok/s** is the throughput number (`eval_count / eval_duration`); average it across the loop. The big small-vs-large gap here is half your routing argument.

## Judge quality, not just cost

Energy without quality is half a measurement. While one teammate runs the loop, the others score **5 answers from each model** with yesterday's rubric (correct? useful? tone?). Then answer the only question that matters:

> **Does the small model pass *your* quality bar? If yes — what justifies routing anything to the bigger tiers?**

## Deliverable (goes into today's evaluation plan + scorecard)

One measured row, cited honestly:

| Task | Model | tok/s | kWh / 1,000 req | g CO₂e / 1,000 req | kWh / 1,000 tok | Passes quality bar? |
|------|-------|-------|-----------------|--------------------|-----------------|---------------------|
| quiet-room request | qwen2.5:0.5b | *measured* | *measured* | *measured* | *measured* | yes / no |
| quiet-room request | gemma2:2b | *measured* | *measured* | *measured* | *measured* | yes / no |
| quiet-room request | mistral:7b | *measured* | *measured* | *measured* | *measured* | yes / no |

Footnote for your slide: *"Measured with CodeCarbon on [laptop model], July 22, 2026, n=20; German grid intensity."*

## Honesty notes (these are features, not bugs)

- On many laptops CodeCarbon **estimates** CPU/GPU power from hardware specs rather than reading meters — say so in the footnote. Remember Week 1's lesson: methodology spreads of 14× exist *between published papers*; your transparent estimate is still better than a copied headline.
- A laptop is not a datacenter: no PUE, no cooling overhead, different hardware. Your number is a **lower bound and a ratio** — the small-vs-large *ratio* is the robust finding, and the ratio is what justifies your routing tier.
- Wednesday's paper measured whole *agent loops*, not single calls. If time remains, run your prompt through a 2–3 step loop (retrieve → answer → summarize) and watch the multiplier appear in your own CSV.

## Fallbacks

- **No laptop can run 7B:** drop `mistral:7b` and compare `qwen2.5:0.5b` vs `gemma2:2b` — the ratio argument is identical.
- **Ollama won't install:** use the shared Colab notebook (GPU runtime; CodeCarbon works there) — link on the course pad.
- **Everything fails:** the instructor's machine runs one team-supplied prompt set live; you still record and cite the measurement.
