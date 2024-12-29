`!lotrevent <role> <terrain> [args]`

## Description
Simulates a journey event during travel in the "Lord of the Rings" system. Rolls for an event, determines the outcome based on skill checks, and provides descriptive feedback for the event and terrain.

## Arguments
- Positional arguments:
  - `<role>` - Specifies the journey role for the character. Must be one of the valid roles defined in the system (e.g., Guide, Scout).
  - `<terrain>` - Specifies the terrain type for the event. Must be a valid terrain type (e.g., Mountains, Forest).
- Optional arguments:
  - `adv|dis` - Specifies advantage or disadvantage on the event roll.
  - `-dc <value>` - Overrides the default difficulty class (DC) for the terrain.
  - `autumn|winter` - Applies a disadvantage on the skill check due to seasonal conditions.
  - `multipleroles` - Applies a penalty for taking multiple roles during the journey.
  - `blessingdie` - Adds a blessing die to the skill check roll.

## Examples
- Roll a journey event for the role of Guide in a Forest:  
  `!lotrevent guide forest`
- Roll an event with a custom DC of 15:  
  `!lotrevent scout mountains -dc 15`
- Apply disadvantage for autumn conditions:  
  `!lotrevent hunter plains autumn`
- Roll an event with a blessing die and multiple roles penalty:  
  `!lotrevent guide hills blessingdie multipleroles`

## Notes
- Uses skill checks tied to the specified role to determine success or failure (see LOTR 5E sourcebook)
- Blessing dice and penalties are automatically applied based on optional arguments.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
