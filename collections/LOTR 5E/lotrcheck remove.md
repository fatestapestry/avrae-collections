`!lotrcheck remove <skill>`

## Description
Removes the configuration for a specified skill in the "Lord of the Rings" system. This action resets the skill's setup, making it no longer usable until reconfigured.

## Arguments
- Positional arguments:
  - `<skill>` - The skill to remove. Must be a valid skill from the LOTR system.

## Examples
- Remove the configuration for "Riddle":  
  `!lotrcheck remove riddle`
- Remove the configuration for "Hunting":  
  `!lotrcheck remove hunting`

## Notes
- Ensures the skill is valid and recognized within the LOTR system before removal.
- Displays an error if:
  - The skill is not recognized.
  - The skill has not been set up.
- Removes the skill's setup, resetting its configuration.
- Skills can be reconfigured later using the `!lotrcheck setup` command.
- Designed for use with the "Lord of the Rings" Roleplaying system.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
