from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get('/login/')
def login(request : Request):
    return templates.TemplateResponse(
        "auth/login.html", 
        {"request": request}
    )


