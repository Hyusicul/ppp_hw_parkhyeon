import pygame
import random
import sys

# 초기 설정
pygame.init()
pygame.mixer.init()


upgrade_sound = pygame.mixer.Sound("upgrade_sound.wav")
sell_sound = pygame.mixer.Sound("sell_sound.wav")
break_sound=pygame.mixer.Sound("break_sound.wav")
break_shield_sound=pygame.mixer.Sound("break_shield_sound.wav")
end_sound=pygame.mixer.Sound("end_sound.wav")
buy_shield_sound=pygame.mixer.Sound("buy_shield_sound.wav")
message_timer = None
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("무기 강화 게임")

font = pygame.font.SysFont("malgungothic", 24)
break_font=pygame.font.SysFont("malgungothic", 20)
upgrade_money_font=pygame.font.SysFont("malgungothic", 24)
sell_money_font=pygame.font.SysFont("malgungothic", 24)
break_shield_font=pygame.font.SysFont("malgungothic", 24)
weapon_name_font=pygame.font.SysFont("malgungothic", 28)
weapon_name25_font=pygame.font.SysFont("malgungothic", 60)
shield_price_font=pygame.font.SysFont("malgungothic", 24)
tip_font=pygame.font.SysFont("malgungothic", 14)

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

#모루
moru_1=pygame.image.load("moru_1.png")
moru_2=pygame.image.load("moru_2.png")
# 무기 레벨과 결과 메시지
weapon_level = 0
result = ""
money=50000000
shield=0

# 버튼 정의
upgrade_button = pygame.Rect(420, 630, 250, 200)
sell_button = pygame.Rect(720, 195, 150, 50)
buy_shield_button=pygame.Rect(740, 570, 150, 100)

weapon_images =[]
for i in range(26):  # 레벨 0 ~ 25
    try:
        img = pygame.image.load(f"weapon_{i}.png")
        img = pygame.transform.scale(img, (300, 300))  
        weapon_images.append(img)
    except:
        surface = pygame.Surface((300, 300))
        surface.fill(GRAY)
        weapon_images.append(surface)


weapon_per=[90, 80, 70, 60, 50, 45, 40, 35, 30, 25, 20, 17.5, 15, 12.5, 10, 9, 8, 7, 6, 5, 4.5, 4, 3.5, 3, 2.5]
break_per=[1,2,3,4,5,6,7,8,9,10]
upgrade_money=[1,3,7,15,27,45,66,95,127,177,265,365,500,725,1000,1450,2222,3150,5000,15000,55500,88888,120000,181818,234567]
sell_money=[0,3,24,69,156,291,489,768,1155,1686,4135,5960,12000,32500,68500,125000,250000,525000,750000,1200000,2500000,6500000,15000000,25000000,50000000,0]
weapon_name_list=["나무 막대기   ","나무 검    ","돌 검     ","철 검     ","금 검     ","다이아 검   ","전기 검    ","불 검     ","마스터 검   ","암흑의 검   ","무지개 검   ","찬란한 빛의 검","굳건한 흙의 검","따스한 풀의 검","붉은 화염의 검","강인한 생명의 검","  죽음의 검   ","  메탈 검    ","  용의 검    ","  오로라의 검  ","  별의 검    ","  은하의 검   ","  우주의 검   ","  창조의 검   ","  파괴의 검   ","완!!      태초의 검      성!!"]

