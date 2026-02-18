# Gemini AI Python Integration

A minimal Python implementation demonstrating integration with the Gemini Pro model using Google's Generative AI SDK.

## Tech Stack

* Python 3.x
* google-genai

## Installation

```bash
pip install google-genai
```

## Usage

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
response = model.generate_content("Explain AI in simple words.")
print(response.text)
```


