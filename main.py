from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import List
import json
from pprint import pprint
from gen_embeddings import chain

app = FastAPI()

# CORS

origins = [
    "*",
    "https://google.com",
    "https://www.google.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error Handling


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print("Validation Error??")
    pprint(exc.errors())

    return JSONResponse(
        status_code=400,
        content={"message": "Validation Error", "details": exc.errors()},
    )


# Models


class FormList(BaseModel):
    forms: List[str]
    prompt: str


# Routes


@app.post("/forms")
async def fillout_forms(form_list: FormList):
    return JSONResponse(
        status_code=200,
        content=json.dumps(
            [
                chain.invoke(f"""
{form}
--- What the user wants ---
{form_list.prompt}
---
""")
                for form in form_list.forms
            ]
        ),
    )
