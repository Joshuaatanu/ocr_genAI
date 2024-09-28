# OCR Package

This Python package allows you to perform OCR on images using Tesseract and interpret the results using generative AI models like OpenAI's GPT and Google's Gemini.

## Installation

To install the package, use:

pip install ocr_genAI

## Usage

```python

from ocr_genai import perform_ocr, interpret_with_openai, interpret_with_gemini,interpret_with_claude



# Replace with your actual image path and API keys
image_path = "image.jpg"  # Ensure this image exists in your directory
openai_api_key = "YOUR_OPENAI_API_KEY"
gemini_api_key = "YOUR_GEMINI_API_KEY"
claude_api_key = "YOUR_CLAUDE_API_KEY"

# Perform OCR
ocr_output = perform_ocr(image_path)
if ocr_output:
    print("OCR Output:\n", ocr_output)

    # Interpret with OpenAI
    openai_response = interpret_with_openai(ocr_output, openai_api_key)
    if openai_response:
        print("OpenAI Response:\n", openai_response)

    # Interpret with Gemini
    gemini_response = interpret_with_gemini(ocr_output, gemini_api_key)
    if gemini_response:
        print("Gemini Response:\n", gemini_response)
    #interpret with Claude
    claude_response = interpret_with_claude(ocr_output, claude_api_key)
        if claude_response:
            print("Claude Response:\n", claude_response)

