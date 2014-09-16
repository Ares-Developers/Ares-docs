Ordinary Damage for :captiontag:`IsSonic` and :captiontag:`UseFireParticles`
````````````````````````````````````````````````````````````````````````````

Weapons with either :tag:`IsSonic=yes` or :tag:`UseFireParticles=yes` do not
deliver conventional damage and rely on other means like ambient damage.

:tagdef:`[Weapon]ApplyDamage=boolean`
  Whether this weapon deals ordinary damage. Can be used to enable :tag:`Damage`
  to work with special weapons, or to disable dealing damage. Defaults to
  :value:`no` if either :tag:`IsSonic=yes` or :tag:`UseFireParticles=yes`, to
  :value:`yes` otherwise.

.. index:: Weapons; Ordinary damage for IsSonic and UseFireParticles weapons

.. versionadded:: 0.8
