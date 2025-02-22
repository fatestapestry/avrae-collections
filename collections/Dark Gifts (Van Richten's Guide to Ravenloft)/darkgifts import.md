`!darkgifts import <gift|abbr>`

## Description
Imports a specified Dark Gift into a character's setup. This includes setting up relevant counters and automation for abilities tied to the Dark Gift.

## Arguments
**Positional arguments**
  - `<gift|abbr>` - The name or abbreviation of the Dark Gift to import. Must be one of the following:
    - `echoingsoul` | `es`
    - `gatheringwhispers` | `gw`
    - `livingshadow` | `ls`
    - `mistwalker` | `mw`
    - `secondskin` | `ss`
    - `symbioticbeing` | `sb`
    - `touchofdeath` | `td`
    - `watchers` | `wa`

## Examples
Import a specific Dark Gift:
```
!darkgifts import livingshadow
```
Import using an abbreviation:
```
!darkgifts import ls
```

## Notes
- This command automatically creates relevant counters for the Dark Gift.
- Validates and loads necessary automation for the Dark Gift.
- The alias **overrides** existing counters and actions if re-run.

## Issues?
You can file reports and feature requests as well as see the source code on [**GitHub**](https://github.com/fatestapestry/avrae-collections).

## Support Me!
Please consider contributing to future development and maintenance by supporting me on [**Patreon**](https://www.patreon.com/fatestapestry), or donating on [**Ko-Fi**](https://ko-fi.com/noralf).