import pgzrun

WIDTH=700
HEIGHT=500
ship=Actor("shippp")
stone=Actor("stone11 (1)")
ship.x=50
ship.bottom=500
player_speed=5
bombs=[]
enemies=[]
stones=[]
enemy_x_speed=1
enemy_y_speed=1
enemies_speed=2
bomb_speed=5
level=1
score=0
game_over=False
missed=False
def draw():
    screen.clear()
    screen.blit("bgoriginal",(0,0))
    ship.draw()
    draw_bomb()
    draw_enemy()
    draw_score()
    if game_over==True:
        draw_last()
        draw_missed_text()
    while missed==True:
        draw_missed_text()
    
def update():
    if not game_over:
      move_player()
      move_bullets()
      ship_border()
      player_collision()
      check_bomb_collision()
      move_enemy()
     
      missed_enemy()
    if game_over==True:
        draw_last()
        draw_missed_text()
def on_key_down(key):
   if not game_over: 
    if key==keys.SPACE:
        create_bomb()
    
def move_player():
    if keyboard.left:
        ship.x-=player_speed
    elif keyboard.right:
        ship.x+=player_speed
    elif keyboard.up:
         ship.y-=player_speed
    elif keyboard.down:
         ship.y+=player_speed
def ship_border():
      if  ship.left > WIDTH :
          ship.right=0
          
     
      if ship.bottom >HEIGHT :
           ship.top=0
      if ship.bottom==0:
          ship.bottom=500
      

    
def create_bomb():
     bomb=Actor("bomb")
     bomb.pos=ship.pos
     bombs.append(bomb)
     
def draw_bomb():
    for bomb in bombs:
        bomb.draw()
        
def move_bullets():
    for bomb in bombs:
        bomb.x+=bomb_speed
        
def create_enemy():
    for i in range(5):
      for j in range(3):
            
             enemy=Actor("enemyship")
             if i//2==0: 
                enemy.x=400+60*i
                enemy.y=100+60*j
             if i//2!=0:
                  enemy.x=400+60*i
                  enemy.y=200+60*j
            
             enemies.append(enemy)



def draw_enemy():
    for enemy in enemies:
        enemy.draw()
def move_enemy():
   
    for enemy in enemies:
        
        enemy.x-=1
         
def check_bomb_collision():
    global level , score
    for bomb in bombs:
        for enemy in enemies:
            if bomb.colliderect(enemy):
                score+=10
                sounds.shoot.play()
                remove_enemy(enemy)
                remove_bomb(bomb)
                if len(enemies)==0:
                    level+=1
                    create_enemy()
                    


def remove_enemy(enemy):
             if enemy in enemies:
                     enemies.remove(enemy)

def remove_bomb(bomb):
    if bomb in bombs:
        bombs.remove(bomb)
        

def player_collision():
    global game_over
    for enemy in enemies:
        if ship.colliderect(enemy):
            ship.image="stonebreak"
            game_over= True
def missed_enemy():
    global missed,game_over
    for enemys in enemies:
        if enemys.x==0:
            missed=True
            game_over=True
            draw_missed_text()
def draw_missed_text():
     
     position = ((WIDTH // 2) , HEIGHT // 2)
     screen.draw.text("*-**INVADER SEIZED YOUR SHIP**-*", (50,135), fontsize=40, color="#e8320e")

def draw_score():
     screen.draw.text("ENEMIE_SHIP_KILLED: "+str(score), (10,10), fontsize=30, color="#e39d12")
     screen.draw.text("LEVEL: "+str(level), (507,21), fontsize=30, color="#e39d12")


def draw_last():
   
    screen.blit("last_pic",(0,0))
    screen.draw.text("opSss! your ship is looted by the theives:(", (10,260), fontsize=50, color="#e2eb38")
    screen.draw.text("* * * * * * * * * * * * ", (299,312), fontsize=50, color="#e2eb38")
    #screen.draw.text(" __ ", (286,353), fontsize=50, color="#e2eb38")
    screen.draw.text("YOUR SCORE: "+str(score), (10,10), fontsize=60, color="#e39d12")
    screen.draw.text("*********TRY AGAIN !!! TO KILL MORE THEIVES ;) *********", (35,445), fontsize=30, color="#fc008b")




missed_enemy()
create_enemy()        
pgzrun.go()
