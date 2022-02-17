from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.jobs import ShowJob, JobCreate
from db.session import get_db
from db.repository.jobs import create_new_job, retrieve_job, list_jobs, update_job_by_id

router = APIRouter()

@router.post("/create-job/", response_model=ShowJob)
def create_job(job: JobCreate, db:Session=Depends(get_db)):
    owner_id=1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job

@router.get("/get/{id}", response_model=ShowJob)
def retrieve_job_by_id(id:int, db:Session=Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    print(job)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            ,detail= f'Job with id {id} does not exist')
    return job

@router.get("/all/", response_model=List[ShowJob])
def retrieve_all_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs

@router.put("/update/{id}")
def update_job(id:int, job: JobCreate, db:Session = Depends(get_db)):
    owner_id = 1 # in this moment this var is hardcoded but in nexts session we will implement a auth system and we change this
    message = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    if not message: #result of searching and not finding the job is 0
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return {"deatil": f"Successfully update job with id {id}"}
        
