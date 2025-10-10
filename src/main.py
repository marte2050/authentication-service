from fastapi import FastAPI
from auth.router import auth_router,auth_group_router, auth_permission_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(auth_group_router)
app.include_router(auth_permission_router)
