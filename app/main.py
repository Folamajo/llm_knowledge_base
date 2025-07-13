from fastapi import FastAPI
from schemas.create_user import CreateUser
import uvicorn

app = FastAPI()

class CreateUserResponse():
   status: str


@app.get("/")
def read_root():
   return {"message": "Hello, world"}

@app.post("/register",)
def create_user(user: CreateUser)-> CreateUser:
   # new_user.append(user)
   return user


# if __name__ = "__main__":
#    import uvicorn
#    uvicorn.run(app, host=)