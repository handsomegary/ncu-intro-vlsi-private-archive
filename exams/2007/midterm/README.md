# 2007 midterm

Original PDFs and photograph panels mentioned below are stored only in the owner-only [private original archive](https://github.com/handsomegary/ncu-intro-vlsi-originals), under the same `homework/` or `exams/` path. This public folder contains the authored reports, reconstructions and verification evidence.

[Original (private)](https://github.com/handsomegary/ncu-intro-vlsi-originals/blob/main/exams/2007/midterm/original-exam.pdf) is a byte-identical copy of all3 source pages. [Editable reconstructed paper](exam.tex) / [PDF](exam.pdf) and [independently corrected solutions](solution.tex) / [PDF](solution.pdf) retain every question. Printed percentages total110%, retained without rescaling.

Student work is locally compared, with explicit corrections: missing photoresist development; voltage-dependent pass source/drain labels; the TG requirement for XOR; and the fixed-channel-length constraint in Q7. Q3 activities require temporal independence that the prompt does not state, so exact occupancy/general activity and qualified independent-sample numbers are separated. Q5 uses literal unequal p/n sizes and a declared square-law overlap approximation; its ordering is not asserted as universal finite-load physical power.

Run `python verify.py`, then two pdfLaTeX passes on each standalone source. Sources and visual/compiler checks are recorded in the accompanying JSON and source review.
