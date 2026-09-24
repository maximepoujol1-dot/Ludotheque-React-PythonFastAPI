from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/auth/register")
def register():
    return 

@router.post("/auth/login")
def login():
    return

@router.get("/auth/me")
def get_current_user():
    return