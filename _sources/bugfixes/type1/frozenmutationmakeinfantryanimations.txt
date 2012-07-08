.. index:: Mutation; Stuck mutation animations are deleted (thus preventing a memory leak).

=======================================================
Frozen Mutation (:captiontag:`MakeInfantry`) Animations
=======================================================
Infantry killed by a mutation warhead appear to transform into another
:type:`InfantryType`. Internally this is achieved by playing an animation, upon
completion of which a new infantry unit is spawned. If the cell where the new
infantry is to be spawned is already occupied then the animation will pause on
the final frame until the obstacle is cleared.

The original game would allocate memory for the new infantry on every frame but
would fail to de-allocate that memory when the infantry could not be placed.
The more time that passes with the animation in this state, the worse the memory
leak gets resulting in the game eventually grinding to a halt. :game:`Ares`
fixes this by simply deleting the animation if the new infantry unit cannot be
spawned. 

.. versionadded:: 0.1
