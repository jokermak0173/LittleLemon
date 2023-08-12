### Please Test this endpoints 

(Create User POST)
http://127.0.0.1:8000/auth/users/
username: {USERNAME}
password: {PASSWORD}

(Generate Token POST)
http://127.0.0.1:8000/auth/token/login/  
username: {USERNAME}
password: {PASSWORD}


GET Bookings
http://127.0.0.1:8000/restaurant/booking/tables/
Token: {YourToken}

GET Menus
http://127.0.0.1:8000/api/menu/
Token: {YourToken}
