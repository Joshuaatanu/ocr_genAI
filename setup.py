from setuptools import setup, find_packages

setup(
    name="ocr-genai-beta",  # Package name
    version="0.1.4",     # Version number
    author="Joshua Atanu",  # Your name or organization's name
    author_email="atanu.joshua@gmail.com",  # Your email
    description="A package for performing OCR and interpreting the output using OpenAI and Gemini models.",
    long_description=open('README.md').read(),  # Optional: Read from README.md
    long_description_content_type='text/markdown',
    url="https://github.com/Joshuaatanu/ocr_genAI/tree/main",  # Optional: Project URL
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "pytesseract",
        "Pillow",
        "openai",
        "google-generativeai",
        "anthropic"
        
    ],  # External dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
