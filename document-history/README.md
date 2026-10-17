# NCU Introduction to VLSI Design

National Central University, EE3032. Editable LaTeX papers and solutions, transistor diagrams, SPICE programs and numerical verification are organized in two parallel archives.

| Archive | Coverage | Contents |
|---|---|---|
| [Homework archive](homework/README.md) | 31 assignments, 2013–2024 | Complete public question PDFs, written derivations, reports, programs and measured evidence; HW4 stops at pre-layout SPICE. |
| [Exam archive](exams/README.md) | 20 papers, 2007–2024 | Reconstructed papers and independently checked corrected solutions; incomplete source questions are labeled. |

## Original sources and privacy

The [homework archive](homework/README.md#public-assignment-questions) includes complete public question PDFs in the original page format. Only the author first name is removed from the footer; all question text, circuit figures, marks, dates and pagination are preserved. Instructor references use surname Li only.

Unedited source masters, original exam scans, photograph panels and supplied instructor attachments remain in the [owner-only private original archive](https://github.com/handsomegary/ncu-intro-vlsi-originals). Public exam readers can use the reconstructed papers and corrected solutions here.

[PRIVATE_SOURCES.json](PRIVATE_SOURCES.json) records neutral private archive paths and original-byte hashes. The previous repository history is retained inside the private archive; this public repository starts with the cleaned collection.

## Verification

```sh
python verify_package.py
```

The checker verifies public artifact hashes, coverage, links, mathematical checks and saved simulation evidence. It does not launch HSPICE. Original-byte verification runs only when `VLSI_PRIVATE_ORIGINALS` points to the owner's private checkout; otherwise it is explicitly reported as not run. Each assignment provides its own reproduction instructions. The CIC018 process model is not redistributed.

[MANIFEST.json](MANIFEST.json) records SHA256 hashes, with text line endings normalized to LF and binary files unchanged.
