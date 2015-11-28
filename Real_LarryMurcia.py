import pygame
class Player(pygame.sprite.Sprite):
	def __init__(self,imagen):# Funcion Que Recibe Imagen
		pygame.sprite.Sprite.__init__(self)
		self.imagen=imagen
		self.rect=self.imagen.get_rect()# Determina Los Limites de la imagen
		self.rect.left,self.rect.top=2,450 # Determina las posiciones en las que aparecera el sprite


	
	def colisiones(self,velx,vely):# Funcion Que Determina Colisiones
		#limites
		lim1=pygame.Rect(0,0,1,500)
		lim2=pygame.Rect(500,0,1,500)
		limabajo=pygame.Rect(0,500,500,1)
		
		
		#Posiciones Sprites
		oldx=self.rect.left# Guardar Anterior x
		oldy=self.rect.top# Guardar Anteriores y
		self.rect.move_ip(velx,vely)
		
		if self.rect.colliderect(lim1):
			self.rect.left=oldx
			
		if self.rect.colliderect(lim2):
			self.rect.left=oldx
		if self.rect.colliderect(limabajo):
			self.rect.top=oldy
			
			
	def update(self,superficie,velx,vely):# Funcion Actualizar
		self.colisiones(velx,vely)
		superficie.blit(self.imagen,self.rect)
		
		
	
def main():
	import pygame
	pygame.init() # Inicializa Funciones Pygame
	pantalla=pygame.display.set_mode([500,500]) # Tam Ventana y La Define Como Superficie
	pygame.display.set_caption("Donkey Kong") # Nombra La Ventana
	reloj1=pygame.time.Clock() # Definimos Un Reloj
	cerrar=False
	
	
	#Cargar Imagen Personaje
	kong=pygame.image.load("1.png").convert_alpha()
	jugador1=Player(kong)
	velx,vely=0,0# velocidades s
	vela,vels=5,10# velocidades Verticales
	
	#Colores
	colorblanco=(0,0,0)
	azul=(0,0,255)
	
	#Fuente Para Cronometro
	fuente1=pygame.font.SysFont("Arial",20,True,True)# Crear Fuente
	
	
	
	while cerrar!=True: # Loop Principal
		for event in pygame.event.get(): # Recorre Eventos De Pygame Para Que No Se Cierre
			if event.type==pygame.QUIT: # Para Cerrar
			    cerrar=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					velx=-vela
				if event.key==pygame.K_RIGHT:
					velx=vela       
				if event.key==pygame.K_UP:
					vely=-vels
					
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT:
					velx=0
				if event.key==pygame.K_RIGHT:
					velx=0  
				if event.key==pygame.K_UP:
					vely=0         
						    
		reloj1.tick(20) 
		pantalla.fill(colorblanco)
		
				    
		
			
		#Cronometro
		tiempo=pygame.time.get_ticks()/1000
		tiempo=str(tiempo)#cambia segundos a string
		cronometro=fuente1.render(tiempo,0,(255,255,255))
		pantalla.blit(cronometro,(455,0))

		# Gravedad 
		if vely ==0:
			vely +=2
		if not vely == 0:
			vely +=2	
			
		jugador1.update(pantalla,velx,vely)# Coloca El Sprite En Pantalla	
		pygame.display.flip()# Actualiza La Ventana
		
		
		
	pygame.quit()
main()
