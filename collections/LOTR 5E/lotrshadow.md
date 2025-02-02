`!lotrshadow <amt> [args]`

## Description
Modifies a character's Shadow Points or Shadow Scars in the "Lord of the Rings" system. Supports both direct and incremental changes, maintaining valid limits automatically.

## Arguments
- Positional arguments:
  - `<amt>` - The amount to adjust the counter by. Can be a positive, negative, or absolute value (e.g., `+1`, `-2`, `3`).
- Optional arguments:
  - `scar` - Applies the adjustment to Shadow Scars instead of Shadow Points.

## Examples
- Increment Shadow Points by 3:  
  `!lotrshadow +3`
- Decrement Shadow Scars by 1:  
  `!lotrshadow -1 scar`
- Set Shadow Points to 5:  
  `!lotrshadow 5`

## Notes
- Adjustments remain within the defined limits for Shadow Points or Shadow Scars.
- When adjusting Shadow Scars, the minimum value for Shadow Points may also be updated.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
