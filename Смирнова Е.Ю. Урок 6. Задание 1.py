from time import sleep

class TrafficLight:
    color = ["красный", "желтый", "зеленый"]

    def running(self):
        i = 0
        while i < 3:
            print(f"Свет светофора \n"
                  f"{TrafficLight.color[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(9)
            i +=1


mc = TrafficLight()
mc.running()