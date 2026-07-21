# Reading Guide — The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling

**Generative AI & Sustainability · Munich Summer School 2026 · Week 2**

- **Assigned:** Tuesday, July 21 (end of day)
- **Due:** Wednesday, July 22, 10:10 — bring your admission ticket to the discussion
- **Paper:** Jiin Kim, Byeongjun Shin, Jinha Chung, Minsoo Rhu. *The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective.* IEEE International Symposium on High-Performance Computer Architecture (HPCA), 2026.
- **Link:** <https://arxiv.org/abs/2506.04301>
- **Time budget:** 60–90 minutes. This is a systems paper — denser than Tuesday's. Read for the argument and the numbers, not the infrastructure details.

## Why this paper

Tuesday's paper measured the cost of *creating* a model. This one measures the cost of running **exactly what you designed on Monday**: agents that reason in loops, call tools, and retry until done. You have already met its headline number — the 136.5× agentic energy multiplier in your Week 1 compute assignment came from this paper, as a citation. Tonight you read where that number actually comes from, and what it means for the agent maps you will pitch on Thursday.

## How to read it

1. Read the **abstract and introduction** closely (10 min). Note the contrast the authors draw between *static, single-turn inference* (a chatbot answer) and *dynamic reasoning* (agents and test-time scaling).
2. Skim the **background** on agent designs — you know CoT, ReAct-style loops, and tool use from Monday; you just need to recognize the five agents they test (CoT, ReAct, Reflexion, LATS, LLMCompiler) (10 min).
3. Read the **characterization results** carefully — this is where the numbers live. Focus on: energy per query vs. the chatbot baseline, the latency split between LLM inference and tool execution, and GPU idle time (25 min).
4. Read the **test-time scaling** analysis for the trade-off curves: reflection depth, parallel reasoning, few-shot prompting (15 min).
5. Read the **datacenter-scale projections and recommendations** closely — this is the part your pitch's sustainability story lives in (10 min).
6. **Skip freely:** vLLM configuration, KV cache internals, and hardware setup details. You need the shape of the findings, not the serving stack.

## Key terms to be able to explain

- **Dynamic reasoning** vs. static single-turn inference
- **Test-time scaling** (spending more compute at inference: deeper reflection, parallel candidates)
- **Sequential vs. parallel scaling** (more reflection rounds vs. more candidates at once)
- **GPU idle time** (what the accelerator does while the agent waits on a tool or API)
- Energy **per query** vs. per token (why the agent multiplier is about *loops*, not model size)

## Guiding questions (take brief notes)

1. Establish the baseline: what does one ordinary chatbot query cost (the ShareGPT baseline), and what do Reflexion and LATS cost per query on the same models? Where does the ~130–136× multiplier come from?
2. Follow the energy inside one agent run: repeated LLM calls, growing context, and tool waits. On the Wikipedia-API workload, what fraction of execution time is the GPU *idle* — and who pays for idle GPUs?
3. Sequential scaling shows sharply diminishing returns (at one point, the same ~4% accuracy gain costs ~31× more latency). How would you decide, for a real product, when the next reflection round is no longer worth it?
4. Parallel reasoning improved accuracy *and* reduced latency in some settings. Why is it not a free lunch? (Think: concurrent requests, memory pressure, total energy.)
5. The 8B model with test-time scaling can approach 70B accuracy at lower total energy. What does that suggest about the routing tier you designed Monday?
6. The projections: an agentic service at current chatbot traffic ≈ the daily electricity of Seattle; at Google-Search scale, ~200 GW — nearly half the average U.S. grid load. Steelman and critique these extrapolations: what assumptions do they make, and which would you challenge?
7. Of the authors' recommendations (compute-aware workflows, mixing small and large models, adaptive scaling, quantization/distillation), which one would you actually adopt this week?

## Admission ticket

Write, in a few sentences each:

1. **One number** from the paper you would put on a slide in your final pitch — and how you would frame it so an audience trusts you *more*, not less, for showing it.
2. **One step or loop in your team's Monday agent map** you would now cut, cap, cache, or route to a smaller model because of this paper — and what you would expect to lose by doing it.
3. **One question** you want the group to argue about.