# import phonenumbers
# from phonenumbers import geocoder,carrier,timezone


# print("x" * 50)

# entered_num = input("Please enter Your  Phone Number :")

# phone_num = phonenumbers.parse(entered_num, None)

# print(phone_num)


# print(geocoder.description_for_number(phone_num, "en"))

# print(carrier.name_for_number(phone_num, "en"))

# print(timezone.time_zones_for_number(phone_num))


####222222

# import turtle

# window = turtle.Screen()
# window.title("Ping Pong Game By SabryHosny")
# window.setup(width=800, height=600)
# window.tracer(0)
# window.bgcolor(.1, .1, .1)

# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape("square")
# ball.color("white")
# ball.shapesize(stretch_len=1, stretch_wid=1)
# ball.goto(x=0, y=0)
# ball.penup()
# ball_dx, ball_dy = 1, 1
# ball_speed = .3


# center_line = turtle.Turtle()
# center_line.speed(0)
# center_line.shape("square")
# center_line.color("white")

# center_line.shapesize(stretch_len=.1, stretch_wid=25)
# center_line.penup()
# center_line.goto(0, 0)

# player1 = turtle.Turtle()
# player1.speed(0)
# player1.shape("square")
# player1.shapesize(stretch_len=1, stretch_wid=5)
# player1.color("blue")
# player1.penup()
# player1.goto(x=-380, y=0)

# player2 = turtle.Turtle()
# player2.speed(0)
# player2.shape("square")
# player2.shapesize(stretch_len=1, stretch_wid=5)
# player2.color("red")
# player2.penup()
# player2.goto(x=380, y=0)


# score = turtle.Turtle()
# score.speed(0)
# score.color("white")
# score.penup()
# score.goto(x=0, y=260)
# score.write("Player1: 0 Player2: 0", align="center",
#              font=("Courier", 14 ,"normal"))
# score.hideturtle()

# players_speeed = 20

# def p1_move_up():
#     player1.sety(player1.ycor() + players_speeed)

# def p1_move_down():
#     player1.sety(player1.ycor() - players_speeed)


# def p2_move_up():
#     player2.sety(player2.ycor() + players_speeed)

# def p2_move_down():
#     player2.sety(player2.ycor() - players_speeed)


# window.listen()
# window.onkeypress(p1_move_up, "w")
# window.onkeypress(p1_move_down, "s")

# window.onkeypress(p2_move_up, "Up")
# window.onkeypress(p2_move_down, "Down")


# while True:
#     window.update()


#     ball.setx(ball.xcor() + (ball_dx * ball_speed))
#     ball.sety(ball.ycor() + (ball_dy * ball_speed))

#     if(ball.ycor() > 290):
#         ball.sety(290)
#         ball_dy *= -1
    

#     if(ball.ycor() < -290):
#         ball.sety(-290)
#         ball_dy *= -1


#     if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and  ball.ycor() < (player1.ycor() +60):
#         ball.setx(-340)
#         ball_dx *= -1


#     if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player2.ycor()-60) and  ball.ycor() < (player2.ycor() +60):
#         ball.setx(-340)
#         ball_dx *= -1


#     if(ball.xcor() > 390):
#         ball.goto(0,0)
#         ball_dx *= -1

#     if(ball.xcor() < -390):
#         ball.goto(0,0)
#         ball_dx *= -1


#####33333


import phonenumbers
from phonenumbers import geocoder ,carrier
import folium
number='+971562072073'


check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,'en')
print(number_location)


service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))



from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode('cd4a52525ca947e98a9a7d3e30c5efb5')

query=str(number_location)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lang=results[0]['geometry']['lng']
print(lat,lang)


map_location=folium.Map(location=[lat,lang],zoom_start=29)
folium.Marker([lat,lang],popup=number_location).add_to(map_location)
map_location.save('mylocation.html')

