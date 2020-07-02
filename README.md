# NuSMV Controller Game
Project releated to the course of the Formal Methods at the first year of Master in Computer Scinece @ La Sapienza, University of Rome.
## Game grid
Given a grid with:
- Start cell;
- Obstacle cell;
- Legal cell;
- Goal cell.</br>

The system returns, if exists the best path from the Start Cell leading to the Goal Cell.

Everything is done, using the definition of controller implemented in Python. (see [paragraph 4.1](http://mclab.di.uniroma1.it/publications/papers/mari/2014/110_Mari_etal2014.pdf)).
The developed controller is realised interacting with **NuSMV** symbolic model checker. </br>
**Before run , ENSURE that the NuSMV bin (dowload here http://nusmv.fbk.eu/) is inside linux or mac-os folder (it depends on your o.s.)**
## How To Run  Controller Game
> python3 goal_game.py
