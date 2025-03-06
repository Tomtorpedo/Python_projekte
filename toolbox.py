if __name__=="__main__":
    print("test")

def timer(funktion:callable,*input,einheit="µs")->int:
    """Stoppt die Zeit einer Funktion"""
    import time
    start=time.perf_counter_ns()
    funktion(*input)
    stop=time.perf_counter_ns()
    d_time=stop-start
    match einheit:
        case "ns":
            d_time=d_time
        case "µs":
            d_time=d_time/1_000
        case "ms":
            d_time=d_time/1_000_000
        case "s":
            d_time=d_time/1_000_000_000
        case _:
            d_time=d_time/1_000
    
    return(d_time)

def list_gen(len:int)->list:
    """Generiert unsortierte liste mit [len] Einträgen"""
    import random
    list=[]
    for i in range(len):
        zahl=random.randint(0,999)
        list.append(zahl)
    return list

def is_sorted(liste,aufsteigend_sortiert=True)->bool:
    """gibt aus, ob eine liste sortiert ist"""
    match aufsteigend_sortiert:
        case True:
            for i in range(len(liste)-1):
                if liste[i]>liste[i+1]:
                    return False
            return True
        case False:
            for i in range(len(liste)-1):
                if liste[i]<liste[i+1]:
                    return False
            return True