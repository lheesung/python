try :
    print("나누기 전용 계산기 입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))

    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력했습니다!")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 나머지 에러
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)