`!lotrcheck <skill> [args]`

## Description
Performs a skill check using the "Lord of the Rings" skill system. Supports custom LOTR-specific skills such as Explore, Hunting, Travel, Riddle, and Old Lore. Allows optional modifiers, including advantage or disadvantage.

## Arguments
- Positional arguments:
  - `<skill>` - The skill to check. Must be one of the following:
    - `explore` - Navigation and exploration-related tasks.
    - `hunting` - Tracking and foraging in the wilderness.
    - `travel` - Endurance and managing long journeys.
    - `riddle` - Solving riddles or interpreting hidden meanings.
    - `oldlore` - Knowledge of ancient stories, histories, and legends.
- Optional arguments:
  - `adv|dis` - Specifies advantage or disadvantage on the skill check.
  - `-b <value>` - Adds a custom bonus to the skill check.

## Examples
- Perform an Explore check:  
  `!lotrcheck explore`
- Perform a Riddle check with advantage:  
  `!lotrcheck riddle adv`
- Perform an Old Lore check with a +3 bonus:  
  `!lotrcheck oldlore -b 3`
- Perform a Hunting check with disadvantage:  
  `!lotrcheck hunting dis`

## Notes
- The skill must first be set up using the `!lotrcheck setup` command to configure its proficiency level.
- Internally, passes off skill checks to `!check`
- Uses the appropriate base ability score associated with each skill.
- Designed for use with the "Lord of the Rings" Roleplaying system.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
