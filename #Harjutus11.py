#Harjutus11


#def tervita(m, k="maailm"):
 #    print ("Tere",k,m) 


#def tervita2():
 #    return("Tere kosmos!")


#tervita("Karin","Eegreid")
#print(tervita2())



#Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
#print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
#print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(s):
    s1, s2 = s.split(" ")
   # print(s1[0], s2[0])
    if s1[0]==s2[0]:
        return True
    else:
        return False


print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed('Lahe Känguru'))

