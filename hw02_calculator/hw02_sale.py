regular_price=2000
sale_per=15
sale_price=regular_price-(regular_price*(sale_per/100))
print("정가가 {}인 물건에 {}%의 할인율을 적용하면 최종가격은 {}입니다.".format(regular_price, sale_per, sale_price))
print("할인된 물건 가격은 {:,.0f}원 입니다.".format(sale_price))