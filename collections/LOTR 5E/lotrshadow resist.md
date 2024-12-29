`!lotrshadow resist <source> <amt> [args]`

## Description
Attempts to resist a source of Shadow, representing a test of willpower against dark influences. Rolls a saving throw to determine how effectively the Shadow is resisted and adjusts Shadow Points accordingly.

## Arguments
- Positional arguments:
  - `<source>` - The source of the Shadow effect being resisted. Must be a valid source defined in the system.
  - `<amt>` - The base amount of Shadow to resist. Must be a positive number.

- Optional arguments:
  - `adv|dis` - Specifies advantage or disadvantage on the saving throw.
  - `-ability <name>` - Specifies the ability used for the saving throw (e.g., `wisdom`, `charisma`). Defaults to the source's recommended ability.
  - `-b` - Includes a custom bonus to the saving throw.
  - `-dc <value>` - Specifies the saving throw difficulty class (DC). Defaults to the source's recommended DC.
  - `miserable` - Treats the character as Miserable, automatically failing on a roll of 2 or less.

## Examples
- Resist Shadow from "Corruption" with a base amount of 3:  
  `!lotrshadow resist Corruption 3`
- Resist Shadow from "Despair" with a custom DC of 15:  
  `!lotrshadow resist Despair 4 -dc 15`
- Resist with a specified ability (e.g., Wisdom):  
  `!lotrshadow resist Fear 2 -ability wisdom`
- Resist with advantage:  
  `!lotrshadow resist Threat 5 adv`
- Resist with disadvantage:  
  `!lotrshadow resist Doubt 2 dis`
- Resist while Miserable:  
  `!lotrshadow resist Threat 5 miserable`
- Resist with a custom bonus of +3:  
  `!lotrshadow resist Influence 4 -b 3`

## Notes
- Determines the amount of Shadow resisted based on the result of a saving throw:
  - A success reduces Shadow by 1.
  - A result exceeding the DC by 5 or more reduces Shadow by 2.
  - Failure applies the full Shadow amount.
- Miserable characters automatically fail the save on a natural roll of 2 or less.
- Defaults for `-ability` and `-dc` are derived from the specified source.
- Adjusts the character's Shadow Points based on the outcome of the roll.
- Designed to align with the mechanics of the "Lord of the Rings" system.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)