# 게임 루프
running = True
while running:
    screen.fill(WHITE)
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buy_shield_button.collidepoint(event.pos) and money>=100000:
                shield+=1
                money-=100000
                buy_shield_sound.play()
            elif buy_shield_button.collidepoint(event.pos) and money<100000 and weapon_level<=24:
                result="돈이 부족합니다!!"

        

            elif upgrade_button.collidepoint(event.pos) and weapon_level<25:
    
                if weapon_level <= 10:
                    chance = random.randint(1, 100)
                else:
                    chance = random.randint(1, 1000)

                
                if weapon_level == 15 and chance > 990 and shield >= 1 and money>=1450:
                    shield -= 1
                    money -= 1450
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 15 and chance > 990 and money>=1450:
                    weapon_level = 0
                    money -= 1450
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 16 and chance > 980 and shield >= 1 and money>=2222:
                    shield -= 1
                    money -= 2222
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 16 and chance > 980 and money>=2222:
                    weapon_level = 0
                    money -= 2222
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

            
                elif weapon_level == 17 and chance > 970 and shield >= 1 and money>=3150:
                    shield -= 1
                    money -= 3150
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 17 and chance > 970 and money>=3150:
                    weapon_level = 0
                    money -= 3150
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 18 and chance > 960 and shield >= 1 and money>=5000:
                    shield -= 1
                    money -= 5000
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 18 and chance > 960 and money>=5000:
                    weapon_level = 0
                    money -= 5000
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 19 and chance > 950 and shield >= 1 and money>=15000:
                    shield -= 1
                    money -= 15000
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 19 and chance > 950 and money>=15000:
                    weapon_level = 0
                    money -= 15000
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 20 and chance > 940 and shield >= 3 and money>=55500:
                    shield -= 3
                    money -= 55500
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 20 and chance > 940 and money>=55500:
                    weapon_level = 0
                    money -= 55500
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 21 and chance > 930 and shield >= 3 and money>=88888:
                    shield -= 3
                    money -= 88888
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 21 and chance > 930 and money>=88888:
                    weapon_level = 0
                    money -= 88888
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 22 and chance > 920 and shield >= 3 and money>=120000:
                    shield -= 3
                    money -= 120000
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 22 and chance > 920 and money>=120000:
                    weapon_level = 0
                    money -= 120000
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 23 and chance > 910 and shield >= 5 and money>=181818:
                    shield -= 5
                    money -= 181818
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 23 and chance > 910 and money>=181818:
                    weapon_level = 0
                    money -= 181818
                    result = "XXX무기 파괴XXX"
                    break_sound.play()

                
                elif weapon_level == 24 and chance > 900 and shield >= 5 and money>=234567:
                    shield -= 5
                    money -= 234567
                    result = "!!!무기파괴 방어!!!"
                    break_shield_sound.play()
                elif weapon_level == 24 and chance > 900 and money>=234567:
                    weapon_level = 0
                    money -= 234567
                    result = "XXX무기 파괴XXX"
                    break_sound.play()




                elif weapon_level==0 and chance <= 90 and money>=1:
                    weapon_level += 1
                    money -= 1
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"  
                elif weapon_level==0 and chance > 90 and money>=1:
                    money -= 1
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==1 and chance <= 80 and money>=3:
                    weapon_level += 1
                    money -= 3
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==1 and chance > 80 and money>=3:
                    money -= 3
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==2 and chance <= 70 and money>=7:
                    weapon_level += 1
                    money -= 7
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==2 and chance > 70 and money>=7:
                    money -= 7
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==3 and chance <= 60 and money>=15:
                    weapon_level += 1
                    money -= 15
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==3 and chance > 60 and money>=15:
                    money -= 15
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==4 and chance <= 50 and money>=27:
                    weapon_level += 1
                    money -= 27
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==4 and chance > 50 and money>=27:
                    money -= 27
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==5 and chance <= 45 and money>=45:
                    weapon_level += 1
                    money -= 45
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==5 and chance > 45 and money>=45:
                    money -= 45
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==6 and chance <= 40 and money>=66:
                    weapon_level += 1
                    money -= 66
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==6 and chance > 40 and money>=66:
                    money -= 66
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==7 and chance <= 35 and money>=95:
                    weapon_level += 1
                    money -= 95
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==7 and chance > 35 and money>=95:
                    money -= 95
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==8 and chance <= 30 and money>=127:
                    weapon_level += 1
                    money -= 127
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==8 and chance > 30 and money>=127:
                    money -= 127
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==9 and chance <= 25 and money>=177:
                    weapon_level += 1
                    money -= 177
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==9 and chance > 25 and money>=177:
                    money -= 177
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==10 and chance <= 20 and money>=265:
                    weapon_level += 1
                    money -= 265
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==10 and chance > 20 and money>=265:
                    money -= 265
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"

                # 이후 단계는 1000으로 바뀜
                elif weapon_level==11 and chance <= 175 and money>=365:
                    weapon_level += 1
                    money -= 365
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==11 and chance > 175 and money>=365:
                    money -= 365
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==12 and chance <= 150 and money>=500:
                    weapon_level += 1
                    money -= 500
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==12 and chance > 150 and money>=500:
                    money -= 500
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==13 and chance <= 125 and money>=725:
                    weapon_level += 1
                    money -= 725
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==13 and chance > 125 and money>=725:
                    money -= 725
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==14 and chance <= 100 and money>=1000:
                    weapon_level += 1
                    money -= 1000
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==14 and chance > 100 and money>=1000:
                    money -= 1000
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==15 and chance <= 90 and money>=1450:
                    weapon_level += 1
                    money -= 1450
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==15 and chance > 90 and money>=1450:
                    money -= 1450
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==16 and chance <= 80 and money>=2222:
                    weapon_level += 1
                    money -= 2222
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==16 and chance > 80 and money>=2222:
                    money -= 2222
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==17 and chance <= 70 and money>=3150:
                    weapon_level += 1
                    money -= 3150
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==17 and chance > 70 and money>=3150:
                    money -= 3150
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==18 and chance <= 60 and money>=5000:
                    weapon_level += 1
                    money -= 5000
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==18 and chance > 60 and money>=5000:
                    money -= 5000
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==19 and chance <= 50 and money>=15000:
                    weapon_level += 1
                    money -= 15000
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==19 and chance > 50 and money>=15000:
                    money -= 15000
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==20 and chance <= 45 and money>=55500:
                    weapon_level += 1
                    money -= 55500
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==20 and chance > 45 and money>=55500:
                    money -= 55500
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==21 and chance <= 40 and money>=88888:
                    weapon_level += 1
                    money -= 88888
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==21 and chance > 40 and money>=88888:
                    money -= 88888
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==22 and chance <= 35 and money>=120000:
                    weapon_level += 1
                    money -= 120000
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==22 and chance > 35 and money>=120000:
                    money -= 120000
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==23 and chance <= 30 and money>=181818:
                    weapon_level += 1
                    money -= 181818
                    upgrade_sound.play()
                    result = f"강화 성공! 현재 +{weapon_level}"
                elif weapon_level==23 and chance > 30 and money>=181818:
                    money -= 181818
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==24 and chance <= 25 and money>=234567:
                    weapon_level += 1
                    money -= 234567
                    upgrade_sound.play()
                    result = " 강화 성공! 최고 레벨!!"
                    end_sound.play()
                elif weapon_level==24 and chance > 25 and money>=234567:
                    money -= 234567
                    upgrade_sound.play()
                    result = f"강화 실패! 현재 +{weapon_level}"
                elif weapon_level==25:
                    result="최고 레벨!!"
                

                            



                else:
                    result = "돈이 부족합니다!"

            #팔기 버튼 누를때의 이벤트
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if sell_button.collidepoint(event.pos):

                    if weapon_level==0:
                        result="0레벨 무기는 판매할 수 없습니다."

                    elif weapon_level == 1:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 3
                        sell_sound.play()
                    elif weapon_level == 2:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 24
                        sell_sound.play()
                    elif weapon_level == 3:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 69
                        sell_sound.play()
                    elif weapon_level == 4:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 156
                        sell_sound.play()
                    elif weapon_level == 5:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 291
                        sell_sound.play()
                    elif weapon_level == 6:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 489
                        sell_sound.play()
                    elif weapon_level == 7:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 768
                        sell_sound.play()
                    elif weapon_level == 8:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 1155
                        sell_sound.play()
                    elif weapon_level == 9:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 1686
                        sell_sound.play()
                    elif weapon_level == 10:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 4135
                        sell_sound.play()
                    elif weapon_level == 11:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 5960
                        sell_sound.play()
                    elif weapon_level == 12:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 12000
                        sell_sound.play()
                    elif weapon_level == 13:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 32500
                        sell_sound.play()
                    elif weapon_level == 14:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 68500
                        sell_sound.play()
                    elif weapon_level == 15:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 125000
                        sell_sound.play()
                    elif weapon_level == 16:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 250000
                        sell_sound.play()
                    elif weapon_level == 17:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 525000
                        sell_sound.play()
                    elif weapon_level == 18:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 750000
                        sell_sound.play()
                    elif weapon_level == 19:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 1200000
                        sell_sound.play()
                    elif weapon_level == 20:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 2500000
                        sell_sound.play()
                    elif weapon_level == 21:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 6500000
                        sell_sound.play()
                    elif weapon_level == 22:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 15000000
                        sell_sound.play()
                    elif weapon_level == 23:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 25000000
                        sell_sound.play()
                    elif weapon_level == 24:
                        result = "무기를 판매했습니다! 레벨 초기화!"
                        weapon_level = 0
                        money += 50000000
                        sell_sound.play()
                    elif weapon_level == 25:
                        result = "검의 가격을 상점 주인이 책정하지 못했습니다."
                        message_timer = pygame.time.get_ticks()
                        

    
            
            

    #무기레벨 메세지
    if weapon_level<=24:
        level_text = font.render(f"무기 레벨: +{weapon_level}   성공 확률: {weapon_per[weapon_level]}%", True, BLACK)
        screen.blit(level_text, (320, 150))
        upgrade_money_text=upgrade_money_font.render(f"강화 비용: {upgrade_money[weapon_level]}",True, BLACK)
        screen.blit(upgrade_money_text, (120, 275))
    if weapon_level>=15 and weapon_level<=24:
        break_text = break_font.render(f"파괴 확률: {break_per[weapon_level-15]}%", True, BLACK)
        screen.blit(break_text, (425, 70))
    if weapon_level<=24:
        weapon_name_text=font.render(f"{weapon_name_list[weapon_level]}", True, BLACK)
        screen.blit(weapon_name_text, (400, 100))
    elif weapon_level==25:
        rainbow_colors = [
        (255, 0, 0),    
        (255, 165, 0),  
        (255, 255, 0),  
        (0, 255, 0),    
        (0, 255, 255),  
        (0, 0, 255),    
        (128, 0, 128),  
        ]

        current_time = pygame.time.get_ticks() // 200  
        color_index = current_time % len(rainbow_colors)
        current_color = rainbow_colors[color_index]
        weapon_name25_text = weapon_name25_font.render(f"{weapon_name_list[weapon_level]}", True, current_color)
        text_rect = weapon_name25_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(weapon_name25_text, text_rect)
    
    #결과 메시지
    result_text = font.render(result, True, GREEN if "성공" in result else RED)
    screen.blit(result_text, (370, 520))

    shield_price_text = font.render("100000", True, BLACK)
    screen.blit(shield_price_text, (770,665))

    #강화버튼
    pygame.draw.rect(screen, WHITE, upgrade_button)
    button_text = font.render("강화하기", True, WHITE)
    screen.blit(button_text, (460, 640))
    
    #쉴드 구매 버튼
    pygame.draw.rect(screen, GRAY, buy_shield_button)
    buy_shield_button_text=font.render("쉴드권 구매", True, BLACK)
    screen.blit(buy_shield_button_text, (750,600))

    #무기 이미지 출력
    weapon_img = weapon_images[weapon_level]
    img_rect = weapon_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(weapon_img, img_rect)

    #돈, 무기판매, 쉴드
    money_text = font.render(f"보유 자금: {money}", True, BLACK)
    screen.blit(money_text, (100, 200))

    sell_money_text= font.render(f"판매 금액: {sell_money[weapon_level]}", True, BLACK)
    screen.blit(sell_money_text, (700,275))
    break_shield_text=font.render(f"쉴드권: {shield}", True, BLACK)
    screen.blit(break_shield_text,(120,320))

    #팔기 버튼
    pygame.draw.rect(screen, GRAY, sell_button)
    sell_text = font.render("팔기", True, BLACK)
    screen.blit(sell_text, (770, 200))
    #모루 이미지 출력
    if weapon_level<=14:
        screen.blit(moru_1, (-20, 200))
    elif weapon_level>=15:
        screen.blit(moru_2, (-20, 200))


    if message_timer is not None:
        sell_current_time = pygame.time.get_ticks()
        if sell_current_time - message_timer >= 3000:
            result = "최고 레벨!!"
            message_timer = None
    tip_font_text=tip_font.render("TIP: 무기파괴는 15성부터 적용. ",True,BLACK)
    screen.blit(tip_font_text, (20,660))
    tip_font_text=tip_font.render("15~19강:쉴드권1장 ",True,BLACK)
    screen.blit(tip_font_text, (50,680))
    tip_font_text=tip_font.render("20~22강:쉴드권3장 ",True,BLACK)
    screen.blit(tip_font_text, (50,700))
    tip_font_text=tip_font.render("23~24강:쉴드권5장",True,BLACK)
    screen.blit(tip_font_text, (50,720))        
    #화면 업데이트
    pygame.display.flip()

pygame.quit()
sys.exit()
