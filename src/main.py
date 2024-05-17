import uvicorn
from presentation import create_api


api = create_api()


if __name__ == "__main__":
    uvicorn.run("main:api", host="localhost", reload=True)
