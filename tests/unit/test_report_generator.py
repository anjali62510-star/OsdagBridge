import pytest

from osdagbridge.core.reports.report_generator import (
    ReportMetadata,
    ReportOptions,
    ReportRequest,
    build_report_payload,
)


def make_report_request(location):
    metadata = ReportMetadata(
        project_name="Temperature Regression Test",
        project_location=location,
        designer="Test Designer",
        client="Test Client",
        company="Test Company",
    )

    options = ReportOptions(
        sections=[],
        include_figures=False,
        include_toc=False,
        include_pdf=False,
    )

    return ReportRequest(
        metadata=metadata,
        options=options,
        output_dir=".",
        file_stem="temperature_regression_test",
    )


@pytest.mark.parametrize("minimum_temperature", [0, -5])
def test_report_payload_preserves_zero_and_negative_minimum_temperature(
    minimum_temperature,
):
    location = {
        "method": "map",
        "data": {
            "latitude": 23.1815,
            "longitude": 79.9864,
        },
        "weather_data": {
            "max_temp": 46.7,
            "min_temp": minimum_temperature,
            "wind_speed": 39,
            "zone": "III",
            "z_value": 0.16,
        },
    }

    payload = build_report_payload(
        make_report_request(location),
        input_dict={},
        output_dict={},
    )

    assert payload.inputs["shade_temp_max"] == 46.7
    assert payload.inputs["shade_temp_min"] == minimum_temperature


def test_report_payload_does_not_overwrite_existing_temperature_inputs():
    location = {
        "method": "map",
        "data": {},
        "weather_data": {
            "max_temp": 46.7,
            "min_temp": 0,
        },
    }

    payload = build_report_payload(
        make_report_request(location),
        input_dict={
            "shade_temp_max": 42.0,
            "shade_temp_min": -2.0,
        },
        output_dict={},
    )

    assert payload.inputs["shade_temp_max"] == 42.0
    assert payload.inputs["shade_temp_min"] == -2.0
