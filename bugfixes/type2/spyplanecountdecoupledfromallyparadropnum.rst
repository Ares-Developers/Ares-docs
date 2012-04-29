.. index:: Spy Planes; SpyPlane.Count decoupled from AllyParaDropNum.

===========================================================
SpyPlane Count Decoupled From :captiontag:`AllyParaDropNum`
===========================================================

If you set :tag:`[General]AllyParaDropNum` to a list of integers so as to send multiple
\ :type:`InfantryTypes` in the paradrop (and thus multiple paradrop planes) then
the SpyPlane super weapon would also send the same number of planes as there
were elements in that list. In :game:`Ares`, the number of spy planes sent out
is now specified by the super weapon's own :tag:`SpyPlane.Count` flag (which
defaults to :value:`1`).

.. versionadded:: 0.1

