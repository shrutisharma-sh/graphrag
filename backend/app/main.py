from fastapi import FastAPI
from app.routes.llm import router as llm_router
from app.routes.compare import router as compare_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="GraphRAG Benchmark API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(llm_router)
app.include_router(compare_router)