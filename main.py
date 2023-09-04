# write your code here
def padel_court_cost(court_type):
    if court_type =="indoor" :
        return 30
    elif court_type == "outdoor":
        return 20

print(padel_court_cost("indoor"))

################################################################

def rackets_cost (racket_brand):
    if racket_brand =="nox":
        return  140 
    elif racket_brand =="siux":
        return 200
    elif racket_brand =="bullpadel":
        return 100 

print(rackets_cost("nox"))

#################################################################

def padel_balls_cost(ball_boxes):
    if ball_boxes== 1:
        return 2
    elif ball_boxes== 2:
        return 3.5
    elif ball_boxes== 3:
        return 5
    

print(padel_balls_cost("box"))

##################################################################

def padel_game_cost():
    the_court_type = input("What is your court type ? ")
    racket_brand = input("What racket brand do you want ? ")
    num_ball_boxes = int(input("How many ball boxes do you want ? "))
    return padel_court_cost(the_court_type) + rackets_cost(racket_brand) + padel_balls_cost(num_ball_boxes)

result = (padel_game_cost())

print(f"The cost of the padel game is {result} KD")










