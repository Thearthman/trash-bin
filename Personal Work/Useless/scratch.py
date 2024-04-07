import matplotlib.pyplot as plt
import numpy as np

begin = np.array([2003,1991,2008,1986,2013,1994,2002])
end =   np.array([2007,2016,2016,2015,2013,1999,2002])
event = ["Event {}".format(i) for i in range(len(begin))]

plt.barh(range(len(begin)),  end-begin, left=begin)

plt.yticks(range(len(begin)), event)
plt.show()