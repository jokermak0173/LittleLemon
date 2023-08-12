### Please Test this endpoints 

(Create User POST)
http://127.0.0.1:8000/auth/users/
username: {USERNAME}
password: {PASSWORD}

(Generate Token POST)
http://127.0.0.1:8000/auth/token/login/  
username: admindjango2
password: employee123


GET Bookings
http://127.0.0.1:8000/restaurant/booking/tables/
Token: 6d018bfd712adc0926541ebaf7f65f4df6c4c655

GET Menus
http://127.0.0.1:8000/api/menu/
Token: 6d018bfd712adc0926541ebaf7f65f4df6c4c655