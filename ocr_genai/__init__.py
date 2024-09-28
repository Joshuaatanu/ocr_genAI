# __init__.py

"""ocr_genai package.

This package provides functions for performing OCR and interpreting the output 
using OpenAI and Gemini models.
"""

from .ocr_package import perform_ocr, interpret_with_openai, interpret_with_gemini, interpret_with_claude


__all__ = [
    "perform_ocr",
    "interpret_with_openai",
    "interpret_with_gemini",
    "interpret_with_claude"

]
