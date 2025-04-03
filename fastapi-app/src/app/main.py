from fastapi import FastAPI

from app import routers

app = FastAPI(title="Demo App", summary="Demo application with basic CRUD")

app.include_router(routers.books.router)

if __name__ == "__main__":
    pass
