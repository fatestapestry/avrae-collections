`!lotrshadow path <flaw|none>`

## Description
Manages the character's Shadow Path flaws by setting them to a specified flaw or resetting them entirely. Allows manual adjustments to the progression of flaws on the Shadow Path.

## Arguments
- Positional arguments:
  - `<flaw|none>` - Specifies the flaw to set as the current maximum flaw in the Shadow Path, or use `none` to reset all flaws.

## Examples
- Set the current flaw to "Despair":  
  `!lotrshadow path despair`
- Reset all flaws to none:  
  `!lotrshadow path none`

## Notes
- Prevents invalid actions by:
  - Validating the character's Shadow Path is properly set up.
  - Ensuring the specified flaw exists in the Shadow Path.
- Provides a list of valid flaws if the specified flaw is invalid.
- Designed for use with the "Lord of the Rings" system mechanics.
- Updates the Shadow Path to reflect the selected flaw or clears all flaws if `none` is specified.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
