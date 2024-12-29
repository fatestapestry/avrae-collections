`!lotrshadow setup`

## Description
Initializes Shadow tracking for characters in the "Lord of the Rings" 5E system. Sets up the necessary counters and assigns the character's Shadow Path based on their calling.

## Arguments
- No positional or optional arguments.

## Examples
- Initialize Shadow tracking for a character:  
  `!lotrshadow setup`

## Notes
- Automatically identifies the character's calling based on their class levels in LOTR-specific callings.
- Creates and initializes the following counters:
  - **Shadow Points**: Tracks points of Shadow gained through fear, doubt, and dark deeds. Initial value is `0`. Maximum value is determined by the character's Wisdom score.
  - **Shadow Scars**: Tracks permanent Shadow points. These can only be removed during Yule. Initial value is `0`. Maximum value is determined by the character's Wisdom score.
- Stores the Shadow Path information, including the calling and associated flaws.
- Provides an error message if no valid calling is found:
  - Lists current classes and their levels.
  - Displays a list of valid callings for the LOTR 5E system.
- Designed for use exclusively with the "Lord of the Rings Roleplaying" system.

## Issues?
You can file reports and feature requests, as well as see the source code, 
at my [GitHub](https://github.com/fatestapestry/avrae-collections)

## Support Me
You can support me and future development at [Ko-Fi](https://ko-fi.com/noralf)
