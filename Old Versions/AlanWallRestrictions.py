def levelRestrictions():

    if level_list[0] == 1:
        if keys[pygame.K_a] and player.x > 0 + 4:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 25:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 230:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 300:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 2:
        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
            
    if level_list[0] == 3:
        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
        
    if level_list[0] == 4:
        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
