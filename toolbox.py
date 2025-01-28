import time
if __name__=="__main__":
    print("test")

def timer(funktion,input)->int:
    start=time.perf_counter_ns()
    funktion(input)
    stop=time.perf_counter_ns()
    return(stop-start)