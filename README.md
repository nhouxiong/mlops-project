# MLOps Project - Milestone 0 - Environment & CI Setup

This repository sets up a reproducilbe Python environment and continuous integreation (CI) workflow to serve as the foundation for a production-ready machine learning system.

![CI](https://github.com/nhouxiong/mlops-project/actions/workflows/ci.yml/badge.svg)

## Overview
The goal of milestone 0 is to establish consistent dependency management and automated validation early in the ML lifecycle. By standardizing the development environment, this project reduces environment-related issues and supports reliable transitions from development to production.

## Quick Start
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `pytest tests/`

## Reproducibility Principles

This project applies three key reproducibility practices:

1. **Dependency Pinning/Explicit Dependencies:** Project dependences packages are locked to exact versions and listed in `requirements.txt`, 
   preventing "works on my machine" issues caused by version drift.

2. **Environment Isolation:** Virtual environments separate this project's dependencies 
   from system Python and other projects.

3. **Automated Validation:** GitHub Actions CI runs tests in a fresh environment on every 
   push, catching integration issues before they reach production.

Together, these practices help ensure the model development and evaluation are repeatable and align with production ML engineering principles.