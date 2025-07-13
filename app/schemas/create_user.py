from pydantic import BaseModel, ValidationError

class CreateUser(BaseModel):
   username : str
   email : str
   password : str


# try:
#    sample_data = User(username="Fola", email="fola@gmail.com", hashed_password="hello")
#    print(sample_data)

# except ValidationError as e:
#    print("Validation error:", e )