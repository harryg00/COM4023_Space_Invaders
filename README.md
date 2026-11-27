> **Authors:** Jacob Levy | Oscar Pocock | Harry Goswell

# COM4023_Space_Invaders

Space Invaders codebase in Python and Pygame for `COM4023-PR1`.

## Setup and Testing

Install the game and test dependencies with:

```sh
python -m pip install -r requirements.txt
```

Run the game and unit tests with:

```sh
python main.py
python -m pytest -v tests
```

The test suite also runs in GitHub Actions on pushes and pull requests.

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
  should animate between two poses, move from side to side, fire at the player
  at random, and increase their movement speed as their numbers are reduced.
- **Defender (Player):** The player must be able to shoot multiple bullets
  continuously. Collision detection should destroy invaders when hit by the
  player, and cause the player to lose a life and respawn (until out of lives)
  when hit by an invader.
- **Barriers:** The four green barriers must progressively diminish every time
  they are shot by either the invaders or the player.

---

## Objects & Methods

### `Barrier`

- `__init__()`
- `get_cell_rect()`
- `draw()`
- `update()`
- `destroy_radius()`
- `check_collision()`

### `Bullet`

- `__init__()`
- `has_defender_bullet()` — [**Class Method**](#class-method)
- `play_shoot_sound()`
- `updateAll()` — [**Class Method**](#class-method)

### `Defender`

- `__init__()`
- `update()`
- `move()`
- `shoot()`

### `Invader`

- `__init__()`
- `current_speed()` — [**Class Method**](#class-method)
- `update_all()` — [**Class Method**](#class-method)
- `_update_animation()` — [**Private Method**](#private-method)
- `_handle_edge()` — [**Private Method**](#private-method)
- `_update_invaders()` — [**Private Method**](#private-method)

---

## Definitions

### Class Method

A class method is a method bound to the class itself rather than any specific
object instance.

### Private Method

A leading underscore marks a method as an internal method. Python does not
enforce private access, so these methods can still be accessed from outside the
class.
