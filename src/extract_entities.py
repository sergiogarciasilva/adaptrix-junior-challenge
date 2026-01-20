#!/usr/bin/env python3
"""
Entity Extraction Pipeline - Junior Challenge

Your task: Complete this script to extract entities from the Gearhead Cycles
weekly operations report using an LLM API.

Deliverables:
1. Extract KPIs (metrics with values)
2. Extract dates and time references
3. Extract organization names
4. Output structured JSON matching the template
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Import helper modules
from helpers.docx_helper import extract_text_from_docx
from helpers.pdf_converter import convert_to_pdf

# TODO: Import your LLM client
# from openai import OpenAI
# or
# from anthropic import Anthropic


def extract_entities(text: str) -> dict:
    """
    Extract entities from document text using an LLM.
    
    Args:
        text: The document text to process
        
    Returns:
        Dictionary with extracted entities
    """
    # TODO: Implement LLM-based entity extraction
    # 
    # Hint: Create a prompt that asks the LLM to identify:
    # 1. KPIs with their values, units, and context
    # 2. Date references and their types
    # 3. Organization names
    #
    # Example prompt structure:
    # "Extract all business KPIs, dates, and organizations from this text..."
    
    entities = {
        "kpis": [],
        "dates": [],
        "organizations": []
    }
    
    return entities


def main():
    """
    Main extraction pipeline.
    """
    # Configuration
    input_file = Path("../input/gearhead_weekly_report.docx")
    output_file = Path("../output/entities.json")
    
    print(f"Processing: {input_file}")
    
    # Step 1: Extract text from DOCX
    # TODO: Use the helper module
    text = ""
    
    # Step 2: Convert to PDF (optional but required for full marks)
    # TODO: Use the PDF converter
    
    # Step 3: Extract entities using LLM
    entities = extract_entities(text)
    
    # Step 4: Build output structure
    output = {
        "document": {
            "filename": input_file.name,
            "extraction_timestamp": datetime.now().isoformat()
        },
        "entities": entities,
        "statistics": {
            "total_entities": (
                len(entities["kpis"]) + 
                len(entities["dates"]) + 
                len(entities["organizations"])
            ),
            "kpi_count": len(entities["kpis"]),
            "date_count": len(entities["dates"]),
            "org_count": len(entities["organizations"])
        }
    }
    
    # Step 5: Save output
    output_file.parent.mkdir(exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"Results saved to: {output_file}")
    print(f"Total entities extracted: {output['statistics']['total_entities']}")


if __name__ == "__main__":
    main()
