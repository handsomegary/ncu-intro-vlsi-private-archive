# Reproducing a fresh download

The published package includes all 31 delivered assignments, 32 original PDFs,
standalone report sources/PDFs, circuit netlists, input stimuli, analysis scripts
and saved measurements. `COVERAGE.json` explicitly lists unavailable/skipped
assignments. HW4 is limited to the documented pre-layout scope.

## Start without any CAD installation

Python 3.10 or later is sufficient. From the repository root:

```sh
python verify_package.py
python reproduce_saved.py --outdir reproduced/saved
python -m unittest discover -s tests -v
```

The first command checks package hashes, local links and numerical evidence.
The second repeats those checks and generates `summary.json`, an index of all
31 delivered assignments, and per-source delay statistics. It uses only
published data and the Python standard library. It does not launch HSPICE.
Use a fresh/empty output directory; sources are protected from overwrite.

To plot the retained 2024 HW3 waveform:

```sh
python -m pip install -r requirements-plots.txt
python reproduce_saved.py --outdir reproduced/plots --plots
```

Delay statistics retain their original conditions and are not a cross-year
performance ranking. Plotting old measurements is not a new process simulation.

## Configure a new process simulation

You must independently provide a licensed HSPICE installation and an authorized
CIC018 TT process library. They are external prerequisites, deliberately not
redistributed with the public repository. The checks below verify paths and file
availability; they do not start CAD, contact a license service or certify model
compatibility. The subsequent simulation uses the simulator's normal license
configuration.

Every direct simulation driver accepts `--hspice`, `--model` and
`--check-environment`. There are no machine-specific C:/D: fallback locations.
Flags take precedence over `HSPICE`/`CIC018_MODEL`; an HSPICE executable on PATH
can also be found automatically. Model contents are never copied into generated
outputs. Replace the example paths with your own installation:

```sh
python check_environment.py --hspice "/path/to/hspice" --model "/path/to/cic018.l"
python 2024/HW3/simulate.py --hspice "/path/to/hspice" --model "/path/to/cic018.l" --check-environment
```

After the check succeeds, remove `--check-environment` and follow that homework's
README to select its scratch/output directory. Historical paths printed in the
stored SPICE decks and original-run descriptions document the earlier runs;
Python drivers replace model references in their generated runtime decks with
the selected model. Do not execute those static decks without configuring their
model references.

PowerShell environment-variable alternative:

```powershell
$env:HSPICE = 'C:\your-installed-tools\hspice.com'
$env:CIC018_MODEL = 'C:\your-authorized-models\cic018.l'
python .\check_environment.py
python .\2024\HW2\reproduce.py --check-environment
```

The 2024 HW2 driver now also supports `--model` and rewrites only scratch copies
of its model-dependent deck. Its original saved SPICE files remain unchanged.
Simulation wrappers for 2016/2017 HW3 pass the same flags to both child drivers.
The full list is [simulation_entries.json](simulation_entries.json).

These modes remain usable without an installed simulator or process model:

```sh
python 2018/HW2/reproduce.py --analytical-only
python 2019/HW2/reproduce.py --analytical-only
python 2020/HW2/reproduce.py --skip-hspice
python 2023/HW2/reproduce.py --logic-only
python 2013/HW3/reproduce.py --prepare-only
```

Homework regeneration scripts write their outputs into their homework folders.
Run them in a disposable copy if you want to retain the release bytes for hash
verification. Unexecuted decks prepared without a model use the explicit
`CIC018_MODEL_REQUIRED.l` placeholder; supplying a model is necessary before
running those decks.

## Use the original instructor testbench safely

The unchanged archived file is
`2024/assignments/hw3_instructor_testbench.sp`. Its original relative include
expects the circuit in its working directory. Prepare an independently runnable
copy with the included final HW3 circuit and your selected model:

```sh
python prepare_instructor_testbench.py --model "/path/to/cic018.l" --outdir reproduced/instructor
hspice -i reproduced/instructor/instructor_testbench.sp -o reproduced/instructor/run
```

Use your selected HSPICE executable instead of `hspice` if it is not on PATH.
The prepared copy uses absolute include/model paths and works from another
working directory. Only those paths change; the original PWL, vectors, duration
and archived source bytes remain intact.

## Reports and optional packages

Compiled PDFs are already included. Rebuilding the standalone reports requires
pdfLaTeX with standard packages including TikZ/PGFPlots, AMS math, geometry,
booktabs, fontenc/lmodern, listings and hyperref. Their figures and data are
embedded; there are no required private image assets. Plotting Python scripts
use the optional Matplotlib dependency declared above.
