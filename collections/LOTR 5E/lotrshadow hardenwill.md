`!lotrshadow hardenwill`

## Description
Clears all accumulated Shadow Points and adds a Shadow Scar to the character, representing a hardening of will at the cost of increased Shadow Scars. Ensures the process adheres to game mechanics, preventing actions that exceed allowable limits.

## Arguments
- No positional arguments or optional arguments.

## Examples
- Harden will and update the character's Shadow stats:  
  `!lotrshadow hardenwill`

## Notes
- Clears all Shadow Points above the minimum and increases the Shadow Scars counter by 1.
- Prevents action if:
  - Total Shadow exceeds the Wisdom score, requiring a bout of madness instead.
  - The maximum number of Shadow Scars (equal to the Wisdom score) is already reached.
- Automatically adjusts Shadow Points' minimum value when a Scar is added.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
