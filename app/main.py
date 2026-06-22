from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import shutil

from app.database import SessionLocal, engine, Base
from app.models import Image

Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db = SessionLocal()

    image = Image(
        filename=file.filename,
        filepath=filepath
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    db.close()

    return {
        "id": image.id,
        "filename": image.filename
    }


@app.get("/image/{image_id}")
def get_image(image_id: int):

    db = SessionLocal()

    image = db.query(Image).filter(
        Image.id == image_id
    ).first()

    db.close()

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    return FileResponse(image.filepath)