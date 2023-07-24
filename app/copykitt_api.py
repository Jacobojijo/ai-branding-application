from typing import Union
from copykitt import generate_branding_snippet, generate_keyword_snippet
from mangum import Mangum

from fastapi import FastAPI, HTTPException

MAX_INPUT_LENGTH = 32

app = FastAPI()
handler = Mangum(app)

@app.get("/generate_snippet")
def generate_branding_snippet_api(prompt:str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": f"{snippet}"}


@app.get("/generate_keyword")
def generate_branding_keyword_api(prompt:str):
    validate_input_length(prompt)
    keywords = generate_keyword_snippet(prompt)
    return {"keywords": f"{keywords}"}


@app.get("/generate_snippet_and_keyword")
def generate_snippet_keyword_api(prompt:str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keyword_snippet(prompt)
    return {"snippet":snippet,"keywords": keywords}

def validate_input_length(prompt:str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"Input length is too. Must be under {MAX_INPUT_LENGTH} characters."
        )

