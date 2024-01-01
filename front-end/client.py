# Let's do a little client side UI
# these are the modules needed

import requests

import flet
from flet import (
AppBar,
ElevatedButton,
Page,
Text,
View,
colors,
Column,
Container,
LinearGradient,
alignment,
border_radius,
padding,
Image,
UserControl,
Row,
IconButton,
margin,
Card,
TextField,
FilledButton,
SnackBar,
)


#We use requests library to send GET/POST requests to our server


def main(page: Page):
   page.title = "Routes Example"
   snack = SnackBar(
         Text("Registration successfull!"),
      )


def GradientGenerator(start, end):
   ColorGradient = LinearGradient(
      begin=alignment.bottom_left,
      end=alignment.top_right,
      colors=[
         start,
         end,
      ],
   )

   return ColorGradient


def req_registter(e, email, password):
   # we set the email and password as a dict/json structure in order to pass it to the request.
   data = {
      "email": email,
      "password": password,
   }

   # here, we call a post request and route our data to server URL and at the same time we
   # pass in our data
   res = requests.post("http://127.0.0.1:5000/register", json=data)

   # now, the request has to be handled by the server....

   # if the status, is ok we say so using a snackbar, otherwise we notify the user something went wrong.

   if res.status_code == 201:
      snack.open = True
      page.update()
   else:
      snack.content.value = "You were not registered! Try again."
      snack.open = True
      page.update()


def req_login(e, email, password):
   data = {
      "email": email,
      "password": password,
   }

res = requests.post("http://127.0.0.1:5000/Login", json=data)

if res.status_code == 201:
   page.views.append(
   View(
      f"/(email)",
      horizontal_alignment="center",
      vertical_alignment="center",
      controls=[
            Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
               Text(
                  "Succssesfuly Logged in!",
                  size=44,
                  weight="w700",
                  text_align="center",
               ),
               Text(
                  f"Login Information:\nEmail: (email)\nPassword: (password)",
                  size=32,
                  weight="w500",
                  text_align="center",
               ),
            ],
            ),
      ],
   )
   ) 
else:
   snack.content.value="Could not log in! Try again."
   snack.open=True
   page.update()
   page.update()

"""Main UI section"""


def route_change(route):
   email=TextField(
      label="Email",
      border="underline",
      width=320,
      text_size=14,
   )

   password=TextField(
      label="Password",
      border="underline",
      width=320,
      text_size=14,
      password=True,
      can_reveal_password=True,
   )

page.views.clear()
# we will be using views for each page, i.e., login page, regis page

# registeration page
page.views.append(
      View(
         "/register",
         horizontal_alignment="center",
         vertical_alignment="center",
         controls=[
            Column(
               alignment="center",
               controls=[
                  Card(
                     elevation=15,
                     content=Container(
                           width=550,
                           height=550,
                           padding=padding.all(30),
                           gradient=GradientGenerator("#1f2937", "#111827"),
                           border_radius=border_radius.all(12),
                           content=Column(
                                 horizontal_alignment="center",
                                 alignment="start",
                                 controls=[
                                    Text(
                                       "Mock REGISTRATION Form With Python API Back-End",
                                       size=32,
                                       weight="w700",
                                       text_align="center",
                                    ),
                                    Text(
                                       "This Flet web-app/registration page is routed to a python(Flask-based) API. Registering sends a request to the API-specific rout and performs several functions.",
                                       size=14,
                                       weight="w700",
                                       text_align="center",
                                       color="#64748b",
                                    ),
                                    Container(padding=padding.only(bottom=20)),
                                    email,
                                    Container(padding=padding.only(bottom=10)),
                                    password,
                                    Container(padding=padding.only(bottom=20)),
                                    Row(
                                       alignment="center",
                                       spacing=20,
                                       controls=[
                                          # the above uI can replicated, here is important part where we pass email and passwords values to register function.
                                          FilledButton(
                                             content=Text(
                                                "Register",
                                                weight="w700",
                                             ),
                                             width=160,
                                             height=40,
                                             # pass the values to register function that sends http request.
                                             on_click = lambda e: req_registter(
                                                   e,
                                                   email.value,
                                                   password.value,
                                             ),
                                          ),
                                          FilledButton(
                                                content-Text(
                                                   "Login",
                                                   weight="w700",
                                                ),
                                                width=160,
                                                height=40,
                                                on_click=lambda: page.go(
                                                   "/login"
                                                ),
                                          ),
                                       snack,
                                    ],
                                 ),
                              ],
                           ),
                        ),
                     )
                  ],
               )
            ],
         )
      )

if page.route == "/login":
     page.views.append(
         View(
            "/Login",
            horizontal_alignment=" center",
            vertical_alignment="center",
            controls=[
                  Column(
                     alignment="center",
                     controls=[
                           Card(
                           elevation=15,
                           content=Container(
                                 width=550,
                                 height=550,
                                 padding=padding-all(30),
                                 gradient=GradientGenerator(
                                    "#2f2937", "#251867"
                                 ),
                                 border_radius=border_radius.all(12),
                                 content=Column(
                                    horizontal_alignment=" center",
                                    alignment="start",
                                    controls=[
                                          Text(
                                             "Mock LOGIN Form With Python API Back-End",
                                             size=32,
                                             weight="w700",
                                             text_align="center",
                                          ),
                                          Text(
                                             "This Flet web-app/registration page is routed a python(Flask-based) API. Registering sends a request to the API-specific rout and performs several functions.",
                                             size=14,
                                             weight="w700",
                                             text_align="center",
                                             color="#64748b",
                                          ),
                                          Container(
                                             padding=padding.only(bottom=20)

                                          ),
                                          email,
                                          Container(
                                             padding=padding.only(bottom=10)
                                          ),
                                          password,
                                          Container(
                                          padding=padding.only(bottom=20)
                                          ),
                                          Row(
                                             alignment="center",
                                             spacing=20,
                                             controls=[
                                                FilledButton(
                                                      content=Text(
                                                         "Login",
                                                         weight="w700",
                                                      ),
                                                      width=160,
                                                      height=40,
                                                      on_click=lambda e: req_login(
                                                         e,
                                                         email.value,
                                                         password.value,
                                                      ),
                                                   ),
                                                FilledButton(
                                                   content=Text(
                                                      "Create acount",
                                                      weight="w700",
                                                   ),
                                                   width=160,
                                                   height=40,
                                                   on_click=lambda: page.go(
                                                      "/register"
                                                   ),
                                                ),
                                                snack,
                                             ],
                                          ),
                                       ],
                                    ),
                                 ),
                              )
                           ],
                        )
                     ],
                  )
               )
page.update()



def view_pop(view):
   page. views.pop()
   top_viewpage.views[-1]
   page.go(top_view.route)
   page.on_route_change =  route_change
   page.on_view_pop = view_pop
   page.go(page.route)


flet.app(target-main, host="localhost", port=9999, view=flet.WEB_BROWSER)
