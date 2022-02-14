from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job

def create_new_job(job : JobCreate, db : Session, owner_id: int): # the owner id is hardcoded, but in next sessions is fix
    job = Job(**job.dict(), owner_id = owner_id) # pass all items of the request
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def retrieve_job(id:int, db:Session):
    job = db.query(Job).filter(Job.id==id).first()
    return job