import numpy as np


if not hasattr(np, "float_"):
    np.float_ = np.float64
if not hasattr(np, "int_"):
    np.int_ = np.int64
if not hasattr(np, "bool_"):
    np.bool_ = np.bool_
if not hasattr(np, "complex_"):
    np.complex_ = np.complex128