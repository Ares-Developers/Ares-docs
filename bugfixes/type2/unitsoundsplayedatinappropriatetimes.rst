.. index:: OpenTopped; Entering/leaving water sounds plays when infantry is transported

=========================================
Unit Sounds Played At Inappropriate Times
=========================================

When an :type:`InfantryType` with :tag:`MovementZone=AmphibiousDestroyer` was
carried between water and land inside an 'open topped' vehicle (e.g. a Nighthawk
converted into a flying Battle Fortress), their :tag:`EnterWaterSound`
/:tag:`ExitWaterSound` would be played. Now, these sounds will only be played
when the :type:`InfantryType` themselves physically enters/leaves water.

.. versionadded:: 0.1
