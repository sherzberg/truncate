truncate
========

truncate

Return a nicely shortened string if over a set upper limit
    (default 75 characters)

    What is nicely shortened? Consider this line from Orwell's 1984...
    0---------1---------2---------3---------4---------5---------6---------7---->
    When we are omnipotent we shall have no more need of science. There will be

    If the limit is set to 70, a hard truncation would result in...
    When we are omnipotent we shall have no more need of science. There wi...

    Truncating to the nearest space might be better...
    When we are omnipotent we shall have no more need of science. There...

    The best truncation would be...
    When we are omnipotent we shall have no more need of science...

    Therefore, the returned string will be, in priority...

    1. If the string is less than the limit, just return the whole string
    2. If the string has a period, return the string from zero to the first
        period from the right
    3. If the string has no period, return the string from zero to the first
        space
    4. If there is no space or period in the range return a hard truncation

    In all cases, the string returned will have ellipsis appended unless
    otherwise specified.

    Parameters:
        s = string to be truncated as a String
        min_pos = minimum character index to return as Integer (returned
                  string will be at least this long - default 0)
        max_pos = maximum character index to return as Integer (returned
                  string will be at most this long - default 75)
        ellipsis = returned string will have an ellipsis appended to it
                   before it is returned if this is set as Boolean
                   (default is True)
    Returns:
        Truncated String
    Throws:
        ValueError exception if min_pos > max_pos, indicating improper
        configuration
    Usage:
    short_string = trunc(some_long_string)
    or
    shorter_string = trunc(some_long_string,max_pos=15,ellipsis=False)

Install
=======

```bash
$ pip install truncate
```

Development
===========

To run the tests you need pytest:

```bash
$ pip install -r test-requirements.txt
$ py.test
```
