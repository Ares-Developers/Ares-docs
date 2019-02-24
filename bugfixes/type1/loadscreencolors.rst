.. index:: Load Screens; Separate load screen text colors for each faction

==================
Load Screen Colors
==================

Westwood did not update the code that selects the load screen text color for
:game:`Yuri's Revenge`. The original campaigns always used :value:`SovietLoad`
red no matter what faction you played as. For the multiplayer game modes,
everything that was not Allied got :value:`SovietLoad` red, too. :game:`Ares`
selects these values: Allies get :value:`AlliedLoad` blue for campaigns and Yuri
gets either the new :value:`YuriLoad` or :value:`Purple` as fallback in
multiplayer.

.. versionadded:: 0.2
