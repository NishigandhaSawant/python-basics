class car():
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

car1 = car()
car2 = car()

car1.start()  # Output: car started
car2.start()  # Output: car started

car1.stop()   # Output: car stopped
car2.stop()   # Output: car stopped