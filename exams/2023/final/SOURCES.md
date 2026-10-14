# Sources and comparison

`original-exam.pdf` is a byte-identical copy of the complete two-page Fall 2023 printed exam. Its filename and hash are in `sources.json`. The retypeset exam preserves all seven questions, all bars, the original 115-point sum, 14 layout crossings, and the capture-clock delay location. Geometry is normalized because the scan supplies no layout scale. The middle Q3 clock stroke touches its wire; the selected barred transcription and the unbarred alternative are explicitly qualified.

The local 17-page `期末整理.pdf` is a mixed-year study compilation. No matching graded answer booklet or identifiable grading provenance was found. It remains local and is not included in this package.

| Question | Reference comparison | Final treatment |
|---|---|---|
| Q1 | Page6 has useful common-rail and dynamic-logic notes; its physical-design definition conflates layout and fabrication. | Use the lecturer's primary definitions and vendor cell-purpose documentation; distinguish geometry generation from fabrication. |
| Q2 | Page12 explicitly assumes50% duty for an AND-to-OR problem with3/2ns and2.5/2ns edges. | That is a different problem. Retain both duty-adjustable166.667MHz and50%100MHz; derive reset concurrently from the original shared clock. |
| Q3 | Charge-sharing snippets on pages8–10 concern other circuits. | Read the original clock bars and internal x/y locations; verify both clock readings, a static-middle repair and a separately identified dynamic repair. |
| Q4 | Page8 contains related complemented complex-gate/pass-logic attempts, with uncertainty markings. | Independently derive the Shannon pass graph and NP XOR, then exhaustively check phases and output polarity. |
| Q5 | Pages2,4,13,16 use similar divider methods with different supply, thresholds, N1 widths or RC targets. | Retain the divider method and recompute all2023 values; state the nonunique pMOS family and literal gate-capacitance contradiction. |
| Q6 | Page14's functional inverter–NOR–inverter drawing matches the extracted function. | Preserve the useful functional result while restoring all14 physical devices, including four off isolation devices. |
| Q7 | Pages14–15 have related sequential sketches but different gate parameters/paths; the handwritten hold conclusion does not follow its own displayed inequality. | Derive the original graph, delayed R5/R6 taps, lockup-latch timing and a concrete reconvergent hazard independently. |

Primary references are listed with exact slide/page locators and access status in `sources.json`. Particularly relevant are lecturer Jin-Fu Li's Chapters4–7, Cadence physical-only-cell training, the Georgia Tech tap/latchup paper, and David Harris's standard-cell lecture. The lecturer's expected clock-distribution pair is H-tree and balanced-tree.
