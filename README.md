## Solve some bug in Macos
------
Add to ssl.py（in /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py） in macos:  

    _create_default_https_context = _create_unverified_context 


## Build apk
-------
In the project root dictory `./`, and run:

>>1.`buildozer init`   
>>2.`buildozer android debug deploy run`  

To generate .apk in `./bin`.



## some error
-------

Java Runtime Enviroment is needed.  

`sudo apt-get install default-jdk` to install `javac`  

`buildozer android clean` can solve `No module named _ctypes` error  

add JAVA_HOME to enviroment, bashrc or zshrc:  
`export PATH=/usr/lib/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH`
`export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64`

