import pygame
def main():
	pygame.init() # Inicializa Funciones Pygame
	pantalla=pygame.display.set_mode([500,500]) # Tam Ventana y La Define Como Superficie
	pygame.display.set_caption("Donkey Kong") # Nombra La Ventana
	reloj1=pygame.time.Clock() # Definimos Un Reloj
	cerrar=False
	
	
	colorblanco=(0,0,0)
	azul=(0,0,255)
	
	fuente1=pygame.font.SysFont("Arial",34,True,True)# Crear Fuente
	
	
	
	rec=pygame.Rect(100,100,50,50) # Crear Figura Rectangular
	rec2=pygame.Rect(500,500,100,100)
	
	while cerrar!=True: # Loop Principal
		for event in pygame.event.get(): # Recorre Eventos De Pygame Para Que No Se Cierre
			if event.type==pygame.QUIT: # Para Cerrar
			    cerrar=True
			if event.type==pygame.KEYDOWN: # Mover por evento izquierda
				if event.key==pygame.K_DOWN:
					rec.move_ip(0,10)
				if event.key==pygame.K_LEFT:
					rec.move_ip(-10,0) # move ip: mover a lugar
				if event.key==pygame.K_UP:
					rec.move_ip(0,-10)
				if event.key==pygame.K_RIGHT:
					rec.move_ip(10,0)		
					
		reloj1.tick(20) # Limita Loop por Segundo
		pantalla.fill(colorblanco)
		
		#Cronometro
		tiempo=pygame.time.get_ticks()/1000
		tiempo=str(tiempo)#cambia segundos a string
		cronometro=fuente1.render(tiempo,0,(255,255,255))
		pantalla.blit(cronometro,(450,0))
		
		#Rectangulos
		(rec2.left,rec2.top)=pygame.mouse.get_pos() # Objeto seguido por mouse
		rec2.left-=rec2.width/2 # centrado
		rec2.top-=rec2.height/2
		
		pygame.draw.rect(pantalla,azul,rec) #Dibuja los Rectangulos
		pygame.draw.rect(pantalla,azul,rec2)
		
		
		
		pygame.display.flip()# Actualiza La Ventana
		
	pygame.quit()
main()

