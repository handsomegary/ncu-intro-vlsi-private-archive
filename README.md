# Introduction to VLSI Design — 2020, 2021, 2023 and 2024

National Central University, EE3032, Jin-Fu Li. Complete English LaTeX reports,
original assignment PDFs, CMOS transistor circuits and reproducible numerical
verification are organized by course year. The newly requested range is
**2023, 2021 and 2020**, with **2022 skipped**. Existing 2024 work remains available.

| Year | Coverage and reports | Numerical evidence |
|---|---|---|
| [2023](2023/README.md) | HW1–HW4; four LaTeX/PDF reports | 284 HW1 functional checks; three HW2 HSPICE decks; RCA: 128 states, 896 directed single-input transitions, 1 ps critical-case refinement |
| [2021](2021/README.md) | HW1–HW4; four LaTeX/PDF reports | HW1: 32 Boolean cases and 5050 square-law points; HW2: 64 electrical rotator cases; HW3/HW4: 36 delay measurements each |
| [2020](2020/README.md) | HW1–HW4; four LaTeX/PDF reports | HW1 32 Boolean cases; HW2 64 electrical rotator cases; HW3 18 runs with timestep/slew checks |
| [2024](2024/README.md) | Existing HW1–HW4 reports | HW1 100 checks; HW2 43 checks; HW3 512 measured states; HW4 eight prescribed vectors |

The original PDFs are in each year's `assignments/` directory, copied byte for
byte. The 2020 HW4 archive contains two original copies, both preserved.
Every new homework has `solution.tex`, a compiled and visually inspected
`solution.pdf`, and a README. HW1 contains derivations and transistor diagrams.
HW2 includes the full analytical answers plus executable logic/electrical
verification. HW3 contains actual HSPICE code and measured data.
**HW4 stops at pre-layout `.sp`**, as requested; no layout/DRC/LVS/PEX results
are claimed. Each year's HW4 circuit is the identical verified HW3 circuit;
the report states whether evidence was rerun or explicitly reused.

## Source review and interpretation

All three newly requested years have existing supplied answers. They were
read first, independently checked, and integrated with attribution and
explicit corrections in [2023](2023/SOURCES.md), [2021](2021/SOURCES.md),
[2020](2020/SOURCES.md), and the overall [source review](SOURCES.md).
Important corrections include the printed HW1 AOI overbar, incorrect body
connections or 3.3 V use on 1.8 V devices in some references, required loads,
and the distinction between an averaged selected-path delay and a measured
maximum. The 2023 HW2 “smallest low” wording is solved literally and separately
from the earlier years' conventional “highest low” specification.

## Reproduction

- Python 3. The saved-data package checker uses only the standard library.
- PrimeSim HSPICE S-2021.09; default `C:/synopsys/Hspice_S-2021.09/WIN64/hspice.com`.
- User-provided CIC018 process model; default `D:/cic018.l`, TT, 1.8 V, 25 C.
  The model remains external and is not redistributed.
- PDFLaTeX for reports; each `.tex` is self-contained. Optional Matplotlib
  regenerates the scientific waveform PNGs.

```sh
python verify_package.py
```

This verifies saved measurements, full assignment/report coverage, original
PDF hashes, artifact hashes, README links and matching HW3/HW4 netlists.
It does not launch a new simulation. Each homework README gives the actual
HSPICE reproduction command and model/executable overrides.
`MANIFEST.json` records text hashes with LF line endings and binary hashes
without transformation. Raw simulator/compiler outputs stay local.

The 2023 RCA's worst delay in the 2 ps sweep is 833.526988 ps over all settled
single-input transitions under its stated conditions. The refined critical-case
1 ps result is 833.905310 ps; the difference is 0.0454%. VDD-only supply power
is 177.082000 uW for its documented 384 ns workload. These numbers do not imply a PVT bound or
equal conditions across different years; see the individual reports.
