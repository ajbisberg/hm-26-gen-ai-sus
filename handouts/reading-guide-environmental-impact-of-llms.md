# Reading Guide — Holistically Evaluating the Environmental Impact of Creating Language Models

**Generative AI & Sustainability · Munich Summer School 2026 · Week 2**

- **Assigned:** Monday, July 20 (end of day)
- **Due:** Tuesday, July 21, 10:10 — bring your written admission ticket to the discussion
- **Paper:** Jacob Morrison, Clara Na, Jared Fernandez, Tim Dettmers, Emma Strubell, Jesse Dodge. *Holistically Evaluating the Environmental Impact of Creating Language Models.* ICLR 2025 (spotlight).
- **Link:** <https://arxiv.org/abs/2503.05804>
- **Time budget:** 60–90 minutes. You do not need to understand every equation — you need the argument, the method, and the numbers.

## Why this paper

On Thursday you will pitch an AI product and defend its sustainability scorecard to an audience. This paper is the most complete public accounting of what it costs — in carbon *and* water — to create a family of language models, including the parts developers almost never report. It gives you the vocabulary and the numbers to make your scorecard honest.

## How to read it

1. Read the **abstract and introduction** closely (15 min).
2. Skim **related work** — note only what "prior estimates leave out" (5 min).
3. Read the **methodology** for structure, not formulas: what counts as *operational* vs. *embodied* impact, and what the authors include in "development" (15 min).
4. Read the **results** carefully — this is where the numbers live. Keep a list (20 min).
5. Read the **discussion/conclusion** closely: power fluctuations, transparency recommendations (15 min).

## Key terms to be able to explain

- Operational vs. **embodied** carbon
- **Development** cost (hyperparameter tuning, architecture tests, scaling-law experiments — the runs that get thrown away)
- Water usage effectiveness (on-site vs. off-site water)
- Inference **break-even point** (how many inferences until deployment impact passes training impact)

## Guiding questions (take brief notes)

1. The authors measure four phases: hardware manufacturing, development, final training, deployment. Which is largest? Which is most surprising to you, and why?
2. What fraction of the total impact came from *development* — and why don't companies report it?
3. Find the water numbers. The data center used water-free on-site cooling; where does the 2.769 million liters come from, then?
4. What happens to GPU power draw during checkpointing, and why do the authors call this a problem for electrical grids?
5. These are open models from 20M to 13B parameters. What do the authors say about how their findings scale to frontier models — and what does that imply about the numbers we *don't* see?
6. Which one recommendation from the conclusion would matter most if it became law (for example, in the EU AI Act)?

## Admission ticket (bring on paper, ~10 minutes to write)

Write, in a few sentences each:

1. **One number** from the paper that most changed your thinking, and what you would have guessed before reading.
2. **One question or critique** about the method — something you'd ask the authors.
3. **One implication for your team's startup:** what would you add to or change in your sustainability scorecard because of this paper?

Your ticket is your entry to the discussion and counts toward participation. In the discussion you will work in a five-person analytic team with an assigned role, so make your notes good enough that you could argue *either side* of the paper's claims.
