`!lotrcheck setup <skill> [none|half|pro|exp]`

## Description
Configures a skill for use in the "Lord of the Rings" system by setting its proficiency level. Supports customizing proficiency as None, Half Proficiency, Proficient, or Expertise.

## Arguments
- Positional arguments:
  - `<skill>` - The skill to configure. Must be a valid skill from the LOTR system.
  - `[none|half|pro|exp]` - The proficiency level to set:
    - `none` - No proficiency bonus.
    - `half` - Half proficiency bonus.
    - `pro` - Full proficiency bonus.
    - `exp` - Expertise (double proficiency bonus).

## Examples
- Configure "Riddle" with full proficiency:  
  `!lotrcheck setup riddle pro`
- Configure "Explore" with half proficiency:  
  `!lotrcheck setup explore half`
- Reset "Travel" to no proficiency:  
  `!lotrcheck setup travel none`
- Set "Old Lore" to Expertise:  
  `!lotrcheck setup oldlore exp`

## Notes
- Ensures the skill is valid and recognized within the LOTR skill system.
- Displays an error if:
  - The skill is not recognized.
  - The proficiency level is invalid.
- Updates the character's configuration, making the skill usable in `!lotrcheck`.
- Configured skills can be removed later using `!lotrcheck remove <skill>`.
- Designed for use with the "Lord of the Rings" Roleplaying system.


## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
