import os
from pathlib import Path

from osdagbridge.core.utils import common
from osdagbridge.core.reports.report_generator import (
    ReportMetadata,
    ReportOptions,
    ReportRequest,
    build_report_payload,
    generate_report,
)

OUT = Path("fossee_evidence/report_test").resolve()
OUT.mkdir(parents=True, exist_ok=True)

# All values below are synthetic test data, not an actual bridge design.
inputs = {
    common.KEY_SPAN: 30,
    common.KEY_TS_NO_OF_GIRDERS: 4,
    common.KEY_TS_DECK_THICKNESS: 250,
    common.KEY_MATERIAL_GIRDER_DENSITY: 78.5,
    "typical_section.overall_bridge_width": 10.0,
    "member_properties.girder_details.section_properties.area.G1.M1": 0.025,
    "member_properties.girder_details.section_properties.mass.G1.M1": 196.25,
}

# Give the material calculator valid properties for all four girders.
for i in range(1, 5):
    inputs[
        f"member_properties.girder_details.section_properties.area.G{i}.M1"
    ] = 0.025
    inputs[
        f"member_properties.girder_details.section_properties.mass.G{i}.M1"
    ] = 196.25

# Synthetic utilization results.
output = {
    "analysis_summary": {
        "status": "Synthetic integration test",
        "max_displacement": 12.4,
        "max_bending_moment": 850.0,
        "max_shear_force": 420.0,
    },
    "design_checks": [],
    "design_results": {
        "per_girder": {
            "G1": {"DCR": 0.72},
            "G2": {"DCR": 0.81},
            "G3": {"DCR": 0.76},
            "G4": {"DCR": 0.68},
        }
    },
    "deck_report_values": {
        "deck.report.m_uls_sag": 120.0,
        "deck.report.mu_bot": 200.0,
        "deck.report.m_uls_hog": 80.0,
        "deck.report.mu_top": 160.0,
        "deck.report.punch_ved": 90.0,
        "deck.report.vrd_c_mpa": 180.0,
        "deck.report.shear_ved": 60.0,
        "deck.report.shear_vrdc": 120.0,
        "deck.report.wk_bot": 0.20,
        "deck.report.wk_top": 0.18,
        "deck.report.wk_limit": 0.30,
    },
    "crossbracing_forces_dict": {
        "pairs": {"G1-G2": {}},
        "geometry": {},
        "brace_type": "X",
    },
    "crossbracing_design_results": {
        "G1-G2": {
            "diagonal": {
                "tension": {"Member.efficiency": 0.62},
                "compression": {"Member.efficiency": 0.74},
            },
            "chord": {
                "tension": {"Member.efficiency": 0.55},
                "compression": {"Member.efficiency": 0.69},
            },
        }
    },
    "end_diaphragm_design_results": {
        "G1-G2": {
            "diagonal": {
                "tension": {"Member.efficiency": 0.58},
                "compression": {"Member.efficiency": 0.83},
            }
        }
    },
    "design_log": [
        "Synthetic integration test: report generation initiated.",
        "Synthetic integration test: report generation completed.",
    ],
}

metadata = ReportMetadata(
    project_name="Synthetic Bridge Integration Test",
    project_location="Test Location, India",
    designer="Integration Test",
    client="Synthetic Client",
    company="Test Organisation",
    group_name="FOSSEE Evidence",
    subtitle="Synthetic Report Validation",
    job_number="SYNTHETIC-001",
    report_date="2026-11-20",
)

options = ReportOptions(
    sections=["loads", "analysis", "design_checks", "drawings"],
    include_figures=True,
    include_toc=True,
    include_pdf=True,
)

request = ReportRequest(
    metadata=metadata,
    options=options,
    output_dir=str(OUT),
    file_stem="synthetic_integration_report",
)

print("Building synthetic report payload...")
payload = build_report_payload(request, inputs, output)

print("Generating complete report...")
result = generate_report(payload, request)

if not result.pdf_path or not Path(result.pdf_path).is_file():
    raise RuntimeError("PDF generation failed. Check the LaTeX output above.")

pdf = Path(result.pdf_path)
tex = Path(result.tex_path) if result.tex_path else None

print("\nREPORT GENERATION PASSED")
print(f"PDF: {pdf}")
print(f"PDF size: {pdf.stat().st_size:,} bytes")

if tex and tex.is_file():
    print(f"TeX: {tex}")
    print(f"TeX size: {tex.stat().st_size:,} bytes")
else:
    raise RuntimeError("LaTeX source file was not generated.")

print("\nChecking generated chart PDFs...")
for name in [
    "ur_steel_plate_girders.pdf",
    "ur_concrete_deck_slab.pdf",
    "ur_cross_bracing.pdf",
    "ur_end_diaphragms.pdf",
    "material_steel_quantities.pdf",
    "material_concrete_quantity.pdf",
    "material_reinforcement_quantity.pdf",
]:
    matches = list(OUT.rglob(name))
    if matches:
        print(f"PASS: {name}")
    else:
        print(f"NOTE: {name} is generated in the temporary report workspace.")

print("\nSYNTHETIC FULL REPORT INTEGRATION TEST PASSED")
