import random
import time

def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class FiniteAutomata:
    def __init__(self):
        self.SLEEP = self.sleep()
        self.STUDY = self.study()
        self.EAT = self.eat()
        self.NIGHTMARE = self.nightmare()
        self.IN_CLASS = self.in_class()

        self.current_state = self.SLEEP

    def send(self, char):
        try:
            self.current_state.send(char)
        except StopIteration:
            print("Something unexpected happened.")

    @prime
    def sleep(self):
        while True:
            hour = yield
            if hour == 4 and random.random()>0.75:
                self.current_state = self.NIGHTMARE
                print("Woke up from terrible nightmare, brr")
            elif hour == 7 and random.random()>0.5:
                print("Woke in time. Going to eat.")
                self.current_state = self.EAT
            elif hour == 9:
                self.current_state = self.IN_CLASS
                print("Oh no, I overslept first lesson. There's still time before the second one.")
            else:
                print("zzz...")

    @prime
    def nightmare(self):
        while True:
            hour = yield
            if hour == 7 and random.random()>0.9:
                print("What an awful night. At least woke up in time. But feel so sleepy...")
                self.current_state = self.EAT
            elif hour == 8 and random.random()>0.75:
                print("What an awful night. Even overslept first lesson. Let's eat.")
                self.current_state = self.EAT
            elif hour == 10:
                print("What an awful night. I overslept everything! Anyway, time to eat.")
                self.current_state = self.EAT
            else:
                print("Trying to sleep...")

    @prime
    def in_class(self):
        while True:
            hour = yield
            if hour == 9:
                print("Trying to not fall asleep during first lesson...")
                self.current_state = self.IN_CLASS
            elif hour == 10:
                print("Trying to not fall asleep during second lesson...")
                self.current_state = self.IN_CLASS
            elif hour == 11:
                print("Finally the end. Anyway, I have to prepare for exams.")
                self.current_state = self.STUDY


    @prime
    def study(self):
        while True:
            hour = yield
            if hour == 14:
                self.current_state = self.EAT
                print("Enough study, time for a break")
            elif hour == 18 and random.random()>0.75:
                self.current_state = self.SLEEP
                print("Feeling so sleeeepy...")
            elif hour == 19:
                self.current_state = self.EAT
                print("Enough study, time for a break")
            elif hour > 21:
                if random.random()>0.8:
                    print("Somehow have some energy to continue studying.")
                    self.current_state = self.STUDY
                else:
                    print("Feeling so sleeeepy...")
                    self.current_state = self.SLEEP
            else:
                print("Studying...")

    @prime
    def eat(self):
        while True:
            hour = yield
            if hour == 8:
                print("No appetite in the morning... Going to the class.")
                self.current_state = self.IN_CLASS
            elif hour == 9:
                self.current_state = self.IN_CLASS
                print("Hot tea warms soul and body. Going to the second lesson.")
            elif hour == 11:
                print("Hot tea warms soul and body. Now, time to study.")
                self.current_state = self.STUDY
            elif hour == 15:
                self.current_state = self.STUDY
                print("Hot soup warms soul and body. Now, it's time to continue studying.")
            elif hour == 20:
                print("Hot tea warms soul and body.")
                if random.random()<0.42:
                    print("Feeling so sleeeepy...")
                    self.current_state = self.SLEEP
                else:
                    print("Somehow have some energy to continue studying.")
                    self.current_state = self.STUDY


if __name__ == "__main__":
    day = FiniteAutomata()
    for i in range(1, 25):
        print(str(i)+":00")
        day.send(i)
        time.sleep(1)
