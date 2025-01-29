`!lotrfatigue [args]`

## Description
Performs a fatigue saving throw for LOTR 5e. Calculates a saving throw result based on constitution, modifiers, and optional bonuses. Adjusts the difficulty class (DC) dynamically based on events and other conditions.

## Arguments
- Optional arguments:
  - `adv|dis` - Specifies advantage or disadvantage on the saving throw.
  - `-dc <value>` - Sets a custom difficulty class (DC) (Default is 10) for the saving throw.
  - `-formcedmarch|fm` - Sets the difficulty class (DC) to 15. Not supported with events (for end-of-day saves only).
  - `-b <value>` - Adds custom bonuses to the saving throw.
  - `blessingdie` - Adds a blessing die to the saving throw.
  - `-mount <value>` - Adds the mount’s Constitution modifier to the saving throw.
  - `-event|e <event|abbr>` - Adds an event consequence modifier to save DC. Multiple events are supported. Supported event types:
`['terriblemisfortune|tm', 'despair|dp', 'illchoices|ic', 'mishap|mh', 'shortcut|sc', 'chancemeeting|cm', 'joyfulsight|js']`

## Examples
- Perform a fatigue saving throw with the default DC:  
  `!lotrfatigue`
- Add a blessing die and apply a mount bonus of 3:  
  `!lotrfatigue -event despair blessingdie -mount 3`
- Apply a custom DC of 15:  
  `!lotrfatigue -dc 15`
- Add an event modifier using its abbreviation:  
  `!lotrfatigue -e tm`
- Perform a fatigue saving throw with multiple events along the journey:  
  `!lotrfatigue -e tm -e illchoices -e mh -e tm`

## Notes
- The base DC for the saving throw is 10 unless overridden by the `-dc` argument or modified by events.
- Events modify the DC dynamically. You can add multiple events using `-e <event|abbr>` or `-event <event|abbr>`.
- Mount bonuses and blessing dice are automatically factored into the roll if specified.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
