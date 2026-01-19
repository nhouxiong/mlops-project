# MLOps Project - Milestone 0 - Environment & CI Setup

This repository sets up a reproducible Python environment and continuous
integration (CI) workflow to serve as the foundation for a production-ready
machine learning system.

![CI](https://github.com/nhouxiong/mlops-project/actions/workflows/ci.yml/badge.svg)

## Overview

The goal of Milestone 0 is to establish consistent dependency management and
automated validation early in the ML lifecycle. By standardizing the development
environment, this project reduces environment-related issues and supports
reliable transitions from development to production.

## Quick Start

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `pytest tests/`

## Reproducibility Principles

This project applies three key reproducibility practices:

1. **Dependency Pinning / Explicit Dependencies**  
   Project dependency packages are locked to exact versions and listed in
   `requirements.txt`, preventing "works on my machine" issues caused by
   version drift.

2. **Environment Isolation**  
   Virtual environments separate this project's dependencies from system Python
   and other projects.

3. **Automated Validation**  
   GitHub Actions CI runs tests in a fresh environment on every push, catching
   integration issues before they reach production.

Together, these practices help ensure that model development and evaluation are
repeatable and align with production ML engineering principles.

## Documentation: Environment Reproducibility and ML Lifecycle Reliability

Environment reproducibility is a foundational requirement for reliable machine
learning systems because model behavior is often sensitive to specific library
versions and runtime configurations. Without a reproducible environment,
differences between development, testing, and deployment setups can lead to
inconsistent results, unexpected failures, or degraded model performance. By
standardizing the environment early, this project reduces variability across the
ML lifecycle and helps ensure that models behave consistently as they move toward
production.

Several reproducibility principles are applied in this setup. Project
dependencies are explicitly defined in `requirements.txt` to prevent version
drift and "works on my machine" issues. Virtual environments are used to isolate
dependencies from system Python and other projects, ensuring a clean and
predictable runtime. In addition, automated validation through continuous
integration runs tests in a fresh environment on every code change, providing
early detection of integration or dependency issues.

Effective environment management directly supports deployment success by
aligning training and deployment conditions. When development environments
closely mirror deployment environments, the risk of runtime errors,
incompatibilities, and unexpected behavior in production is significantly
reduced. This alignment enables smoother transitions from experimentation to
deployment and supports long-term system maintainability.
