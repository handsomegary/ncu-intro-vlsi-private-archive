# Source review and decisions

Review date: 2026-10-13. The supplied **Fall 2024** PDFs and instructor clarifications define the requirements. Code from other years is used only as an architectural reference. All authored reports and explanations are in English; original instructor attachments retain their original language and have labeled English translations.

## Original assignments

- `2024/assignments/homework1.pdf` through `homework4.pdf`: copied byte for byte, without rewriting the assignments.
- `hw3_instructor_testbench.sp`: original PWL sources, I/O names, 9 ns duration, CIN=0.
- `hw3_clarifications.txt`: original instructor attachment specifying W>=0.47 um, 1.8 V swing, energy=Pavg times 9 ns, and required patterns. See the [English translation](2024/assignments/hw3_clarifications.en.md).
- `hw4_clarifications.txt`: original full layout/DRC/LVS/PEX requirements. See the [English translation](2024/assignments/hw4_clarifications.en.md). This delivery follows the user's narrower request for pre-layout `.sp` files.

## Existing local answers

| Material | Content reviewed | Adoption or correction |
| --- | --- | --- |
| HW1 Reference A: supplied four-page correction/reference; Reference B: three-page `VLSI HW1.pdf` | All handwritten solutions and transistor connections; enlarged control complement bar | Independently simplify and verify connectivity, remove absorbed branches, and redraw complementary TG controls. A's central complement mark is visible, but its upper MOS symbol is unclear; no same-polarity-control fault is attributed to it. |
| HW2 `VLSI_HW2.pdf` | Stored voltage, leakage retention, pseudo-NMOS NOR sizing | Cross-check derivations; add retention conditions, sizing inequalities, and the BL readout qualification. |
| Supplied 2024 HW3 student archive, student ID 111501026 | Report and 88T XNOR/TG/mux code | Rerun an equivalent circuit under identical conditions and compare with reconstructed candidates; see HW3 measurements. |
| Supplied 2024 HW4 student archive, student ID 111501026 | Three-page report, 64T schematic, actual PEX files, testbench | Use the architecture as a candidate. The report reverses pre/post labels and its testbench combines two DUTs, so total power is not a single-design measurement. Its layout area and PEX are not results of this work. |

Original local filenames remain in the user's source folder. Reference labels and student IDs identify those files without requiring non-English filenames in authored reports. Existing student documents are not republished as new solutions.

## Public search

Queries included `Jin-Fu Li 2024 homework VLSI github`, `EE3032 Homework github`, `NCU VLSI 2024`, `four_bit_multbased_adder`, and `NCU VLSI`. Search visibility is limited; no claim is made that other 2024 solutions do not exist.

- [dOwOb1212/NCU_VLSI_Design_2023_HW](https://github.com/dOwOb1212/NCU_VLSI_Design_2023_HW): reviewed [`hw1/CLA_cmos.sp`](https://github.com/dOwOb1212/NCU_VLSI_Design_2023_HW/blob/main/hw1/CLA_cmos.sp), Git blob SHA `9bee2ead3081e2abb2e5e19fee6f47c9414c267c`. Its two-XNOR/carry-mux unit checks the carry equation, but carry still propagates bit by bit despite the CLA filename. This is an **8-bit** implementation with W=0.25/0.45 um and different vectors, below the 2024 minimum W=0.47 um. The full program was not copied into this repository.
- [Yeimaoz/NCU_VLSI](https://github.com/Yeimaoz/NCU_VLSI): found in search, but the API returned `409 Git Repository is empty`; no solution was available to read.

Each report records its derivation, sources, and verification conditions. Unverified values from existing answers are not presented as new measurements.

## HSPICE measurement definitions

The installed official PrimeSim HSPICE documentation was checked: `docs_help/hspice_6/selecting_simulation_output_parameters.htm`, **Power Output**. `POWER` includes dissipation and changes in stored energy. Its sign convention gives the negative sum of power absorbed by all independent sources, including PWL input drivers. It differs from VDD-only supply power. Both are reported, and the instructor's total `POWER` definition is used for 9 ns energy.
