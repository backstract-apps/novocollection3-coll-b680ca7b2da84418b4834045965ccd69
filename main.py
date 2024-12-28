from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novocollection3-coll-b680ca7b2da84418b4834045965ccd69',debug=False,docs_url='/quirky-morse-9bc8fc92c4e711efb0720242ac12000292/docs',openapi_url='/quirky-morse-9bc8fc92c4e711efb0720242ac12000292/openapi.json')

app.include_router(router, prefix='/quirky-morse-9bc8fc92c4e711efb0720242ac12000292/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()