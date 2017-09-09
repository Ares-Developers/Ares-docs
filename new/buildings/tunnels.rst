Tunnel Networks
~~~~~~~~~~~~~~~

This is the tunnel systems known from :game:`Generals`. Tunnels are buildings
that allow to quickly move units from one place to another. There can be many
entrance buildings, but they all share the same queue of occupants. Units do not
actually move between tunnels; after they entered an entrance they can be
ejected from another entrance immediately.

The occupants will be kept alive until the last entrance of the same type owned
by the same player is destroyed. The killer of the last entrance will be awarded
the kills of the occupants also. If the last entrance is sold, units will try to
evacuate.

Different tunnel types are declared as list under the :tag:`[TunnelTypes]`
section, and they have the following options:

:tagdef:`[TunnelType]Passengers=integer`
  The maximum number of occupants this tunnel system can have. This does not
  consider size. Each unit takes up one slot of space. Defaults to :value:`0`.

:tagdef:`[TunnelType]MaxSize=double`
  The maximum :tag:`Size=` units can have to be allowed into this tunnel.
  Defaults to :value:`0.0`.

.. quickstart:: If you don't get the enter cursor on the tunnel entrances, check
  that you correctly set :tag:`Passengers=` and :tag:`MaxSize` on the
  :type:`TunnelType`.

Then, a :type:`BuildingType` can be turned into a tunnel entrance by setting the
following tag. Multiple :type:`BuildingType`\ s can share the same tunnel type.
Tunnel entrances play :tag:`EnterTransportSound` and :tag:`LeaveTransportSound`
whenever a unit enters or leaves the building. The entrance building
will show pips representing the contents of the tunnel system.

:tagdef:`[BuildingType]Tunnel=TunnelType`
  The type of tunnel system this building is an entrance to.

  .. note:: Tunnel buildings are not allowed to have weapons, turrets and can't
    be capturable or mind-controllable.

  .. warning:: Hover units have the same problems with tunnel entrance buildings
    as they have entering :tag:`UnitAbsorb=yes` buildings.

Example:
  ::

    ; Tunnel declarations
    [TunnelTypes]
    0=GLATunnel
    1=CivilianTunnel
    2=LoveTunnel

    ; Tunnel definition
    [GLATunnel]
    Passengers=8
    MaxSize=4.0

    ; Civilian Tunnel Entrance Building
    [CATNNL]
    Tunnel=CivilianTunnel

.. index:: Buildings; Tunnel Networks

.. versionadded:: 0.E
