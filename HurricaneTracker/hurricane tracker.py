#Code by Jack Siegel
#Inspired by Phillip Ventura's 2018 SIGCSE Nifty Assignments submission
#http://nifty.stanford.edu/2018/ventura-hurricane-tracker/nifty-hurricanes.html


import csv
import os
import turtle
import glob


def graphical_setup():
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    atlanticbasin = absolute_path + '/images/atlantic-basin.png'
    map_bg_img = tkinter.PhotoImage(file=atlanticbasin)

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
    
    hurricanegif = absolute_path + '/images/hurricane.gif'
    t = turtle.Turtle()
    wn.register_shape(hurricanegif)
    t.shape(hurricanegif)

    return t, wn, map_bg_img


def track_storm(filename):
    """Animates the path of the storm.
    """
    (t, wn, map_bg_img) = graphical_setup()
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lat = ''
        lon = ''
        wind = ''

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lat = float(row[2])
                lon = float(row[3])
                wind = float(row[4])
                line_count += 1
                print(lat, lon, wind)
                t.goto(lon, lat)
                t.pendown()
                if wind > 157:
                    t.pensize(5)
                    t.color('red')
                    t.write('5')
                elif wind > 129 and wind < 157:
                    t.pensize(4)
                    t.color('orange')
                    t.write('4')
                elif wind > 110 and wind < 129:
                    t.pensize(3)
                    t.color('yellow')
                    t.write('3')
                elif wind > 96 and wind < 111:
                    t.pensize(2)
                    t.color('green')
                    t.write('2')
                elif wind > 74 and wind < 97:
                    t.pensize(1)
                    t.color('blue')
                    t.write('1')
                elif wind < 75:
                    t.pensize(1)
                    t.color('white')
                
    return wn, map_bg_img


def main():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    data = absolute_path + '/data'
    file_list= glob.glob(data + "/*.csv")

    storm = input("Enter a storm: ")
    storm_value = data + '/' + storm.lower() +'.csv'


    wn, map_bg_img = track_storm(storm_value)
    if not (storm_value in file_list):
        print(f'ERROR: "{storm}" is not in list of storms.')
        turtle.Screen().bye()
    wn.exitonclick()


if __name__ == "__main__":
    main()
