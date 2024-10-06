from fastapi import FastAPI, File, UploadFile, HTTPException
import os

app = FastAPI()

@app.get("/")
async def read_root():
  return {"message": "Hello, FastAPI!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), destination: str = "uploaded_file"):
  try:
    # Open a stream to save the uploaded file
    with open(destination, 'wb') as f:
      # Define the buffer size (in bytes)
      buffer_size = 10 * 1024 * 1024  # 10 MB
      # Read the file in chunks and write to the file on disk
      while content := await file.read(buffer_size):
        f.write(content)
    return {"message": f"File uploaded successfully to {destination}"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
