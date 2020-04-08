## This is tutorial handler. 
Ever tried to collect snippets (screenshots) of a tutorial for future purposes (revision).
This is simple offline solution for this problem.

### STEPS<br/>
1. clone repository<br/>
    `$git clone https://github.com/anumaurya114/useless-tutorial-handler.git`<br/>
    `$cd useless-tutorial-handler`<br/>
    
2. Delete all files from `assets/`<br/>

3. Steps while capturing snippets:<br/>
    Run `watchman.py` file<br/>
        `$python3 watchman.py`<br/>
    Whenever take a new screenshot. Move that file in `assets/`<br/>
    watchman.py will handle the naming.<br/>

4. View the tutorial.<br/>
    Open `tutorial.html` in browser for view.<br/>
    Use `next` and `prev` button for next snippet and previous snippet respectively.<br/>  
    When no further snippets will be available the page will show `no img available`<br/>
**Note<br/>
Only one file change is expected per time interval i.e. Update_interval (in watchman.py)<br/>
Currently Update_interval is 1 (in sec).<br/>

More functionalities<br/>
    You can delete any intermediate snippet( single file) `watchman.py` will re-number all the files.<br/>


TODO:<br/>
    Add an video of working example.<br/>
