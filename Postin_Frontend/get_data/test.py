import requests as rq
import reflex as rx

class LoginUser:
  base_url: str = "https://postin-api.onrender.com/"
  token: str


  def login(self, username, password) -> dict:
    login_url = self.base_url + "users/login"
    headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
      "username": username, "password": password
    }

    response = rq.post(login_url, headers=headers, data=data)
    if response.status_code != 200:
      return "could not login"

    self.token = response.text
    return self.token


token = LoginUser().login(username="user", password="1234")
print(token)


      



    