
# 거북이, 홍학, 토끼 순으로 도착했어요. 차례로 추가해 보세요
line_up=[]

line_up.append('거북이')
line_up.append('홍학')
line_up.append('토끼')

# 줄을 잘 세웠는지 line_up을 출력해 확인해요
print(line_up)



# 리스트 line_up에 거북이, 홍학, 토끼 순으로 줄을 서 있어요
line_up = ['거북이', '홍학', '토끼']

# 거북이와 홍학 사이에 도도새를 넣어 봐요
line_up.insert(1,'도도새')

# line_up을 출력해 도도새의 위치를 확인해 봐요
print(line_up)



# 리스트 line_up에 거북이, 도도새, 홍학, 토끼 순으로 줄을 서 있어요
line_up = ['거북이', '도도새', '홍학', '토끼']

# 새치기한 도도새를 line_up에서 쫓아내 봐요
line_up.remove('도도새')

# line_up을 출력해 도도새를 잘 쫓아냈는지 확인해 봐요
print(line_up)



# 리스트 line_up에 거북이, 홍학, 토끼 순으로 줄을 서 있어요
line_up = ['거북이', '홍학', '토끼']

# line_up을 사전순으로 정렬해 봐요
line_up.sort()

# 잘 정렬되었는지 출력해 보세요
print(line_up)



# jewel1에 '다이아몬드' 하나를 담아 보세요
bag1 = ['은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '다이아몬드', '은']
jewel1 = bag1[14]

# jewel2에 '금' 9개를 담아 보세요
bag2 = ['은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '금', '금', '금', '금', '금', '금', '금', '금', '금']
jewel2 = bag2[-9:]

# 보석을 잘 골라냈는지 확인해 볼까요?
print('두더지 가방 안의 가장 비싼 보석', jewel1)
print('두더지 가방 안의 금빛 보석들', jewel2)



# 리스트 ['Apple', 'Banana', 'Chamwae', 'Durian']을 담아 주세요
my_list =['Apple', 'Banana', 'Chamwae', 'Durian']

# 'Egg'가 my_list에 들어 있는지 확인하고, 그 결과를 넣어 주세요
my_var='Egg' in my_list
print(my_var)



# 문자열 'Impossible'을 담아 주세요
my_str ='Impossible'

# len을 이용해 my_str의 길이를 넣어 주세요
my_var =len(my_str)


c['o','n']+['c','e']
print(c)
#['o','n','c','e']



# 리스트에 [3, 6, 9]가 담겨 있어요
my_list = [3, 6, 9]

# [3, 6, 9]를 3번 반복한 리스트를 담아 주세요
my_var =my_list*3



# 엘리스 토끼가 강화 무기에 넣고 싶은 내용을 item1, item2, item3에 적었어요
item1 = '완전 좋고'
item2 = '빛나며'
item3 = '손에 착착 감기는'

# item1, item2, item3을 이어 붙여서 무기를 만들어 보세요
weapon =item1+' '+item2+' '+item3+' '+'무기'
#중간에 공백 넣는것을 잊지 말도록

# 만든 무기 weapon을 출력해 확인해요
print(weapon)



# 기차에 승객이 3명 있어요
train = ['성진', '찬경', '준영']

# 서울역: 승객 '주아'를 맨 뒤에 태우세요
train.append('주아')
print('서울역 도착. // ', train)

# 대전역: 1등석 승객 '동빈'을 맨 앞에 태우세요
train.insert(0,'동빈')
print('대전역 도착. // ', train)

# 부산역: 종착역이니 사전순으로 정렬해 주세요
train.sort()
print('부산역 도착. // ', train)
print('오늘도 코딩별 기차를 이용해 주셔서 감사합니다.')





# 도마뱀 빌이 장바구니에 담은 과일 리스트입니다
fruits = ['바나나', '딸기', '두리안', '망고']

# '딸기'가 fruits 안에 들어 있다면 지우고, 없다면 메시지를 출력하세요
if  '딸기'in fruits:
        fruits.remove('딸기')

else:   print('딸기가 없습니다.')