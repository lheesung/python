from line import line as l
# list 선언 / list 는 []
lst = ['ABC', 'DEF', 'Python', '가나다', 'hello']

lst.append('no no')
print(lst[:])
del (lst[2])
print(lst[:])
# lst[0][1] = 'Z'
# print(lst)
l()
print(" ", end="\n")
lis = ['1', '2', '3', '4', '5', '6', '7', '8']

# lis 의 마지막 원소 삭제
lis.pop()
print(lis)

# lis 의 6번 째 원소 삭제
print(lis[6])

# lis 의 4 지우기
lis.remove('4')
print(lis)

# lis 의 0 번째에 hello 삽입
# lis.insert(lis[0], "10")
# print(lis)

# 5 의 위치 출력
print(lis.index('5'))

# lis 의 index를 뒤집어 출력
lis.reverse()
print(lis)