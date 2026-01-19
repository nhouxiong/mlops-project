# MLOps Project\n\Milestone 0 - Environment & CI Setup

A reproducible Python environment with automated CI validation.

![CI](https://github.com/nhouxiong/mlops-project/actions/workflows/ci.yml/badge.svg)

## Quick Start

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `pytest tests/`

## Reproducibility Principles

This project applies three key reproducibility practices:

1. **Dependency Pinning:** All packages are locked to exact versions in `requirements.txt`, 
   preventing "works on my machine" issues caused by version drift.

2. **Environment Isolation:** Virtual environments separate this project's dependencies 
   from system Python and other projects.

3. **Automated Validation:** GitHub Actions CI runs tests in a fresh environment on every 
   push, catching integration issues before they reach production.

These practices support ML lifecycle reliability by ensuring that training environments 
match deployment environments-a critical requirement when model behavior depends on 
specific library versions.

## Project Structure