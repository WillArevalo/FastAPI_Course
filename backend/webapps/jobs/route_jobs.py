from urllib import request, robotparser
from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.jobs import list_jobs, retrieve_job
from sqlalchemy.orm import Session
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        name="jobs/homepage.html", 
        context={'request':request, 'jobs':jobs, 'msg':msg})


@router.get('/detail/{id}')
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    return templates.TemplateResponse(
        name="jobs/detail_job.html", 
        context={'request':request, 'job':job})