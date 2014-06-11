Sides & Countries
~~~~~~~~~~~~~~~~~

In the original game the sides and countries were, for the most part,
hard-coded. You could not add to, remove or reorder the 10 countries or 3 sides.
:game:`Ares`, however, makes these tasks possible - you can now have up to 16
fully functional countries and sides, and you can customize these in numerous
ways...

.. note:: Certain flags work properly for up to 32 countries, and yet others
  fail after merely 16 - it is recommended to not have any more than 16
  playable countries and 32 total countries. Put the playable countries first in
  the list, followed by the other countries.

.. index:: Sides; New sides & countries (including numerous enhancements).


Sides
`````

Sides are specified in the :tag:`[Sides]` list in :file:`rulesmd.ini`.

There is no limit to the number of sides that can be defined. However, only 16
fully-working countries can be implemented (see above).

Each side can (and should) define its own values for the following flags in the
side's INI section.

.. toctree::
	:glob:
	
	defaultside
	uiside


Countries
`````````

Countries are specified in the :tag:`[Countries]` list in :file:`rulesmd.ini`.
Any country with :tag:`Multiplay=yes` set will appear in the country selection
drop-down list and be eligible for random selection if the player chooses
'Random'. Countries can be excluded from the 'random country' option, or given
differing weights.

The :tag:`[Countries]` list can contain up to 32 countries, however taunts
will only work for 16 of these.

Each country can be customized using the following flags in the country's INI
section.

.. toctree::
	:glob:
	
	defaultcountry
	uicountry
