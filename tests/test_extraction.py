#!/usr/bin/env python3
"""
Basic validation tests for the entity extraction challenge.

These tests verify that the candidate's output meets the requirements.
"""

import json
import pytest
from pathlib import Path


# Expected output path
OUTPUT_FILE = Path(__file__).parent.parent / "output" / "entities.json"


def load_output() -> dict:
    """Load the candidate's output file."""
    if not OUTPUT_FILE.exists():
        pytest.skip("Output file not found - run extraction first")
    
    with open(OUTPUT_FILE) as f:
        return json.load(f)


class TestOutputStructure:
    """Tests for correct output structure."""
    
    def test_has_document_section(self):
        """Output must have document metadata."""
        output = load_output()
        assert "document" in output
        assert "filename" in output["document"]
        assert "extraction_timestamp" in output["document"]
    
    def test_has_entities_section(self):
        """Output must have entities section."""
        output = load_output()
        assert "entities" in output
        assert "kpis" in output["entities"]
        assert "dates" in output["entities"]
        assert "organizations" in output["entities"]
    
    def test_has_statistics_section(self):
        """Output must have statistics."""
        output = load_output()
        assert "statistics" in output
        assert "total_entities" in output["statistics"]


class TestKPIExtraction:
    """Tests for KPI extraction accuracy."""
    
    def test_extracted_kpis(self):
        """At least 3 KPIs should be extracted."""
        output = load_output()
        kpis = output["entities"]["kpis"]
        assert len(kpis) >= 3, f"Expected at least 3 KPIs, got {len(kpis)}"
    
    def test_kpi_has_required_fields(self):
        """Each KPI must have name, value, unit."""
        output = load_output()
        for kpi in output["entities"]["kpis"]:
            assert "name" in kpi, "KPI missing 'name' field"
            assert "value" in kpi, "KPI missing 'value' field"
            assert "unit" in kpi, "KPI missing 'unit' field"
    
    def test_oee_extracted(self):
        """OEE KPI should be extracted with correct value."""
        output = load_output()
        kpis = output["entities"]["kpis"]
        
        oee_found = False
        for kpi in kpis:
            if "oee" in kpi.get("name", "").lower():
                oee_found = True
                # Value should be around 78.5
                if kpi.get("value"):
                    assert 75 <= float(kpi["value"]) <= 82, \
                        f"OEE value seems incorrect: {kpi['value']}"
        
        assert oee_found, "OEE KPI not found in extraction"
    
    def test_otd_extracted(self):
        """On-Time Delivery KPI should be extracted."""
        output = load_output()
        kpis = output["entities"]["kpis"]
        
        otd_found = any(
            "delivery" in kpi.get("name", "").lower() or 
            "otd" in kpi.get("name", "").lower()
            for kpi in kpis
        )
        
        assert otd_found, "On-Time Delivery KPI not found"


class TestDateExtraction:
    """Tests for date extraction."""
    
    def test_extracted_dates(self):
        """At least 2 date references should be extracted."""
        output = load_output()
        dates = output["entities"]["dates"]
        assert len(dates) >= 2, f"Expected at least 2 dates, got {len(dates)}"
    
    def test_week_reference_found(self):
        """Week 45 reference should be found."""
        output = load_output()
        dates = output["entities"]["dates"]
        
        week_found = any(
            "45" in str(date.get("text", "")) or 
            "week" in str(date.get("text", "")).lower()
            for date in dates
        )
        
        assert week_found, "Week 45 reference not found"


class TestOrganizationExtraction:
    """Tests for organization extraction."""
    
    def test_gearhead_found(self):
        """Gearhead Cycles should be extracted."""
        output = load_output()
        orgs = output["entities"]["organizations"]
        
        gearhead_found = any(
            "gearhead" in org.get("name", "").lower()
            for org in orgs
        )
        
        assert gearhead_found, "Gearhead Cycles not found in organizations"


class TestConfidenceScores:
    """Tests for confidence score implementation."""
    
    def test_kpis_have_confidence(self):
        """KPIs should include confidence scores."""
        output = load_output()
        for kpi in output["entities"]["kpis"]:
            assert "confidence" in kpi, "KPI missing confidence score"
            assert 0 <= kpi["confidence"] <= 1, \
                f"Confidence should be 0-1, got {kpi['confidence']}"
