# Source provenance and independent solution

Original supplied paper: `EE3032(2016期末考考題).pdf`, under `考古/2021/期末考`. Fall 2016 printed footers determine the year. It contains complete Q1–Q8 on printed 3-1 through3-3, 120 points, plus a nearly blank page 4. The original PDF is copied byte-for-byte; hashes are in sources.json. PDF text extraction was empty, so complete native/rendered pages and enlarged circuit/contact crops were read visually.

No matching supplied student answer was found. All answers were derived from the original. A second independent audit checked Q5–Q6 timing and Q4's 24 physical MOS. The significant correction during that audit was that Q4b's third column is driven by the first inverter OUTPUT, not its input a; the output is therefore a·bar(b)·bar(c). The original Q4a final gate/output self-connection was independently confirmed and retained.

Conceptual primary sources inspected:

- [Li, NCU Chapter3](https://www.ee.ncu.edu.tw/jfli/public_html/VLSI/lecture/ch03.pdf), slides 31–36: latchup and guard rings.
- [Li, NCU Chapter6](https://www.ee.ncu.edu.tw/jfli/public_html/VLSI/lecture/ch06.pdf), slides 13–18,29–33: dynamic/domino retention/cascade limitations, fully differential and split-level load topology. DSL controls the pMOS loads from opposite INTERNAL low-swing nodes.
- [Shivakumar et al., DSN 2002](https://users.cs.utah.edu/~rajeev/cs7810/papers/shivakumar02.pdf), *Modeling the effect of technology trends on the soft error rate of combinational logic*: masking and scaling trends. Its conclusions do not justify a universal assertion that electrical masking always vanishes with scaling.

Q1 uses both literal per-node balance and a clearly labelled extra common-time design. Q2 retains the unresolved upper trip; no student noise-peak inference is adopted. Q3 gives a sizing family and one balanced conducting-path solution. Q5 reports both skew directions and the extra positive-skew hold repairs. Q6 is a resistor-divider/writeability approximation, not a simulated transient. No private process model is included.
