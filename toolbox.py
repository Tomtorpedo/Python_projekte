import time
if __name__=="__main__":
    print("test")

def timer(funktion,input1,input2)->int:
    start=time.perf_counter_ns()
    funktion(input1,input2)
    stop=time.perf_counter_ns()
    return(stop-start)