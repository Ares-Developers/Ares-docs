.. _custom-ivan-bombs:

.. index::
  Weapons; Multiple Ivan Bombs with separate settings
  Ivan Bombs; Multiple weapons with separate settings
  Ivan Bombs; Death bombs blow up when the victim dies

Ivan Bombs
~~~~~~~~~~

As with many other features of :game:`Yuri's Revenge`, the settings that control
Crazy Ivan Bombs are global so you can't have multiple variations of them with
their own controls. With :game:`Ares` it is now possible to create new Ivan
Bomb-esque weapons -- new types of sticky bomb with whatever settings you like.

:game:`Ares` adds the Death Bombs feature, which was originally planned to be in
but were cut from the game before :game:`Red Alert 2` was released. Death Bombs
can rig victims with bombs that will not detonate automatically, but remain
active either until the unit dies to go off then, or the owner manually
detonates it, if allowed.

:game:`Ares` now also supports shrapnel weapons, as long as they have a
:tag:`CellSpread` of :value:`0.5` or more.

When :tag:`IvanBomb=yes` is set on the weapon's warhead, the weapon can specify
the following flags in order to customize that bomb:

:tagdef:`[Weapon]IvanBomb.Warhead=WarheadType`
  The warhead that will be used when the bomb detonates. Defaults to
  :tag:`[CombatDamage]IvanWarhead`.
:tagdef:`[Weapon]IvanBomb.Damage=integer`
  The damage that will be dealt when the bomb detonates. Defaults to
  :tag:`[CombatDamage]IvanDamage`.
:tagdef:`[Weapon]IvanBomb.DeathBomb=boolean`
  Whether this bomb will be a death bomb instead of a timed bomb when planted on
  enemy objects. Defaults to :value:`no`.
:tagdef:`[Weapon]IvanBomb.DeathBombOnAllies=boolean`
  Whether this bomb will be a death bomb instead of a timed bomb when planted on
  allied objects. Defaults to :value:`no`.
:tagdef:`[Weapon]IvanBomb.Detachable=boolean`
  Whether or not Engineers can remove this bomb from units it has been attached
  to. Defaults to :value:`yes`.
:tagdef:`[Weapon]IvanBomb.DestroysBridges=boolean`
  Whether or not this bomb can be used on Bridge Repair Huts in order to destroy
  the corresponding Bridge. Defaults to :value:`yes`.
  
  .. note:: Bombs can always be attached to Bridge Huts, but the resulting
    explosion will not destroy the bridge unless
    \ :tag:`IvanBomb.DestroysBridges=yes` is set.
:tagdef:`[Weapon]IvanBomb.CanDetonateTimeBomb=boolean`
  Whether or not players can manually detonate time bombs attached by this
  weapon. Defaults to :tag:`[CombatDamage]CanDetonateTimeBomb`.
:tagdef:`[Weapon]IvanBomb.CanDetonateDeathBomb=boolean`
  Whether or not players can manually detonate death bombs attached by this
  weapon. Defaults to :tag:`[CombatDamage]CanDetonateDeathBomb`.
:tagdef:`[Weapon]IvanBomb.DetonateOnSell=boolean`
  Whether attached bombs shall explode if the victim is sold. Otherwise, the
  bomb will just be disarmed. Defaults to :value:`yes`.
:tagdef:`[Weapon]IvanBomb.Delay=integer`
  The number of frames that will elapse before the bomb detonates automatically.
  Defaults to :tag:`[CombatDamage]IvanTimedDelay`.
:tagdef:`[Weapon]IvanBomb.AttachSound=sound name`
  The sound that will be played when the bomb is attached to a target. Defaults
  to :tag:`[AudioVisual]BombAttachSound`.
:tagdef:`[Weapon]IvanBomb.TickingSound=sound name`
  The sound that will be played whilst the bomb is attached to a unit. In order
  for this sound to loop correctly, the sound must have :tag:`Control=loop` set
  in its INI section in :file:`soundmd.ini`. Defaults to
  :tag:`[AudioVisual]BombTickingSound`.
:tagdef:`[Weapon]IvanBomb.Image=filename, *excluding*the .shp extension`
  The SHP file for the image to display over a unit that has a bomb attached to
  them, in the format "filename"(the ".shp" extension is automatically added by
  the engine). If the image cannot be loaded then the game will fall back to the
  default :file:`bombcurs.shp`.
:tagdef:`[Weapon]IvanBomb.FlickerRate=integer`
  The rate at which the bomb SHP will flip back and forth between two frames to
  give the impression of a flickering fuse. Must be higher than :value:`0`.
  Defaults to :tag:`[CombatDamage]IvanIconFlickerRate`.
  
  The animation is slowed down to play over the entire lifetime of the bomb
  (:tag:`IvanBomb.Delay`). The flicker rate is the number of frames between
  alternating between the current frame and the following frame.
  :tag:`IvanBomb.FlickerRate=5` means the current frame is shown 5 frames, then
  the next one for 5 frames, then the current one again for 5 frames, ....

Originally this logic was hard-coded to ignore the last frame of the bomb SHP,
which was originally planned to be used for Death Bombs. This hard-coding has
been changed so that the whole SHP is now considered for the fuse, however this
means that you'll now see that extra frame from :file:`bombcurs.shp`, unless you
replace that SHP file.

.. image:: /images/bombcurs.png
  :alt: Image of bombcurs.shp
  :align: center

.. versionadded:: 0.1
.. versionchanged:: 0.5
.. versionchanged:: 0.D
