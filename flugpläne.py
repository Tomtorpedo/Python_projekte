fluplaene={"DEINEMUDDA":[[6,1,10],[7,2,12]]}
def landung(fluege:str)->list:
    landeplätze=[]
    for flug in fluege:
        zeit,ort,*rest=fluege[flug][-1]
        tupel:tuple=flug,zeit,ort
        landeplätze.append(tupel)
    return(landeplätze)
print(landung(fluplaene))
