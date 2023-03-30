# Internal Development in QA (SDET) Team

## Code in file "sync.py"

### To use this program, you can run it from the command line with the following arguments:
<pre><code> python sync.py [source folder] [replica folder] [sync interval in seconds] [log file] </code></pre>
#### This command should start copying, deleting or replacing files referring to the source folder in the folder you specified as a replica at the interval you specify.


### If the code does not run and throws a permission related error, then you can run the process as an administrator with this command:
<pre><code> sudo python sync.py [source folder] [replica folder] [sync interval in seconds] [log file] </code></pre>
