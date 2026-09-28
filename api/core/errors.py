from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

class Error(Exception):
    def __init__(self, message: str, code : int):
        self.message = message
        self.code = code 

async def exception_handler(request : Request, exc: Error):
    return JSONResponse(status_code=exc.code, content = { "erreur": { "code": exc.code, "message": exc.message}})        

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    message = "; ".join(
        f"{'.'.join(str(part) for part in err['loc'])}: {err['msg']}" for err in exc.errors()
    )
    return JSONResponse(
        status_code=422,
        content={"erreur": {"code": 422, "message": message}},
    )