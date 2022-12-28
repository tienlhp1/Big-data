# BigDataExercises
## Install Zeppelin using docker 
Make sure you install docker first 
http://zeppelin.apache.org/download.html
Using docker: ```docker run -p 8080:8080 --rm --name zeppelin apache/zeppelin:0.9.0```
## How to run
1. To run zeppelin: (Windows PowerShell)
Run bellow command in the current folder!

```docker run -p 8080:8080 --rm -v $PWD/data:/data -v $PWD/notebook:/notebook -e ZEPPELIN_DATA_DIR='/data' -e ZEPPELIN_NOTEBOOK_DIR='/notebook' --name zeppelin apache/zeppelin:0.9.0```

```Or (Windows only): Right click file StartZeppelin.ps1, select "Run with Powershell".```

- data: Folder to stored data files
- notebook: Folder to store notebook files

2. Access Zeppelin by go to localhost:8080 in your web browser. </br>

## Some other notes
1. Some note when using Zeppelin:
- "CTRL + ." is auto-complete code.


## Other Resources:
1. Repo of the Book "Learning Spark v2": https://github.com/databricks/LearningSparkV2
2. Doc: https://zeppelin.apache.org/docs/latest/interpreter/python.html
https://spark.apache.org/docs/1.6.1/api/python/


