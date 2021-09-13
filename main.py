#!/usr/bin/python

import argparse
import json
import random

class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	CYAN = '\033[96m'
	RESET = '\033[0m'

def grn(text):
	return bcolors.GREEN + str(text) + bcolors.RESET

def ylw(text):
	return bcolors.YELLOW + str(text) + bcolors.RESET

def red(text):
	return bcolors.RED + str(text) + bcolors.RESET

def cyn(text):
	return bcolors.CYAN + str(text) + bcolors.RESET

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "A simple random picker. As usual one of my Sunday Programming challenges (on Tuesday)" ,formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("activities", help="The json file where to pick from. Should be correctly formatted")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    f = open(args.activities,"r")
    activities = json.load(f)

    print("\n\nThese are the possibile activities that you can pick:")
    for category in activities:
        print(category + " (" + str(len(activities[category])) + ")")
        for elem in activities[category]:
            print("\t", elem)

            if (args.verbose):
                time = activities[category][elem]["time"]
                task = activities[category][elem]["task"]

                if task == "lazy":
                    task = grn(task)
                elif task == "engaging":
                    task = ylw(task)
                elif task == "intensive":
                    task = red(task)

                print("\t  ", cyn("time: ") + str(time) + "min","\t",cyn("task: ") + task)

    results = random.sample(list(activities), 2)

    test = 0
    while test != "1" and test != "2":
        print("\n\nI have decided that you should pick among: ")
        print(cyn("\t1)"), results[0])
        print(cyn("\t2)"), results[1])

        test = input()

    if test == "1":
        firstpick = results[0]
        secondpick = results[1]
    else:
        firstpick = results[1]
        secondpick = results[0]
    print(firstpick)

    if random.uniform(0, 1) > 0.2:
        print("\n\nGood! you can go for " + firstpick)
        decision = random.sample(list(activities[firstpick]),1)
        print("\tGet ready for some", grn(decision[0]),"(" + str(activities[firstpick][decision[0]]["time"])  + "min)!")
    else:
        print("\n\nNah! I have decided that it is better to go for " + secondpick)
        decision = random.sample(list(activities[secondpick]),1)
        print("\tGet ready for some", grn(decision[0]),"(" + str(activities[secondpick][decision[0]]["time"])  + "min)!")
