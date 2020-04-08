This is tutorial handler. 
Ever tried to collect snippets (screenshots) of a tutorial for future purposes.
This is simple solution for this problem.

Steps while capturing snippets:
    Run `watchman.py` file
        `$python3 watchman.py`
    Whenever take a new screenshot. Move that file in `assets/`
    watchman.py will handle the naming.

View the tutorial.
    Open `tutorial.html` in browser for view.
    Use `next` and `prev` button for next snippet and previous snippet respectively.   
    When no further snippets will be available the page will show `no img available`
**Note
Only one file change is expected per time interval i.e. Update_interval (in watchman.py) 
Currently Update_interval is 1 (in sec).

More functionalities 
    You can delete any intermediate snippet `watchman.py` will re-number all the files.


TODO:
    Add an video of working example.