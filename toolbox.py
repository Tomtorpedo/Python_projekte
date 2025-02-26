if __name__=="__main__":
    print("test")

def timer(funktion,*input)->int:
    """Stoppt die Zeit einer Funktion"""
    import time
    start=time.perf_counter_ns()
    funktion(*input)
    stop=time.perf_counter_ns()
    return(stop-start)

def list_gen(len:int)->list:
    """Generiert unsortierte liste mit [len] Einträgen"""
    import random
    list=[]
    for i in range(len):
        zahl=random.randint(0,999)
        list.append(zahl)
    return list