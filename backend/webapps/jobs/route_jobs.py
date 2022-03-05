from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request):
    # print(dir(request))
    return templates.TemplateResponse(
        name="jobs/homepage.html", 
        context={'request':request})


