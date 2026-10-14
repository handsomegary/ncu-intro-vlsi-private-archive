# Fall 2023 — HW1 through HW4

Original PDFs and photograph panels mentioned below are stored only in the owner-only [private original archive](https://github.com/handsomegary/ncu-intro-vlsi-originals), under the same `homework/` or `exams/` path. This public folder contains the authored reports, reconstructions and verification evidence.

All four original [assignment PDFs](assignments/) are preserved byte for byte.
The reports are in English and include the independent derivations, reference
comparison and actual verification conditions.

| Homework | Report | Runnable deliverables |
|---|---|---|
| [HW1](HW1/) | [LaTeX](HW1/solution.tex), [PDF](HW1/solution.pdf) | CMOS diagrams; 284 functional switch-connectivity checks |
| [HW2](HW2/) | [LaTeX](HW2/solution.tex), [PDF](HW2/solution.pdf) | Dual-Vt derivation, retention and sizing; Python and three HSPICE decks |
| [HW3](HW3/) | [LaTeX](HW3/solution.tex), [PDF](HW3/solution.pdf) | 84T static CMOS three-bit RCA; 128 states and 896 directed single-input transitions |
| [HW4](HW4/) | [LaTeX](HW4/solution.tex), [PDF](HW4/solution.pdf) | Same pre-layout RCA and independent 128-state HSPICE rerun |

Important prompt details: HW1 Q1(a) is complemented AOI, not positive AO.
HW2 Q3 says **smallest** low voltage; its literal ratio 2.25 and the conventional
maximum-low ratio 4.5 are derived separately. HW3's three-stage diagram resolves
its wording “four full adders.” HW4 follows the user's pre-layout-only scope.

See [SOURCES.md](SOURCES.md) for the existing-answer review and integration decisions.
Use the local CIC018 model, default `D:/cic018.l`; it is not included in the repository.
