import enum, random
'''
class Kid(enum.Enum):
    Boy = 0
    GIRL = 1 

def random_kid():
    return random.choice([Kid.BOY, Kid.GIRL])

both_girl = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger -- Kid.GIRL:
        both_girls += 1
    if older == Kid.Girl or younger == Kid.GIRL:
        either_girl += 1

print("P(both | older) : ", both_girls / older_girl)
print("P(both | either) : ", both_girls / either_girl)
'''
import math
SQRT_TWO_PI = math.sqrt(2*math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float =1)->float:
    return (math.exp(-(x-mu) **2 / 2 / sigma ** 2) / (SQRT_TWO_PI*sigma))

import matplotlib.pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

def inverse_normal_cdf(p: float,
                        mu: float = 0,
                        sigma: float =1,
                        tolerance: float = 0,00001):

low_z = -10.0
hi_z = 10.0
while hi_z -low_z > tolerance:
    mid_z = (low_z +hi_z) / 2
    mid_p = normal_cdf(mid_z)
    if mid_p<p:
        low_z = mid_z
    else:
        hi_z = mid_z

return mid_z