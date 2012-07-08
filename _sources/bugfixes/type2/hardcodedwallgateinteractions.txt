.. index:: Walls; Gates can be slammed onto any walls not just GAWALL or NAWALL.

================================
Hardcoded Wall/Gate Interactions
================================

In :game:`Tiberian Sun` you could place buildable gates on top of existing
walls. This logic still exists in :game:`Yuri's Revenge`. However, the logic was
hardcoded to only work with :tag:`[GAWALL]` and :tag:`[NAWALL]`, so it wouldn't
work with Yuri's wall (:tag:`[YAWALL]`) or, indeed, any other walls you might
add to the game. :game:`Ares` changes this so that all overlays with
:tag:`Wall=yes` set can have gates "slammed" onto them.

.. note:: The automatic joining of walls to the gates still only works for
  \ :tag:`GAWALL` and :tag:`NAWALL` however this will be fixed in future.

.. versionadded:: 0.1
