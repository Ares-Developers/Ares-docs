.. index:: Secret Labs; Secret lab boons are picked truly at random.

=========================
Secret Lab Boon Weighting
=========================

The random weighting of each possible Secret Lab boon was not calculated
correctly the later a boon appeared in the list the less likely it was to
appear in-game. For example, if the Grand Cannon were not picked as the boon for
the first Secret Lab on the map (probability 1/8) then it could not be picked
for any of the other Secret Labs. This has been fixed such that every Secret
Lab will pick its boon completely at random, independently of other Secret Labs
on the map.

.. versionadded:: 0.1
