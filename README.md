This is tutorial handler. 
Ever tried to collect snippets (screenshots) of a tutorial for future purposes.
This is simple solution for this problem.

Delete all files from `assets/`<br/>

Steps while capturing snippets:<br/>
    Run `watchman.py` file<br/>
        `$python3 watchman.py`<br/>
    Whenever take a new screenshot. Move that file in `assets/`<br/>
    watchman.py will handle the naming.<br/>
Steps while capturing snippets:<br/>
    Run `watchman.py` file <br/>  
         format is<br/>
         `$python3 watchman.py time` <br/>
        `$python3 watchman.py 1`<br/>
         Update interval is set to 1 (sec).
    Whenever take a new screenshot. Move that file in `assets/`<br/>
    watchman.py will handle the naming.<br/>

View the tutorial.<br/>
    Open `tutorial.html` in browser for view.<br/>
    Use `next` and `prev` button for next snippet and previous snippet respectively.<br/>  
    When no further snippets will be available the page will show `no img available`<br/>
**Note<br/>
Only one file change is expected per time interval i.e. Update_interval (in watchman.py)<br/>
Currently Update_interval is 1 (in sec).<br/>

More functionalities<br/>
    You can delete any intermediate snippet `watchman.py` will re-number all the files.<br/>


TODO:<br/>
    Add an video of working example.<br/>
