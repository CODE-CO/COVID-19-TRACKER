# @CODE_CO :)
# DATA SOURCE: HTTPS://CORONA.HELP
#-------------------------------------------------LIBRARIES-----------------------------------------------#
import re, os, requests
#------------------------------------------------CLEAR SHELL----------------------------------------------#
os.system("CLS")
#-------------------------------------------------COMMANDS------------------------------------------------#
print("""
|________|@CODE_CO|_________|COMMANDS|________|@CODE_CO|_________|
|GET INFORMATION OF A COUNTRY WITH NAME ('IRAN').                |
|GET LIST OF COUNTRIES WITH ('LIST').                            |
|GET INFORMATION OF A COUNTRY WITH NUMBER OF THAT COUNTRY ('2'). |
|FOR CLEAR THE SHELL JUST ENTER ('CLEAR').                       |
|FOR EXIT OF THIS PROFESSIONAL PROGRAM :) ENTER ('EXIT').        |
|________________________________________________________________|""")
#--------------------------------------------SET SOME VARIABLES-------------------------------------------#
COUNTRY, BOOLEAN = "", False

try:
    print("\nCONNECTING...")
    CORONA_HELP_MAIN_PAGE = requests.get("HTTPS://CORONA.HELP/").text
    print("\nCONNECTED :)")
    COUNTRIES = re.findall(r"corona.help/country/(.*)\"", CORONA_HELP_MAIN_PAGE)
    COUNTRIES = list(map(lambda X : X.upper(), COUNTRIES))
except:
    print("\nERROR: PLEASE CHECK YOUR INTERNET CONNECTION PROGRAM MAY NOT WORK CORECTLY !")
#---------------------------SHOW LIST OF COUNTRIES WITH THE NUMBERS BEHIND THEM---------------------------#
def GET_COUNTRIES():
    COUNTER = 0
    for i in COUNTRIES:
	    print("{0} - {1}".format(COUNTER, i))
	    COUNTER += 1
#------------------------------GET NUMBER OF INFECTED, DEATH AND LAST UPDATE------------------------------#
def GET_INFORMATION():
    global COUNTRY
    if " " in COUNTRY:
        COUNTRY = COUNTRY.replace(" ", "-")
        BOOLEAN = True
    elif "-" in COUNTRY:
        BOOLEAN = True
    else:
        BOOLEAN = False
    CORONA_HELP_COUNTRY = requests.get("HTTPS://CORONA.HELP/country/%s/" % COUNTRY).text
    INFORMATION = re.findall(r"bold-700.*?>(.*)?<", CORONA_HELP_COUNTRY)
    LAST_UPDATE = re.findall(r".+ago", CORONA_HELP_COUNTRY)
    if BOOLEAN:
        print("\n{0}: (|TOTAL|) INFECTED: {1} | DEATHS: {2} | RECOVERD: {3} | (|TODAY|) INFECTED: {4} | DEATHS: {5}, RECOVERD: {6} | LAST UPDATE: {7}.".format(COUNTRY.upper().replace("-", " "), INFORMATION[0], INFORMATION[2], INFORMATION[4], INFORMATION[1], INFORMATION[3], INFORMATION[5],LAST_UPDATE[0].upper().strip()))
    else:
        print("\n{0}: (|TOTAL|) INFECTED: {1} | DEATHS: {2} | RECOVERD: {3} | (|TODAY|) INFECTED: {4} | DEATHS: {5}, RECOVERD: {6} | LAST UPDATE: {7}.".format(COUNTRY.upper(), INFORMATION[0], INFORMATION[2], INFORMATION[4], INFORMATION[1], INFORMATION[3], INFORMATION[5], LAST_UPDATE[0].upper().strip()))
#------------------------------LOOP TO GET NAME|NUMBER OF COUNTRIES FOR SHOW------------------------------#
while COUNTRY != "EXIT":
    COUNTRY = input("\nINPUT: ").upper()
    if COUNTRY == "CLEAR":
        os.system("CLS")
        continue
    if COUNTRY.isdigit():
        try:
            COUNTRY = COUNTRIES[int(COUNTRY)]
        except:
            print("NUMBER OUT OF RANGE !")
            continue
    if COUNTRY == "LIST":
        GET_COUNTRIES()
        COUNTER = 0
    else:
        try:
            GET_INFORMATION()
        except:
            if COUNTRY != "EXIT":
                if COUNTRY not in COUNTRIES:
                    print("WRONG INPUT !")
                else:
                    print("PLEASE CHECK YOUR INTERNET CONNECTION !")
#--------------------------------------------------BYE :)-------------------------------------------------#
print("BYE :)")
