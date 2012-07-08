.. index:: Map Triggers; Only existing players will receive reinforcements in multiplayer games through triggers.

===========================================
Reinforcements and Multiplayer Map Triggers
===========================================

Using the `Player@X` logic, :game:`Yuri's Revenge` would also try to reinforce
players that don't exist, which leads to a crash. When using `Reinforcement`,
`Reinforcement at Waypoint` and `Reinforcement by Chrono` map actions,
\ :game:`Ares` will only create a team if the player exists on the map.

.. versionadded:: 0.2
