.. _custom-ivan-bombs:

.. index::
  Weapons; Multiple Ivan Bombs with separate settings
  Ivan Bombs; Multiple weapons with separate settings
  Ivan Bombs; Death bombs blow up when the victim dies

Ivan Bombs
~~~~~~~~~~

As with many other features of :game:`Yuri's Revenge`, the settings that control
Crazy Ivan Bombs are global so you cannot have multiple variations of them with
their own controls. With :game:`Ares` it is now possible to create new Ivan
Bomb-esque weapons -- new types of sticky bomb with whatever settings you like.

:game:`Ares` adds the Death Bombs feature, which was originally planned to be in
but were cut from the game before :game:`Red Alert 2` was released. Death Bombs
can rig victims with bombs that will not detonate automatically, but remain
active either until the unit dies to go off then, or the owner manually
detonates it, if allowed.

:game:`Ares` now also supports shrapnel weapons, as long as they have a
:tag:`CellSpread` of :value:`0.5` or more.

.. versionadded:: 0.1
.. versionchanged:: 3.0


General Bomb Settings
---------------------

When :tag:`IvanBomb=yes` is set on the weapon's warhead, the weapon can specify
the following flags in order to customize that bomb:

:tagdef:`[Weapon]IvanBomb.Delay=integer`
  The number of frames that will elapse before a time bomb detonates
  automatically. Defaults to :tag:`[CombatDamage]IvanTimedDelay`.
:tagdef:`[Weapon]IvanBomb.Warhead=Warhead`
  The warhead that will be used when the bomb detonates. Defaults to
  :tag:`[CombatDamage]IvanWarhead`.
:tagdef:`[Weapon]IvanBomb.Damage=integer`
  The damage that will be dealt when the bomb detonates. Defaults to
  :tag:`[CombatDamage]IvanDamage`.
:tagdef:`[Weapon]IvanBomb.AttachSound=sound name`
  The sound that will be played when the bomb is attached to a target. Defaults
  to :tag:`[AudioVisual]BombAttachSound`.
:tagdef:`[Weapon]IvanBomb.TickingSound=sound name`
  The sound that will be played whilst the bomb is attached to a unit. In order
  for this sound to loop correctly, the sound must have :tag:`Control=loop` set
  in its INI section in :file:`soundmd.ini`. Defaults to
  :tag:`[AudioVisual]BombTickingSound`.


Bomb Behavior
-------------

:tagdef:`[Weapon]IvanBomb.DeathBomb=boolean`
  Whether this bomb will be a death bomb instead of a timed bomb when planted on
  enemy objects. Defaults to :value:`no`.
:tagdef:`[Weapon]IvanBomb.DeathBombOnAllies=boolean`
  Whether this bomb will be a death bomb instead of a timed bomb when planted on
  allied objects. Defaults to :value:`no`.
:tagdef:`[Weapon]IvanBomb.CanDetonateTimeBomb=boolean`
  Whether or not players can manually detonate time bombs attached by this
  weapon. Defaults to :tag:`[CombatDamage]CanDetonateTimeBomb`.
:tagdef:`[Weapon]IvanBomb.CanDetonateDeathBomb=boolean`
  Whether or not players can manually detonate death bombs attached by this
  weapon. Defaults to :tag:`[CombatDamage]CanDetonateDeathBomb`.
:tagdef:`[Weapon]IvanBomb.DetonateOnSell=boolean`
  Whether attached bombs shall explode if the victim is sold. Otherwise, the
  bomb will just be disarmed. Defaults to :value:`yes`.
:tagdef:`[Weapon]IvanBomb.Detachable=boolean`
  Whether or not Engineers can remove this bomb from units it has been attached
  to. Defaults to :value:`yes`.
:tagdef:`[Weapon]IvanBomb.DestroysBridges=boolean`
  Whether or not this bomb can be used on Bridge Repair Huts in order to destroy
  the corresponding bridge. Defaults to :value:`yes`.
  
  .. note:: Bombs can always be attached to Bridge Repair Huts, but the
    resulting explosion will not destroy the bridge unless
    \ :tag:`IvanBomb.DestroysBridges=yes` is set.


Bomb Overlay Image
------------------

A bomb overlay image file has to contain zero or more blocks (each consisting of
two frames) of flickering images for time bombs, followed by a single, optional
frame used as image for Death Bombs.

The image file used for only Death Bombs thus might contain a single frame only,
while the image file used only for time bombs are allowed to contain the
flickering image blocks only and omit the last frame. If a bomb might be both,
the image file has to contain images for both bomb types.

.. image:: /images/bombcurs.png
  :alt: Image of bombcurs.shp
  :align: center

The original :file:`bombcurs.shp` contains thirteen frames: six blocks of
flickering images at the beginning, followed by one image at the end for the
Death Bomb that was planned but cut from :game:`Red Alert 2`.

Death Bombs will always display their only frame while for time bombs the
animation defined by the flickering image blocks is stretched to play over the
entire lifetime of the bomb defined by :tag:`IvanBomb.Delay`.

:tagdef:`[Weapon]IvanBomb.Image=filename, *excluding*the .shp extension`
  The SHP file for the image to display over a unit that has a bomb attached to
  them, in the format "filename"(the ".shp" extension is automatically added by
  the engine). If the image cannot be loaded then the game will fall back to the
  default :file:`bombcurs.shp`.
:tagdef:`[Weapon]IvanBomb.FlickerRate=integer`
  The number of frames at which the bomb image will alternate between the two
  flickering images in a block to give the impression of a flickering fuse. If
  :value:`0`, flickering is disabled. Defaults to
  :tag:`[CombatDamage]IvanIconFlickerRate`.

  :tag:`IvanBomb.FlickerRate=5` means the first frame is shown 5 frames, then
  the second one for 5 frames, then the first one again for 5 more frames, ....

  If flickering is disabled, all images in all blocks are played over the
  lifetime of the bomb. The second frame of each block is not ignored and
  it thus is not necessary to add an empty frame to fill up a block. Still, the
  logic only deals in full flickering image blocks and will ignore the last
  frame if the number of frames in the file is odd.

.. note:: The logic works best if :tag:`IvanBomb.Delay` is a multiple of the
  number of flickering image blocks and :tag:`IvanBomb.FlickerRate`. Then each
  frame is played smoothly for the same amount of time.
