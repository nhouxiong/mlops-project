# tests/test_smoke.py
"""
Smoke tests for Milestone 0 environment validation.

These tests verify that the development environment is correctly
configured with all required dependencies.
"""

import pytest


class TestCoreImports:
    """Verify core packages are importable."""
    
    def test_numpy(self):
        import numpy
        assert numpy.__version__
    
    def test_pandas(self):
        import pandas
        assert pandas.__version__
    
    def test_sklearn(self):
        import sklearn
        assert sklearn.__version__
    
    def test_pytest(self):
        import pytest
        assert pytest.__version__


class TestBasicFunctionality:
    """Verify packages work beyond just importing."""
    
    def test_numpy_array_operations(self):
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr.sum() == 6
    
    def test_pandas_dataframe_creation(self):
        import pandas as pd
        df = pd.DataFrame({'x': [1, 2, 3]})
        assert len(df) == 3
    
    def test_sklearn_model_fit(self):
        from sklearn.linear_model import LinearRegression
        import numpy as np
        
        X = np.array([[1], [2], [3]])
        y = np.array([1, 2, 3])
        
        model = LinearRegression()
        model.fit(X, y)
        
        prediction = model.predict([[4]])
        assert prediction[0] == pytest.approx(4.0, rel=0.1)


class TestProjectStructure:
    """Verify project structure is correct."""
    
    def test_src_is_package(self):
        """Verify src directory is a Python package."""
        from pathlib import Path
        assert Path("src/__init__.py").exists()
    
    def test_requirements_exists(self):
        """Verify requirements.txt exists."""
        from pathlib import Path
        assert Path("requirements.txt").exists()

"""Smoke tests to verify environment and basic functionality."""
"""CI WORKFLOW TEST"""

def test_imports():
    """Verify core packages are importable."""
    import pandas
    import numpy
    import sklearn
    assert True

def test_data_loading():
    """Verify sample data can be loaded."""
    import pandas as pd
    # Replace with your actual data path
    # df = pd.read_csv("data/sample.csv")
    # assert len(df) > 0
    assert True  # Placeholder

def test_model_instantiation():
    """Verify model class can be instantiated."""
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=10)
    assert model is not None