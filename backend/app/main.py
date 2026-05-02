from fastapi import FastAPI
from app.routes.llm import router as llm_router

app = FastAPI(title="GraphRAG Benchmark API")


app.include_router(llm_router)