aantal=int(input())

for i in range(1,aantal+1):
    zinTekens=""
    zin=str(input()).lower()
    for teken in zin:
        if teken.isalpha():
            zinTekens=zinTekens+teken
    zinTekens="".join(set(zinTekens))
    if len(zinTekens)==26:
        print("De zin is een pangram.")
    else:
        print("De zin telt "+str(len(zinTekens))+" verschillende letters.")

    
    
