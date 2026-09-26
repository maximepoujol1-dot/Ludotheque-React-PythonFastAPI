from fastapi import Request
from fastapi.responses import JSONResponse

class Error(Exception):
    def __init__(self, message: str, code : int):
        self.message = message
        self.code = code 

async def exception_handler(request : Request, exc: Error):
    return JSONResponse(status_code=exc.code, content = { "erreur": { "code": exc.code, "message": exc.message}})        

