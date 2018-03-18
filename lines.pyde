'''use space bar to change arrow orientations
   explanation in
   http://illusionoftheyear.com/2017/10/dynamic-muller-lyer-illusion/'''

left_arrow = []
center_arrow = []
right_arrow = []
selection = 1


def setup():
    size(600, 400)
    left_arrow.append([-150, 0, -120, 30])
    left_arrow.append([-150, 0, -120, -30])
    center_arrow.append([0, 0, -30, 30])
    center_arrow.append([0, 0, -30, -30])
    right_arrow.append([150, 0, 180, 30])
    right_arrow.append([150, 0, 180, -30])


def draw():
    global left_arrow, center_arrow, right_arrow
    
    translate(width/2, height/2)
    background(255, 255, 255)
    line(-150, 0, 150, 0)
    line(*left_arrow[0])
    line(*left_arrow[1])
    line(*center_arrow[0])
    line(*center_arrow[1])
    line(*right_arrow[0])
    line(*right_arrow[1])


def keyPressed():
    global left_arrow, center_arrow, right_arrow, selection
    
    if key == " ":
        left_arrow[0][2] -= 60*selection
        left_arrow[1][2] -= 60*selection
        center_arrow[0][2] += 60*selection
        center_arrow[1][2] += 60*selection
        right_arrow[0][2] -= 60*selection
        right_arrow[1][2] -= 60*selection
        selection = -selection
        