# CLI Adventure Game (HW) 
### inspired by  (completely ripped from) the Vault of Glass raid in Destiny

# Commit 2

- IO works pretty well
- Moving through room sequences & checking conditions is shaping but still lacks structure
- 

TODO
 - make `set_state` batch a reload to any state object / side effect
 - combine all classes to the `game.py` doc
 - `Storylines` and `Room` should be combined and stored in `Game.locations`.
 - Implement the `Room.portals` property to better control navigation
 - ? Command dispatcher ? (main gameplay loop getting too long)
 - ? Dynamically control what is used in the loop at all through state?