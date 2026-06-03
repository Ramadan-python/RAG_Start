from fastapi import APIRouter,FASTAPI
base_router = APIRouter()

@base_router.get("/")
def welcome():
    return ("message: Welcome to the mini-RAG system!")
    