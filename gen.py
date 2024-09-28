from ocr_package import perform_ocr, interpret_with_openai, interpret_with_gemini, interpret_with_claude

ocr_output = perform_ocr("image_path.jpg")
openai_response = interpret_with_openai(ocr_output, "your_openai_api_key")
gemini_response = interpret_with_gemini(ocr_output, "your_gemini_api_key")
claude_response = interpret_with_claude(ocr_output, "your_claude_api_key")