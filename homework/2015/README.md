# Introduction to VLSI Design - 2015

Original PDFs and photograph panels mentioned below are stored only in the owner-only [private original archive](https://github.com/handsomegary/ncu-intro-vlsi-originals), under the same `homework/` or `exams/` path. This public folder contains the authored reports, reconstructions and verification evidence.

All four authentic instructor assignments are included, with complete standalone English LaTeX/PDF solutions and source comparison.

| Homework | Coverage | Verification |
|---|---|---|
| HW1 | Four MOS theory / MUX / static CMOS problems | 32 exhaustive Boolean cases; full series-channel derivation |
| HW2 | Input slew, clock critical path, mobility, noise margins | Reproducible analytical tables, actual unity-slope ideal VTC points |
| HW3 | Equal-size AND gate and 5-load short-circuit overlap sweep | Real HSPICE, both output directions, timestep checks, settled full-cycle integration |
| HW4 | 28T mirror and 38T valid cascaded domino full adders | Real HSPICE, 56 static transitions, 8 domino words, rise/fall sizing within3percent, fine-step check |

Follow each homework's README to reproduce its data. `D:/cic018.l` and the HSPICE license remain local. HW4 stops at pre-layout SPICE. The inverter power curve is explicitly an intrinsic-channel-overlap estimator, with supply power and external switching power separately reported. Slew balancing is a documented electrical target rather than a claim of exact equality on all paths and corners.

2014 has no original prompt and is skipped; student-only material is not reconstructed or published.
