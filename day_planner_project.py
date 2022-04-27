import datetime
import json
import os
from random import randint
import sys
from time import sleep


os.system('cls')

LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
e = datetime.datetime.now()


def clr():
    _ = os.system('cls')


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def time():
    print("Today is " + e.strftime("%a, %b %d, %Y"))
    print("The time is currently " + e.strftime("%I:%M:%S %p,"), LOCAL_TIMEZONE, "\n")


file = "planner_files.json"


month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


program_files = {'Shopping List': {'eggs': [12, 'pasture raised only'],
                                   'bread': [1, 'whole wheat or potato'],
                                   'pickles': [2, 'not picky']},
                 'Jokes': {'What did the father buffalo say to his child when he went to college?': 'Bye son.',
                           'How many lawyers does it take to change a lightbulb?': 'Depends. Can you afford any?',
                           "What's more amazing than a talking dog?": 'A spelling bee.',
                           'Did you hear what happened to the dyslexic cultist?': 'He sold his soul to Santa.'},
                 'Appointments': {'Dinner with Lou': [2022, 6, 14],
                                  "Cait's Birthday": [2022, 12, 9],
                                  'DeAnza Ride': [2021, 15, 1]
                                  }
                 }

if not os.path.exists("planner_files.json"):
    with open("planner_files.json", "w") as outfile:
        json.dump(program_files, outfile, indent=4)

schedule_matches = ["sch", "dul", "plan"]
shopping_matches = ["sho", "ping", "list"]
joke_matches = ["tell", "me", "joke"]


def get_planner_json():
    with open("planner_files.json", "r") as planner:
        planner_data = json.load(planner)
    return planner_data


def save_planner_json(planner_data):
    with open("planner_files.json", "w") as planner:
        json.dump(planner_data, planner, indent=4)


def set_appt(appt, data):
    append_data = get_planner_json()
    append_data['Appointments'][appt] = data
    save_planner_json(append_data)


def set_purc(purc, data):
    append_data = get_planner_json()
    append_data['Shopping List'][purc] = data
    save_planner_json(append_data)


def modify_sch(operation):
    appt = input(f"What appointment would you like to {operation}?\n")
    appt_year = int(input("What year is this appointment?\n"))
    appt_month = int(input("What is the numerical month of the appointment?\n"
                           "Example: January is 1, December is 2, etc.\n"))
    appt_day = int(input("What is the day of the appointment?\n"
                         "Example, if your appointment was in January 14th, please enter '14' here.\n"))

    set_appt(appt, [appt_year, appt_month, appt_day])


def modify_sho(operation):
    purc = input(f"What purchase would you like to {operation}?\n")
    purc_num = int(input("How many of this purchase would you like to make?\n"))
    purc_note = input("What notes would you like to add to this purchase?\n"
                      "Example: brands, price limitations, etc.\n")

    set_purc(purc, [purc_num, purc_note])


def append_sch():
    clr()
    appt_reminders()
    modify_sch("add")


def edit_sch():
    clr()
    appt_reminders()
    modify_sch("edit")


def append_sho():
    clr()
    shopping_list()
    modify_sho("add")


def edit_sho():
    clr()
    shopping_list()
    modify_sho("edit")


def random_joke():
    clr()
    with open("planner_files.json") as json_file:
        json_data = json.load(json_file)

    joke_data = json_data["Jokes"]
    random_index = randint(0, len(joke_data)-1)
    joke_key = list(joke_data)[random_index]
    print(joke_key)
    sleep(5)
    print(joke_data[joke_key])
    sleep(5)


def appt_reminders():
    reminder_file = open("planner_files.json", "r")
    reminder_data = json.load(reminder_file)
    reminders = reminder_data["Appointments"]
    print("You have the following appointments:\n")
    for key in reminders:
        app_date = reminders[key]
        year = app_date[0]
        mnth = app_date[1]
        dte = app_date[2]
        print("{} on {} {}, {}.".format(key, month[mnth], dte, year))
    print()
    reminder_file.close()


def shopping_list():
    list_file = open("planner_files.json")
    list_data = json.load(list_file)
    list_items = list_data["Shopping List"]
    print("This is your shopping list so far:")
    for key in list_items:
        purchase = list_items[key]
        quantity = purchase[0]
        notes = purchase[1]
        print("{} X {}; {}".format(key, quantity, notes))
    list_file.close()


def del_sch():
    clr()
    reminder_file = open("planner_files.json")
    reminder_data = json.load(reminder_file)
    reminders = reminder_data["Appointments"]
    appt_reminders()
    print("You have opted to delete one or more appointments.")
    del_option = input("Which would you like to remove?\n"
                       "If you would like to remove them all, please enter \"clear all\"\n")
    if del_option in reminders:
        del reminders[del_option]
    elif del_option == "clear all":
        reminder_data["Appointments"] = {}
    with open("planner_files.json", "w") as file:
        json.dump(reminder_data, file, indent=4)


def del_sho():
    clr()
    list_file = open("planner_files.json")
    list_data = json.load(list_file)
    list_items = list_data["Shopping List"]
    shopping_list()
    print("You have opted to remove something from your shopping list.")
    del_option = input("Which item would you like to remove?\n"
                       "If you would like to remove them all, please enter \"clear all\"\n")
    if del_option in list_items:
        del list_items[del_option]
    elif del_option == "clear all":
        list_data["Shopping List"] = {}
    with open("planner_files.json", "w") as file:
        json.dump(list_data, file, indent=4)


def main_menu():
    clr()
    time()
    while True:
        print("Hello!\nWelcome to your day planner!")
        sleep(2)
        menu_input = input("What would you like to do?\nAccess schedule?\nShopping list?\nHear a joke?\n").lower()
        sch_option = any(x in menu_input for x in schedule_matches)
        sho_option = any(x in menu_input for x in shopping_matches)
        jke_option = any(x in menu_input for x in joke_matches)
        if sch_option and sho_option:
            print("Huh?")
            input("Press Enter to return to the main menu.\n")
        elif sch_option:
            def sch_function():
                clr()
                appt_reminders()
                while True:
                    print("\nThis is your schedule planner.\nWhat would you like to do here?")
                    sch_choice = input("Add something to your schedule?\nChange an appointment?\nRemove something?\n"
                                       "Return to the main menu?\n").lower()
                    if "add" in sch_choice:
                        append_sch()
                        sch_function()
                    elif "change" in sch_choice:
                        edit_sch()
                        sch_function()
                    elif "remove" in sch_choice:
                        del_sch()
                        sch_function()
                    elif "main" or "menu" in sch_choice:
                        main_menu()
            sch_function()
        elif sho_option:
            clr()

            def sho_function():
                clr()
                shopping_list()
                while True:
                    print("You are currently accessing your shopping list.\nWhat would you like to do here?\n")
                    sho_choice = input("Add something to the shopping list?\nEdit your shopping list?\n"
                                       "Remove something?\nReturn to the main menu?\n").lower()
                    if "add" in sho_choice:
                        append_sho()
                        sho_function()
                    elif "edit" in sho_choice:
                        edit_sho()
                        sho_function()
                    elif "remove" in sho_choice:
                        del_sho()
                        sho_function()
                    elif "main" or "menu" in sho_choice:
                        main_menu()
            sho_function()
        elif jke_option:
            random_joke()
            main_menu()
        else:
            main_menu()


main_menu()

# Things to do:
# 1: use the datetime module as a means to replace the "month" dictionary
# 2: use the datetime module to make reliable alarms and reminders
