# Source and comparisons

Canonical original: `2008/final/final.pdf` in the local exam archive, three scanned pages with printed Fall 2008 footers and pages 1-1 through 1-3. All Q1-Q8 and figures are intact. Original handwritten annotations are excluded from reconstructed prompt text; the original PDF remains byte-identical. Printed weights total 115%.

The two-page `answer.pdf` and `final-answer.pdf` are byte-identical, with SHA-256 saved in `sources.json`. Their numbered JPGs are also exact duplicate pairs. They form one student reference. Both pages were read in full after derivation from the original; identities and grades are not reproduced. `student-comparison.csv` and per-question paragraphs state what was retained or corrected.

Q2 has a full bar over A(B+C)+DE. Q3 uses p-clocked first two stages and n-clocked last two, distinct from the 2009 register. Q4 has static output inverters and 20 MOS. Q7(a) has eight MOS and an independently verified clock/data separation: in the original native TIFF (1648 by 2338), all 190 pixels are white in rectangle x455..464/y1690..1708. A second reader confirmed this gap. Q7(b) has 12 MOS, a NAND3 core and six rail-gated OFF devices. The preserved source supplies the original contact geometry; reconstruction normalizes spacing while retaining net connectivity.

Q8(b)'s Figure 6(c) reference and caption are typos: the two actual right-panel latches are labelled (b), with clear opposite mux port numbers and noninverting buffers. Q4 duty, Q5 contamination delay and Q6 device thresholds remain explicitly unprovided; the answers give the resulting conditional or symbolic expressions.
