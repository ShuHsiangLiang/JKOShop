from enum import IntEnum, Enum

class BaseOperation:
	pass


class MemberCardType(IntEnum):
    GLOGBAL_MALL = 1
    HI_LIFE = 2
    FAMILY = 3
    SEVEN_ELEVEN = 4
    SIMPLE_MART = 5

card = [1,2,3,4,5]

# print(list(MemberCardType), type(list(MemberCardType)[0]))

for i in card:
	if i in list(MemberCardType):
		print(MemberCardType(i).name)
		print(MemberCardType.GLOGBAL_MALL)

