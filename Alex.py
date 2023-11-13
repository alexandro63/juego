# --EJECUCION DEL JUEGO--
# Cargar imagen de fondo
background = pygame.image.load("assets/background.png").convert()
# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)  # Reproducir música en bucle
#GAME OVER
game_over = True
running = True
while running:
    # Pantalla de inicio
    if game_over:
        show_go_screen()
        # Reiniciar el juego
        game_over = False
        all_sprites = pygame.sprite.Group()  # Grupo para todos los sprites
        meteor_list = pygame.sprite.Group()  # Grupo para meteoros
        bullets = pygame.sprite.Group()  # Grupo para balas
        player = Player()  # Crear instancia del jugador
        all_sprites.add(player)  # Agregar jugador al grupo de sprites
        for i in range(8):
            meteor = Meteor()  # Crear instancia de meteoro
            all_sprites.add(meteor)  # Agregar meteoro al grupo de sprites
            meteor_list.add(meteor)  # Agregar meteoro al grupo de meteoros
        score = 0
    clock.tick(60)  # Limitar el juego a 60 fotogramas por segundo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Salir del bucle si se cierra la ventana
        # Disparar al presionar la barra espaciadora
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  # Método para que el jugador dispare
    all_sprites.update()  # Actualizar todos los sprites en el grupo
    # Colisiones - Meteoro - Laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)  # Detectar colisiones
    for hit in hits:
        score += 10  # Incrementar puntaje por cada meteoro destruido
        # Reproducir sonido de explosión
        # explosion_sound.play()
        explosion = Explosion(hit.rect.center)  # Crear instancia de explosión
        all_sprites.add(explosion)  # Agregar explosión al grupo de sprites
        meteor = Meteor()  # Crear nuevo meteoro
        all_sprites.add(meteor)  # Agregar nuevo meteoro al grupo de sprites
        meteor_list.add(meteor)  # Agregar nuevo meteoro al grupo de meteoros
    # Checar colisiones - Jugador - Meteoro
    hits = pygame.sprite.spritecollide(player, meteor_list, True)  # Detectar colisiones
    for hit in hits:
        player.shield -= 25  # Reducir el escudo del jugador por colisión
        meteor = Meteor()  # Crear nuevo meteoro
        all_sprites.add(meteor)  # Agregar nuevo meteoro al grupo de sprites
        meteor_list.add(meteor)  # Agregar nuevo meteoro al grupo de meteoros
        if player.shield <= 0:
            game_over = True  # Establecer game_over en True si el escudo es <= 0
    screen.blit(background, [0, 0])  # Dibujar la imagen de fondo en la pantalla
    all_sprites.draw(screen)  # Dibujar todos los sprites en la pantalla
    # Marcador
    draw_text(screen, str(score), 25, WIDTH // 2, 10)  # Función para dibujar texto
    # Barra de escudo.
    draw_shield_bar(screen, 5, 5, player.shield)  # Función para dibujar la barra de escudo
    pygame.display.flip()  # Actualizar la pantalla
pygame.quit()  # Salir del juego cuando se cierra la ventana
