import numpy as np
import time
from simple_pid import PID
import matplotlib.pyplot as plt


class DrawingSimulation:
    def __init__(self, perform_length:int, preform_diameter:int, feed_speed:int):
        '''
        Les unités de chacune des variable son les suivante:
        - prefome_length [mm]
        - preform_diameter [mm]
        - feed_speed [mm/s]
        '''
        self.premform_length = perform_length
        self.preform_diameter = preform_diameter
        self.feed_speed = feed_speed
        

    def drawing_diameter(self, speed:int):
        '''
        Les unités de chacune des variable sont les suivante:
        - speed [mm/s]
        '''
        volume_in = self.feed_speed*np.pi*(self.preform_diameter/2)**2
        fiber_diameter =  np.sqrt(volume_in/(speed*np.pi/4)) #retourne le diamètre de la fibre
        return fiber_diameter

    def one_iteration(self, dt:float, fix_diametre:float, fiber_speed:float, Kp:float, Ki:float, Kd:float):
        '''
        Les unités de chacune des variable sont les suivante
        - dt [s]
        - fix_diametre [mm]
        - fiber_speed [mm/s]
        '''
        pid = PID(Kp, Ki, Kd, fix_diametre)
        time.sleep(0.011)
        fiber_speed = fiber_speed -(pid(self.drawing_diameter(fiber_speed))/dt)
        self.premform_length -= dt*self.feed_speed
        return (fiber_speed, self.drawing_diameter(fiber_speed),pid(self.drawing_diameter(fiber_speed)))


    def simulat(self, dt:float, fix_diametre:float, fiber_speed:float, Kp:float, Ki:float, Kd:float, iteration:int):
        '''
        Les unités de chacune des variable sont les suivante
        - dt [s]
        - fix_diametre [mm]
        - fiber_speed [mm/s]
        '''
        ts = []
        t = 0
        fiber_diameter = []
        self.fix_diametre = fix_diametre
        pid = PID(Kp, Ki, Kd, fix_diametre)
        pids = []
        n = 0
        while (self.premform_length > 0 and n < iteration):
            time.sleep(0.011)
            fiber_diameter.append(self.drawing_diameter(fiber_speed))
            pids.append(pid(self.drawing_diameter(fiber_speed)))
            ts.append(t)
            fiber_speed = fiber_speed-(pid(self.drawing_diameter(fiber_speed))/dt)
            self.premform_length -= dt*self.feed_speed
            n += 1
            t += dt
        return [fiber_diameter, pids, ts]

sim = DrawingSimulation(100,20,0.01)
result = sim.simulat(0.05,0.2,10,0.5,0,0,100)


fig, axs = plt.subplots(2)
fig.suptitle('Ajustement du diamètre (PID)')
axs[1].plot(result[-1], result[0], label= f'Diametre {sim.fix_diametre}[mm]')
axs[1].plot([0,result[-1][-1]],[sim.fix_diametre,sim.fix_diametre],'--r')
axs[0].plot(result[-1], result[1])
plt.legend()
plt.show()

# sim2 = DrawingSimulation(100,20,0.1)
# f_ds = []
# f_s = 10
# while sim2.premform_length > 0:
#     f_s, f_d, f_pid = sim2.one_iteration(1,0.1,f_s,10,5,2)
#     f_ds.append(f_d)
#     print(sim2.premform_length, f_s, f_d, f_pid)
# print(f_ds)
