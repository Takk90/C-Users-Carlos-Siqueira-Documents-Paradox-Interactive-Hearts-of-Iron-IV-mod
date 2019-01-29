#!/usr/bin/env python3
import os, sys, fnmatch, re
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(creds)

startTime = time.time()

__version__ = 1.0

def get_tags(rootDir):
    tags = []
    pos =0
    with open(rootDir, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.readlines()
        for line in content:
            if not line.startswith("#") or line.startswith(""):  # If the line doesn't start with a comment or blank
                hasTag = re.match(r'^[A-Z]{3}', line, re.M | re.I)  # If it's a tag
                if hasTag:
                    tags.append(hasTag.group())
                    pos +=1
    #input()
    return tags

def get_sheet_tags (sheet):
    sheet_tags = []

    for y, x in enumerate(sheet[0]):
        if x != "":
            sheet_tags.append(x)

    return sheet_tags

def createPartNameLoc (rootDir, sheet):
    content = ""
    filepath = rootDir + "/localisation/MD_subideology_names.yml"
    content = "l_english:\n"
    for a, b in enumerate(sheet[0]):
        if b != "" or a != 0:
            for c in range(0,36):

                if c not in [0,1,2,3,9,17,31,37]:
                    if c > 36:
                        break
                    d = sheet[c][a]
                    #print(d)
                    #input()
                    #western
                    if not d.isspace():
                        if c == 4 and d != "":
                            content += " " + b +"."+"conservatism:0 \"£generic_conservatism_small "+d +"\"\n"
                            content += " " + b +"."+"conservatism_desc:0 \"" +"\"\n"
                        elif c == 5 and d != "":
                            content += " " + b +"."+"liberalism:0 \"£generic_liberalism_small "+d +"\"\n"
                            content += " " + b +"."+"liberalism_desc:0 \""+"\"\n"
                        elif c == 6 and d != "":
                            content += " " + b +"."+"socialism:0 \"£generic_socialism_small "+d +"\"\n"
                            content += " " + b +"."+"socialism_desc:0 \""+"\"\n"
                        elif c == 7 and d != "":
                            content += " " + b +"."+"Western_Autocracy:0 \"£generic_Western_Autocracy_small "+d +"\"\n"
                            content += " " + b +"."+"Western_Autocracy_desc:0 \"" +"\"\n"

                        #Emerging
                        elif c == 10 and d != "":
                            content += " " + b +"."+"Communist-State:0 \"£generic_Communist_State_small "+d +"\"\n"
                            content += " " + b +"."+"Communist-State_desc:0 \"" +"\"\n"
                        elif c == 11 and d != "":
                            content += " " + b +"."+"Conservative:0 \"£generic_Conservative_small "+d +"\"\n"
                            content += " " + b +"."+"Conservative_desc:0 \"" +"\"\n"
                        elif c == 12 and d != "":
                            content += " " + b +"."+"Autocracy:0 \"£generic_Autocracy_small "+d +"\"\n"
                            content += " " + b +"."+"Autocracy_desc:0 \"" +"\"\n"
                        elif c == 13 and d != "":
                            content += " " + b +"."+"Vilayat_e_Faqih:0 \"£generic_Vilayat_e_Faqih_small "+d +"\"\n"
                            content += " " + b +"."+"Vilayat_e_Faqih_desc:0 \"" +"\"\n"
                        elif c == 14 and d != "":
                            content += " " + b +"."+"Mod_Vilayat_e_Faqih:0 \"£generic_Mod_Vilayat_e_Faqih_small "+d +"\"\n"
                            content += " " + b +"."+"Mod_Vilayat_e_Faqih_desc:0 \"" +"\"\n"
                        elif c == 15 and d != "":
                            content += " " + b +"."+"anarchist_communism:0 \"£generic_anarchist_communism_small "+d +"\"\n"
                            content += " " + b +"."+"anarchist_communism:0 \"" +"\"\n"

                        #Salafist
                        elif c == 18 and d != "":
                            content += " " + b +"."+"Caliphate:0 \"£generic_Caliphate_small "+d +"\"\n"
                            content += " " + b +"."+"Caliphate_desc:0 \"" +"\"\n"
                        elif c == 19 and d != "":
                            content += " " + b +"."+"Kingdom:0 \"£generic_Kingdom_small "+d +"\"\n"
                            content += " " + b +"."+"Kingdom_desc:0 \"" +"\"\n"

                        #Non-Alligned
                        elif c == 22 and d != "":
                            content += " " + b +"."+"Neutral_conservatism:0 \"£generic_Neutral_conservatism_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_conservatism_desc:0 \"" +"\"\n"
                        elif c == 23 and d != "":
                            content += " " + b +"."+"oligarchism:0 \"£generic_oligarchism_small "+d +"\"\n"
                            content += " " + b +"."+"oligarchism_desc:0 \"" +"\"\n"
                        elif c == 24 and d != "":
                            content += " " + b +"."+"neutral_Social:0 \"£generic_neutral_Social_small "+d +"\"\n"
                            content += " " + b +"."+"neutral_Social_desc:0 \"" +"\"\n"
                        elif c == 25 and d != "":
                            content += " " + b +"."+"Neutral_Libertarian:0 \"£generic_Neutral_Libertarian_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_Libertarian_desc:0 \"" +"\"\n"
                        elif c == 26 and d != "":
                            content += " " + b +"."+"Neutral_Autocracy:0 \"£generic_Neutral_Autocracy_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_Autocracy_desc:0 \"" +"\"\n"
                        elif c == 27 and d != "":
                            content += " " + b +"."+"Neutral_Communism:0 \"£generic_Neutral_Communism_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_Communism_desc:0 \"" +"\"\n"
                        elif c == 28 and d != "":
                            content += " " + b +"."+"Neutral_Muslim_Brotherhood:0 \"£muslim_brotherhood_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_Muslim_Brotherhood_desc:0 \"" +"\"\n"
                        elif c == 29 and d != "":
                            content += " " + b +"."+"Neutral_Green:0 \"£generic_Neutral_Green_small "+d +"\"\n"
                            content += " " + b +"."+"Neutral_Green_desc:0 \"" +"\"\n"

                        #Nationalist
                        elif c == 32 and d != "":
                            content += " " + b +"."+"Nat_Autocracy:0 \"£generic_Nat_Autocracy_small "+d +"\"\n"
                            content += " " + b +"."+"Nat_Autocracy_desc:0 \"" +"\"\n"
                        elif c == 33 and d != "":
                            content += " " + b +"."+"Nat_Fascism:0 \"£generic_Nat_Fascism_small "+d +"\"\n"
                            content += " " + b +"."+"Nat_Fascism_desc:0 \"" +"\"\n"
                        elif c == 34 and d != "":
                            content += " " + b +"."+"Nat_Populism:0 \"£generic_Nat_Populism_small "+d +"\"\n"
                            content += " " + b +"."+"Nat_Populism_desc:0 \"" +"\"\n"
                        elif c == 35 and d != "":
                            content += " " + b +"."+"Monarchist:0 \"£generic_Monarchist_small "+d +"\"\n"
                            content += " " + b +"."+"Monarchist_desc:0 \"" +"\"\n"








                    #input()
    f = open(filepath, "w")
    with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(content)


def createPartyLeaders (rootDir, sheet, filepath):
    content = ""
    content = "l_english:\n"
    for a, b in enumerate(sheet[0]):
        if b != "" or a != 0:
            content += "###" + b + "###\n"
            for c in range(0,31):

                if c not in [1,8,15,18,27]:
                    if c > 36:
                        break
                    d = sheet[c][a]
                    #print(d)
                    #input()
                    #western
                    if not d.isspace():
                        if c == 4 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = conservatism\n"
                            content += "\ttraits = {\n"
                            content += "\t\twestern_conservatism\n"
                            content += "\t}\n"
                            content += "}\n"
                        elif c == 5 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = liberalism\n"
                            content += "\ttraits = {\n"
                            content += "\t\twestern_liberalism\n"
                            content += "\t}\n"
                            content += "}\n"
                        elif c == 6 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = socialism\n"
                            content += "\ttraits = {\n"
                            content += "\t\twestern_socialism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 7 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Western_Autocracy\n"
                            content += "\ttraits = {\n"
                            content += "\t\twestern_Western_Autocracy\n"
                            content += "\t}\n"
                            content += "}\n"

                        #Emerging
                        elif c == 10 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Communist-State\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_Communist-State\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 11 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Conservative\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_Conservative\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 12 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Autocracy\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_Autocracy\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 13 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Vilayat_e_Faqih\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_Vilayat_e_Faqih\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 14 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Mod_Vilayat_e_Faqih\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_Vilayat_e_Faqih_ref\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 15 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = anarchist_communism\n"
                            content += "\ttraits = {\n"
                            content += "\t\temerging_anarchist_communism\n"
                            content += "\t}\n"
                            content += "}\n"

                        #Salafist
                        elif c == 18 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Caliphate\n"
                            content += "\ttraits = {\n"
                            content += "\t\tsalafist_Caliphate\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 19 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Kingdom\n"
                            content += "\ttraits = {\n"
                            content += "\t\tsalafist_Kingdom\n"
                            content += "\t}\n"
                            content += "}\n"


                        #Non-Alligned
                        elif c == 22 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_conservatism\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_conservatism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 23 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = oligarchism\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_oligarchism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 24 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = neutral_Social\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_neutral_Social\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 25 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_Libertarian\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_Libertarian\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 26 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_Autocracy\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_Autocracy\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 27 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_Communism\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_Communism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 28 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_Muslim_Brotherhood\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_Muslim_Brotherhood\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 29 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Neutral_green\n"
                            content += "\ttraits = {\n"
                            content += "\t\tneutrality_Neutral_green\n"
                            content += "\t}\n"
                            content += "}\n"


                        #Nationalist
                        elif c == 32 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Nat_Autocracy\n"
                            content += "\ttraits = {\n"
                            content += "\t\tnationalist_Nat_Autocracy\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 33 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Nat_Fascism\n"
                            content += "\ttraits = {\n"
                            content += "\t\tnationalist_Nat_Fascism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 34 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Nat_Populism\n"
                            content += "\ttraits = {\n"
                            content += "\t\tnationalist_Nat_Populism\n"
                            content += "\t}\n"
                            content += "}\n"

                        elif c == 35 and d != "":
                            content += "create_country_leader = {\n"
                            content += "\tname = \"" + d + "\"\n"
                            content += "\tpicture = \"\"\n"
                            content += "\tideology = Monarchist\n"
                            content += "\ttraits = {\n"
                            content += "\t\tnationalist_Monarchist\n"
                            content += "\t}\n"
                            content += "}\n"








                    #input()
    f = open(filepath, "w")
    with open(filepath, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(content)


def main():
    sheet = gc.open('Politics')
    worksheet = sheet.worksheet('Party Name')
    content = worksheet.get_all_values()

    scriptDir = os.path.realpath(__file__)
    rootDir = os.path.dirname(os.path.dirname(scriptDir))
    tags = get_tags(rootDir + "/common/country_tags/00_countries.txt")
    sheetTags =  get_sheet_tags(content)

    #print(content)
    #input()

    #print(content)
    #input()

    for x in tags:
         if x not in sheetTags:
            print (str(x) + " is a country in game but wasn't found in the politics partyname sheet")

    #input()
    createPartNameLoc(rootDir, content)

    worksheet = sheet.worksheet('Party Leader 2000')
    content = worksheet.get_all_values()
    createPartyLeaders(rootDir, content,(rootDir + "/history/generated_2000_leaders.txt"))

    worksheet = sheet.worksheet('Party Leader 2017')
    content = worksheet.get_all_values()
    createPartyLeaders(rootDir, content,(rootDir + "/history/generated_2017_leaders.txt"))

    #print(len(sheet.row_values(1)))
    #data = sheet.get_all_records()

    print('The script took {0} second!'.format(time.time() - startTime))


if __name__ == "__main__":
    sys.exit(main())