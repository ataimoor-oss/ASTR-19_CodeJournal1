#Session 4
#Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.

class Animal_Cheetah: 
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.furry = furry

    def describe(self):
        print("Animal: Cheetah")
        print(f"Arm length: {self.arm_length} inches")
        print(f"Leg length: {self.leg_length} inches")
        print(f"Number of eyes: {self.num_eyes} eyes")
        print(f"Has tail: {self.has_tail}")
        print(f"It is furry: {self.furry}")

def main():
    my_cheetah = Animal_Cheetah(arm_length =29, leg_length =29, num_eyes =2, has_tail =True, furry =True)
    my_cheetah.describe()

if __name__ == "__main__":
    main()
