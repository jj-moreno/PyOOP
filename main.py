import matplotlib.pyplot as pylab
from Trial import Trial


if __name__ == '__main__':
    time_in_secs = 5
    trial = Trial(time_in_secs)
    trial.performtrial()
    trial.printresult()
    pylab.plot(trial.distances)
    pylab.title('Random Walk')
    pylab.xlabel('Time')
    pylab.ylabel('Distance From Origin')
    pylab.show()
