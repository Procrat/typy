aantal = int(input())
for i in range(0,aantal):
    zin = input()
    aantal = len(set(filter(str.isalnum,zin.lower())))
    if(aantal == 26):
        print("De zin is een pangram.")
    else:
        print("De zin telt %i verschillende letters." %(aantal))