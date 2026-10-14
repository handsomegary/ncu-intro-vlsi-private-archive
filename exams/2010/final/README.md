# 2010 final

Original PDFs and photograph panels mentioned below are stored only in the owner-only [private original archive](https://github.com/handsomegary/ncu-intro-vlsi-originals), under the same `homework/` or `exams/` path. This public folder contains the authored reports, reconstructions and verification evidence.

[Original (private)](https://github.com/handsomegary/ncu-intro-vlsi-originals/blob/main/exams/2010/final/original-exam.pdf) preserves all three Fall 2010 pages byte-for-byte. [Reconstructed paper](exam.pdf) / [standalone TeX](exam.tex); [corrected solutions](solution.pdf) / [standalone TeX](solution.tex). All 130 printed points are retained.

Q2's positive-edge register and Q7's negative-edge, 16-MOS layout are different original circuits. Q4's fixed P1 and strict clock-power target are incompatible, as shown algebraically. Q5 preserves the 2010 values (Cz = 2 pF and PMOS threshold magnitude = 0.6 V); its legal sharing-only states pass the stated ideal voltage test. Q6 states signed skew and minimum-delay assumptions explicitly. Q8 uses square-law current balance to derive a beta ratio of 1; a graded resistor shortcut cannot establish that ratio.

`python verify.py` reproduces the ideal graph and analytical checks. Two pdfLaTeX passes compile each standalone source. No HSPICE measurement is asserted. See the sources and QA JSON.
