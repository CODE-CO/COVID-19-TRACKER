# @CODE_CO :) | TELEGRAM: @CODE_CO | GITHUB: CODE-CO |----------------------------------------------
# DATA SOURCE: HTTPS://CORONA.HELP
#---------------------------------------------------------------------------------------------------
try:
    import os, re, requests
    from matplotlib import pyplot as PLT
except:
    print("SOME LIBRARIES NOT FOUND ! | LIBRARIES THAT YOU NEED TO RUN THIS SCRIPT: OS, RE, REQUESTS AND MATPLOTLIB.")
#---------------------------------------------------------------------------------------------------
def CONNECT():
    try:
        global COUNTRIES
        print("\nCONNECTING...")
        COUNTRIES = re.findall(r"CORONA.HELP/COUNTRY/(.*)\"", (requests.get("HTTPS://CORONA.HELP/").text).upper())
        print("\nCONNECTED :)")
    except:
        print("\nERROR: PLEASE CHECK YOUR INTERNET CONNECTION AND RUN THE PROGRAM AGIAN.")
        exit()
#---------------------------------------------------------------------------------------------------
def GET_COUNTRIES():
    LIST = list()
    for index, i in enumerate(COUNTRIES, start = 0):
	    LIST.append("{0} - {1}".format(index, i))
    for i in (reversed(LIST)):
        print(i)
#---------------------------------------------------------------------------------------------------
def GET_INFORMATION():
    if COUNTRY[:4] == "PLOT" and COUNTRY[5:] in COUNTRIES:
        CORONA_HELP_COUNTRY_PAGE = requests.get("HTTPS://CORONA.HELP/country/%s/" % COUNTRY[5:]).text
        INFORMATION_0 = re.findall(r"total.*(\[.*\])", CORONA_HELP_COUNTRY_PAGE)
        INFORMATION_1 = re.findall(r"daily.*(\[.*\])", CORONA_HELP_COUNTRY_PAGE)
        WHICH_PLOT = input("\nWHICH PLOT DO YOU NEED? ENTER (0 OR TOTAL INFECTED | 1 OR TOTAL DEAD | 2 OR TOTAL RECOVERD | 3 OR DAILY INFECTED | 4 OR DAILY DEAD | 5 OR DAILY RECOVERD): ")
        if WHICH_PLOT == "TOTAL INFECTED" or WHICH_PLOT == "0":
            LIST(INFORMATION_0[0])
        elif WHICH_PLOT == "TOTAL DEAD" or WHICH_PLOT == "1":
            LIST(INFORMATION_0[1])
        elif WHICH_PLOT == "TOTAL RECOVERD" or WHICH_PLOT == "2":
            LIST(INFORMATION_0[2])
        elif WHICH_PLOT == "DAILY INFECTED" or WHICH_PLOT == "3":
            LIST(INFORMATION_1[0])
        elif WHICH_PLOT == "DAILY DEAD" or WHICH_PLOT == "4":
            LIST(INFORMATION_1[1])
        elif WHICH_PLOT == "DAILY RECOVERD" or WHICH_PLOT == "5":
            LIST(INFORMATION_1[2])
        else:
            print("\nWRONG INPUT !")
#---------------------------------------------------------------------------------------------------
    else:
        CORONA_HELP_COUNTRY_PAGE = requests.get("HTTPS://CORONA.HELP/country/%s/" % COUNTRY).text
        INFORMATION = re.findall(r"bold-700.*?>(.*)?<", CORONA_HELP_COUNTRY_PAGE)
        LAST_UPDATE = re.findall(r".+ago", CORONA_HELP_COUNTRY_PAGE)
        print("\n{0}: (|TOTAL|) INFECTED: {1} | DEATHS: {2} | RECOVERD: {3} | (|TODAY|) INFECTED: {4} | DEATHS: {5}, RECOVERD: {6} | ACTIVE CASES: {7} | TOTAL TESTS: {8} | LAST UPDATE: {9}.".format(COUNTRY.upper(), INFORMATION[0], INFORMATION[2], INFORMATION[4], INFORMATION[1], INFORMATION[3], INFORMATION[5], INFORMATION[6], INFORMATION[10], LAST_UPDATE[0].upper().strip()))
