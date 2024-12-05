import os
import json

# Define the project structure
structure = {
    'epigenetic-analysis-tools': {
        'data': ['raw', 'processed'],
        'docs': [],
        'src': {
            'qc': [],
            'alignment': [],
            'assembly': [],
            'hic_analysis': [],
            'diff_expression': []
        },
        'notebooks': ['utils'],
        'results': ['fastqc', 'trimmomatic', 'hisat2', 'stringtie', 'hic-pro', 'juicer', 'deseq2'],
        'config': [],
        'tests': [],
        'final_pipeline': {'modules': []}
    }
}

# Define notebook templates
notebook_templates = {
    '01_fastqc_analysis.ipynb': """# FastQC Analysis

## 1. Quality Metrics Understanding
- Per-base sequence quality interpretation
- Quality score distributions
- Sequence length distributions

## 2. Content Analysis
- GC content patterns
- Overrepresented sequences
- Adapter content

## 3. Comparative Analysis
- High vs. low quality examples
- Pattern recognition in problematic data

## 4. Decision Making
- Quality thresholds
- When to reject vs. trim data""",

    '02_trimmomatic_analysis.ipynb': """# Trimmomatic Analysis

## 1. Understanding Trimming Operations
- Sliding window mechanics
- Adapter trimming specifics
- Quality thresholds

## 2. Parameter Impact Analysis
- Data loss vs. quality improvement
- Read length distribution changes
- Quality score improvements

## 3. Optimization Strategies
- Parameter selection based on input quality
- Balancing data retention vs. quality""",

    '03_hisat2_analysis.ipynb': """# HISAT2 Analysis

## 1. Genome Indexing Deep Dive
- Index structure understanding
- Resource requirements
- Impact on alignment

## 2. Alignment Process Analysis
- Algorithm behavior with different inputs
- RNA-seq vs. DNA-seq differences
- Impact of read quality

## 3. Output Interpretation
- Alignment statistics meaning
- Common failure modes
- Quality metrics""",

    '04_stringtie_analysis.ipynb': """# StringTie Analysis

## 1. Transcript Assembly Mechanics
- Assembly algorithm understanding
- Coverage impact on reconstruction
- Splice junction detection

## 2. Expression Quantification
- Abundance estimation methods
- Coverage normalization
- Isoform-level analysis

## 3. Validation and Quality Control
- Reference comparison metrics
- Assembly confidence scores
- Common artifacts""",

    '05_hicpro_analysis.ipynb': """# HiC-Pro Analysis

## 1. Quality Assessment
- Valid interaction rates
- Library complexity metrics
- Technical biases

## 2. Matrix Generation and Normalization
- Resolution effects
- Normalization methods comparison
- Distance decay patterns

## 3. Interaction Analysis
- Contact probability calculation
- Distance-dependent patterns
- Biological significance""",

    '06_juicer_analysis.ipynb': """# Juicer Analysis

## 1. Map Generation and Interpretation
- Different map types and uses
- Resolution considerations
- Pattern interpretation

## 2. Feature Detection
- A/B compartment calling
- TAD boundary detection
- Loop calling and validation

## 3. Comparative Analysis
- HiC-Pro vs. Juicer results
- Method strengths and limitations
- Integration strategies""",

    '07_deseq2_analysis.ipynb': """# DESeq2 Analysis

## 1. Normalization Understanding
- Size factor calculation
- Count transformations
- Batch effect handling

## 2. Statistical Analysis
- Dispersion estimation
- P-value distributions
- Multiple testing correction

## 3. Results Interpretation
- Log2 fold change meaning
- P-value interpretation
- MA and volcano plot patterns"""
}

def create_notebook(content):
    notebook = {
        "cells": [{"cell_type": "markdown", "metadata": {}, "source": content}],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    return notebook

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        os.makedirs(path, exist_ok=True)
        if isinstance(content, dict):
            create_structure(path, content)
        elif isinstance(content, list):
            for item in content:
                os.makedirs(os.path.join(path, item), exist_ok=True)

# Create project structure
create_structure('.', structure)

# Create notebooks
for filename, content in notebook_templates.items():
    notebook = create_notebook(content)
    with open(f'./notebooks/{filename}', 'w') as f:
        json.dump(notebook, f, indent=1)

# Create README files
readme_content = """# Bioinformatics Project
This project contains scripts, notebooks, and pipelines for bioinformatics analyses."""

with open('./README.md', 'w') as f:
    f.write(readme_content)

notebooks_readme = """# Analysis Notebooks

This directory contains Jupyter notebooks for analyzing and understanding each bioinformatics tool."""

with open('./notebooks/README.md', 'w') as f:
    f.write(notebooks_readme)
