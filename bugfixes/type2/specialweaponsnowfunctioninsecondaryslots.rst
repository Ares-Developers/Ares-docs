.. index:: Weapons; Special weapons will now work in the Secondary slot

=================================================
"Special" Weapons now function in secondary slots
=================================================

Units with weapons that use :tag:`MindControl=yes`, :tag:`Parasite=yes` or
\ :tag:`Temporal=yes` require special treatment behind-the-scenes in order to
function. However, the original game only performed this treatment if those
units had such weapons as their :tag:`Primary` weapon. The treatment would not
be applied for :tag:`Secondary` weapons and thus result in crashes.
:game:`Ares` performs the treatment for :tag:`Secondary` weapons too.

.. note:: The 'special treatment' sets up the object wielding these weapons.
	However, the original code is not designed to handle an object having
	more than one weapon with 'special' functionality so it is not
	recommended to have multiple weapons with the same type of special
	functionality on a single object.

.. versionadded:: 0.1
