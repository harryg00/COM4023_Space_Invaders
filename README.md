> **Authors:** Jacob Levy | Oscar Pocock | Harry Goswell

# COM4023_Space_Invaders

Space Invaders codebase in Python and Pygame for `COM4023-PR1`.

## Resources

### Assets

- [Sounds](https://classicgaming.cc/classics/space-invaders/sounds)
- [Background images](https://www.magnific.com/free-photo/abstract-geometric-background-shapes-texture_20540507.htm#fromView=keyword&page=1&position=3&uuid=a75c538a-93cc-4faa-a396-fd25d57e8e08&track=ais_hybrid&query=Space+background+textures)

### Examples

- [Free Invaders](https://freeinvaders.org/)
- [Korovatron Space Invaders](https://www.korovatron.co.uk/spaceinvaders/)

### Documentation

- [Pygame Official Docs](https://www.pygame.org/docs/)
- [Pygame Tutorial](https://pygame.readthedocs.io/en/latest/index.html)

---

## Project Requirements

- **Invaders:** The full invaders array must include three types of aliens. They
  should move from side to side, fire at the player at random, and increase
  their movement speed as their numbers are reduced.
- **Defender (Player):** The player must be able to shoot multiple bullets
  continuously. Collision detection should destroy invaders when hit by the
  player, and cause the player to lose a life and respawn (until out of lives)
  when hit by an invader.
- **Barriers:** The four green barriers must progressively diminish every time
  they are shot by either the invaders or the player.

---

## Objects & Methods

### `Barrier`

- `get_cell_rect()`
- `draw()`
- `update()`
- `destroy_radius()`
- `check_collision()`

### `Bullet`

- `updateAll()` — [**Class Method**](#class-method)

### `Defender`

- `update()`
- `move()`
- `shoot()`

### `Invader`

- `updateAll()` — [**Class Method**](#class-method)

---

## Definitions

### Class Method

A class method is a method bound to the class itself rather than any specific
object instance.
