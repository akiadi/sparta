# 불러오기
import sys
import pygame
from pygame.locals import *
 
# 게임 색상 정의하기
# 더 많은 색상을 추가했습니다.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (148, 0, 211)
 
# 게임 시작은 이곳에서
# 파이게임 초기화하기
pygame.init()
 
# 프레임 매니저 초기화하기
clock = pygame.time.Clock()
# 프레임 레이트 설정하기
clock.tick(60)
 
# 제목 표시줄 설정하기
pygame.display.set_caption("Crazy Driver")
 
# 게임 화면 초기화하기
screen = pygame.display.set_mode((1000, 600))    # 창 크기는 이곳에서 변경합니다.
 
# 배경 색상 설정하기
screen.fill(VIOLET) # 선택한 색은 이곳에 지정합니다.
 
# 화면 업데이트하기
pygame.display.update()
 
# 메인 게임 루프
while True:
    # 이벤트 확인하기
    for event in pygame.event.get():
        # 플레이어가 게임을 그만두는지?
        if event.type == QUIT:
            # 게임 끝내기
            pygame.quit()
            sys.exit()
 
    # 화면 업데이트하기
    pygame.display.update()