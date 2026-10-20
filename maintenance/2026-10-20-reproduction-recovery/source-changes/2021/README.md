# 2021 Introduction to VLSI Design solutions

Each homework has an English standalone `solution.tex`, its rendered PDF, runnable verification, and a README. Original prompts are in `assignments/`.

| Homework | Scope | Verification |
| --- | --- | --- |
| HW1 | All MOS theory, mux design, and CMOS diagrams | 32 Boolean cases and 5,050 ideal square-law operating points |
| HW2 | All three theory/design questions plus code/netlists | 64 real-CIC018 rotator cases, 4 real-CIC018 pseudo-NOR cases; 8 illustrative Level-1 Q1 cases |
| HW3 | Complete AND-gate pre-layout simulation and both-node delay measurements | 3 switching families, 3 cycles, 36 actual HSPICE delays, rail checks |
| HW4 | Requested pre-layout `.sp` and measurements; layout excluded | Independent repeat of all HW3 switching measurements |

For HW1: `cd HW1` and run `python verify_logic.py`. For HW2: run both `python verify_logic.py` and `python reproduce.py`. For HW3/HW4: run `python reproduce.py`. All simulation drivers accept `--hspice`, `--model`, `--check-environment`, and `--work`. Set your installed executable/model paths through flags or `HSPICE`/`CIC018_MODEL`; there are no machine-specific fallback paths. Supply a writable raw-output directory with `--work` to retain listings. No process model is redistributed. See the [download guide](../REPRODUCING.md).

CIC018 TT does not provide characterized low/high-threshold variants. Therefore Q1's dual-Vt placement is answered using the prompt's delay/slack assumptions; an explicitly educational Level-1 deck checks its topology only. Physical dual-Vt leakage and timing are not fabricated.

The supplied answers were read and compared first; independently verified improvements were integrated with attribution. See `SOURCES.md` for every source, hashes, and the comparison decisions.
