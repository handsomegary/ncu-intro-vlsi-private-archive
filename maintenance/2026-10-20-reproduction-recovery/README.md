# Reviewed local reproduction changes

All 47 uncommitted files from the older homework checkout are preserved byte-for-byte in `source-changes/`, along with its tracked diff. `integration-review.json` records the decision and current public destination for every file. The current public collection keeps the latest exam, prompt and privacy policy; older manifest fields were regenerated rather than restored.

The port adds portable simulator/model preflight, saved-data reproduction, testbench preparation, documentation and CI tests. Tests do not execute HSPICE or read the owner's process model. Existing PDF, TeX, netlist, plot and CSV artifacts were unchanged.

This is a small source-change recovery record, not a copy of simulator scratch data or the full work directory.
