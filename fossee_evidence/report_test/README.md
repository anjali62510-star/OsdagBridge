# OsdagBridge – Report Integration Test Evidence

## Purpose
This folder contains evidence for the report-layout, utilization-chart,
and material-visualization enhancements implemented in PR #444.

## Test methodology
A reproducible Python script creates synthetic bridge input and output
data, builds a report payload, and runs the OsdagBridge report-generation
pipeline.

All test values are synthetic. They are used to exercise report generation
and chart integration, not to validate an actual bridge design.

## Results
- Full report PDF generated successfully.
- LaTeX source generated successfully.
- 50-page A4 PDF compiled successfully.
- Executive Summary, Project Information, Loads, Analysis Results,
  Design Checks, and Bill of Materials verified in extracted PDF text.
- Four utilization charts verified:
  steel plate girders, concrete deck slab, cross bracing, and end diaphragms.
- Three material charts verified:
  structural steel tonnage, concrete deck volume, and deck reinforcement.
- Three rendered PDF-page previews visually inspected; chart content
  was visible and unclipped.

## Files
- `run_integration_test.py`: reproducible synthetic integration test.
- `integration_test.log`: captured test execution output.
- `synthetic_integration_report.pdf`: generated report.
- `synthetic_integration_report.tex`: generated LaTeX source.
- `report_text.txt`: extracted PDF text used for content verification.
- `charts-utilization-40.png`: utilization chart preview, PDF page 40.
- `charts-utilization-41.png`: utilization chart preview, PDF page 41.
- `charts-material-45.png`: material chart preview, PDF page 45.

## Limitations
This is synthetic integration evidence. It does not establish engineering
validation against real bridge designs, independent code review, or
maintainer approval of the pull request.
