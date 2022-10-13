class human:
    def __init__(self, height, age):
        self.height = height    # 멤버변수
        self.age = age

    def age(self):  # 메소드
        print(self.age, "살입니다")

    def tall(self):
        print(self.height, "cm 입니다")

man = human(170, 17) # 인스턴스 생성
girl = human(170, 17) # 인스턴스 생성

print(man.height)

