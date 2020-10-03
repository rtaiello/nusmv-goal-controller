# NuSMV Goal Controller
[![License: GPL v3](https://img.shields.io/badge/-Sapienza%20University%20of%20Rome-red)](https://www.gnu.org/licenses/gpl-3.0)

## Description
This repository contains the code used to realize the project of [Formal Method in Software Development](https://twiki.di.uniroma1.it/twiki/view/MFS/FormalMethodsInSoftwareDevelopment20192020) a.y. 2019/2020 held at Sapienza University of Rome.
## Game grid
Given a grid (stated differently a matrix) which each cell have one of the following shape:
- Start cell (**S**);
- Obstacle cell (**#**);
- Legal cell (**o**);
- Goal cell (**G**).</br>

The system returns, if exists the best path from **S** leading to **G**.

Everything is done, using the definition of controller implemented in Python 3.6. (see [paragraph 4.1](http://mclab.di.uniroma1.it/publications/papers/mari/2014/110_Mari_etal2014.pdf)). </br>
The developed controller is realised interacting with **NuSMV** symbolic model checker. </br>
**Before run , ENSURE that the NuSMV bin (download here http://nusmv.fbk.eu/) is inside _numsmv_exactubles/linux_ or _numsmv_exactubles/mac-os_ folder (it depends on your o.s.)**

## Specification in Temporal Logic
In order to proof the existence of a path that doesn't have any obstacles **#** from **S** to **G**, we state the following Temporal Logic formulae:
- LTL :  ¬♢ (G*)
- CTL : ¬E♢ (G*)

G* means the coordinate of the Goal cell

## How To Run  Controller Game
> python3 goal_game.py