from ..services.authentifcation_services import (
    get_user as get_user_service,
    login_user as login_user_service,
    register_user as register_user_service,
)


@app.post("/auth/register")
async def register_user():
    return

@app.post("/auth/login")
async def login_user():
    return

@app.get("/auth/me")
async def get_user():
    return