#---------------------------------------------------------------------------------------------------
def LIST(INFORMATION_0):
    LIST = list(map(lambda X : int(X), (list(dict.fromkeys(INFORMATION_0.strip('][').split(',')[:-1])))))
    PLT.plot(LIST)
    PLT.show()
#---------------------------------------------------------------------------------------------------
def CLEAR():
    os.system("CLS" if os.name == "nt" else "clear")
#---------------------------------------------------------------------------------------------------
def IS_DIGIT():
    global COUNTRY
    try:
        if "PLOT" not in COUNTRY:
            COUNTRY = COUNTRIES[int(COUNTRY)]
        else:
            COUNTRY = "PLOT " + COUNTRIES[int(COUNTRY[5:])]
    except:
        print("\nNUMBER OUT OF RANGE !")
        COUNTRY = "WRONG INPUT !"
#---------------------------------------------------------------------------------------------------
def COMMANDS():
    print("|____________________________|COMMANDS|___________________________|\n|                                                                 |\n|TO GET INFORMATION OF A COUNTRY ENTER NAME 'IRAN' OR NUMBER '11'.|\n|TO GET PLOT OF COUNTRIES ENTER 'PLOT IRAN' OR 'PLOT 11'.         |\n|TO GET TOTAL INFORMATION ENTER 'TOTAL'.                          |\n|TO SEE LIST OF COUNTRIES ENTER 'LIST'.                           |\n|TO SEE THE COMMANDS ENTER 'HELP'.                                |\n|TO CLEAR THE SHELL ENTER 'CLEAR'.                                |\n|TO EXIT OF THIS PROFESSIONAL PROGRAM :) ENTER 'EXIT'.            |\n|_________________________________________________________________|")
#---------------------------------------------------------------------------------------------------
def CHECK():
    if COUNTRY != "WRONG INPUT !" and COUNTRY in COUNTRIES or COUNTRY[:4] == "PLOT" and COUNTRY[5:] in COUNTRIES:
        try:
            GET_INFORMATION()
        except:
            print("\nERROR !")
    else:
        if COUNTRY != "WRONG INPUT !":
            print("\nWRONG INPUT OR COUNTRY !")
#---------------------------------------------------------------------------------------------------
def TOTAL():
    CORONA_HELP_MAIN_PAGE = (requests.get("HTTPS://CORONA.HELP/").text).upper()
    TOTAL = re.findall(r"\<H2 CLASS=\"TEXT-BOLD-700.*?\>(.*?)\<", CORONA_HELP_MAIN_PAGE)
    LAST_UPDATE = re.findall(r".+AGO", CORONA_HELP_MAIN_PAGE)
    print("\nTOTAL CONFIRED CASES: {0} | TOTAL DEATH {1} | CONFIRMED RECOVERIES: {2} | ACTIVE CONFIRMED CASES: {3} | MORTALITY / CLOSED CASES: {4} | TOTAL TESTS: {5} | LAST UPDATE: {6}.".format(TOTAL[0], TOTAL[2], TOTAL[4], TOTAL[6], TOTAL[8], TOTAL[10], LAST_UPDATE[0].strip()))
#---------------------------------------------------------------------------------------------------
CLEAR(), COMMANDS(), CONNECT()
#---------------------------------------------------------------------------------------------------
while True:
    COUNTRY = input("\nINPUT: ").upper().replace(" ", "-")
    if COUNTRY == "TOTAL":
        TOTAL()
        continue
#---------------------------------------------------------------------------------------------------
    if COUNTRY == "CLEAR":
        CLEAR()
        continue
#---------------------------------------------------------------------------------------------------
    if COUNTRY.isdigit() or COUNTRY[5:].isdigit():
        IS_DIGIT()
#---------------------------------------------------------------------------------------------------
    if COUNTRY == "LIST":
        GET_COUNTRIES()
        continue
#---------------------------------------------------------------------------------------------------
    if COUNTRY == "HELP":
        COMMANDS()
        continue
#---------------------------------------------------------------------------------------------------
    if COUNTRY[:4] == "PLOT":
        COUNTRY = "PLOT " + COUNTRY[5:]
#---------------------------------------------------------------------------------------------------
    if COUNTRY == "EXIT":
        print("\nBYE :)\n")
        break
#---------------------------------------------------------------------------------------------------
    CHECK()
