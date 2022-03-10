from unicodedata import name
from urllib import request
from xml.etree.ElementInclude import include
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory='templates')


@router.get('/register/')
def register(request: Request):
    return templates.TemplateResponse(
        name='users/register.html', 
        context={"request":request})
