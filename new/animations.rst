Animation Damage
~~~~~~~~~~~~~~~~

Using a Weapon
``````````````

Instead of dealing damage directly using the :tag:`Warhead`, a weapon can be
defined to create a projectile and detonate it immediately. This allows some
weapon effects to be applied.

:tagdef:`[Animation]Weapon=weapon`
  The weapon used to deliver animation damage. If set, creates a projectile and
  detonates it immediately. The damage delivered is defined by the animation,
  not the weapon.

  .. note:: The weapon has to be known to the game already, otherwise it cannot
    be parsed correctly. It is recommended to add it to the :type:`WeaponTypes`
    list.

  .. note:: Currently, the created projectile is neither owned by the player who
    created the animation nor the owner of the unit or structure the animation
    is attached to. While damage delivered using :tag:`Warhead` at least knows
    about the player who created the animation for scoring purposes, weapon
    damage does not pass on this information. This might change in the future.

.. versionadded:: 2.0


Damage Delay
````````````

:tagdef:`[Animation]Damage.Delay=integer - animation frames`
  The delay between two applications of animation damage. Requires :tag:`Damage`
  greater than or equal to :value:`1.0`. A value of :value:`0` disables the
  delay. Defaults to :value:`0`.

  .. note:: Mind that this value is measured in animation frames: depending on
    :tag:`Rate`, the animation might not advance to the next animation frame
    every game frame.

.. versionadded:: 2.0
