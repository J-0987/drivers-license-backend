#temporary debugging
import sys
print(sys.path)


from fastapi import Depends
from sqlmodel import Session, select
from app.models import LicenseApplication
from app.schema import CreateApplication, LicenseApplicationList

def create_application(db: Session, license_data: CreateApplication):
    db_license = LicenseApplication(**license_data.model_dump())
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license


def get_driver_licenses(db: Session, skip: int = 0, limit: int = 100):
    statement = select(LicenseApplication).offset(skip).limit(limit)
    return db.exec(statement).all()

def delete_application(db: Session, license_id: int):
    statement = select(LicenseApplication). where(LicenseApplicationList.id == license_id)
    db_license = db.exec(statement).first()
    db.delete(db_license)
    db.commit()