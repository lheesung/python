class Human:
    def __init__(self, height, age):
        self.height = height  # 멤버변수
        self.age = age

    def age(self):  # 메소드
        print(self.age, "살입니다")

    def tall(self):
        print(self.height, "cm 입니다")


# 인스턴스 생성
man = Human(170, 17)
girl = Human(170, 17)

print(man.height)
print(girl.age)
