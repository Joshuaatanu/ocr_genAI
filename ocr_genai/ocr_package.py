# -*- coding: utf-8 -*-
"""ocr_package.py

This module provides functions for performing OCR and interpreting the output using
generative AI models (OpenAI and Gemini).
"""

import pytesseract
from PIL import Image
import re
from openai import OpenAI
import google.generativeai as genai
import anthropic

def perform_ocr(image_path):
    """Performs OCR on an image and cleans the output.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: A string containing the cleaned OCR output.
    """
    try:
        # Perform OCR using Tesseract
        data = pytesseract.image_to_string(Image.open(image_path))
        
        # Clean the OCR output
        cleaned_data = re.sub(r'\s*\n', ' ', data)  # Replace newlines with spaces
        cleaned_data = re.sub(r'[^\w\s,.]', '', cleaned_data)  # Remove non-word characters
        cleaned_data = re.sub(r'\b\w{1,3}\b(?=\s)', '', cleaned_data)  # Remove short words
        cleaned_data = re.sub(r'\s{2,}', ' ', cleaned_data)  # Replace multiple spaces with a single space
        
        return cleaned_data.strip()  # Return the cleaned output
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None

def interpret_with_openai(ocr_output, openai_api_key):
    """Interprets OCR output using OpenAI's GPT model.

    Args:
        ocr_output (str): The OCR output to interpret.
        openai_api_key (str): Your OpenAI API key.

    Returns:
        str: The OpenAI model's response.
    """
    try:
        client = OpenAI(api_key=openai_api_key)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant interpreting OCR output."},
                {"role": "user", "content": ocr_output}
            ]
        )
        return completion.choices[0].message.content  # Return the generated text from the response
    except Exception as e:
        print(f"Error during OpenAI interpretation: {e}")
        return None

def interpret_with_gemini(ocr_output, gemini_api_key):
    """Interprets OCR output using Google Gemini.

    Args:
        ocr_output (str): The OCR output to interpret.
        gemini_api_key (str): Your Gemini API key.

    Returns:
        str: The Gemini model's response.
    """
    try:
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("You are a helpful assistant interpreting OCR output: " + ocr_output)
        return response.text  # Return the text from the response
    except Exception as e:
        print(f"Error during Gemini interpretation: {e}")
        return None
    
def interpret_with_claude(ocr_output,claude_api_key):
    try:
        client = anthropic.Anthropic(
            api_key = claude_api_key
        )
        message  = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens= 512,
        messages =[
            {"role":"user", "content":"you are a helpful assistant, your job is  to interprete the data recieved from the ocr engine" + ocr_output}
        ]
        )
        return message.content
    except Exception as e:
         print(f"Error during Gemini interpretation: {e}")
         return None


if __name__ == "__main__":
    # Example usage
    image_path = "Testproc1.jpg"
    ocr_output = perform_ocr(image_path)
    
    if ocr_output:
        # Replace with your actual API keys
        openai_api_key = "YOUR_OPENAI_API_KEY"
        gemini_api_key = "YOUR_GEMINI_API_KEY"
        claude_api_key = "YOUR_GEMINI_API_KEY"

        openai_response = interpret_with_openai(ocr_output, openai_api_key)
        if openai_response:
            print("OpenAI Response:\n", openai_response)

        gemini_response = interpret_with_gemini(ocr_output, gemini_api_key)
        if gemini_response:
            print("Gemini Response:\n", gemini_response)
        
        claude_response = interpret_with_claude(ocr_output, claude_api_key)
        if claude_response:
            print("Claude Response:\n", claude_response)

