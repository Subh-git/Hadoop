## Steps to operate the word count program.

1. Copy the mapper and reducer files to the hadoop installed user, ignore if only one user.

2. Start the hadoop  ecosystem with the following command from the home directory of hadoop user:
    start-all.sh
3. This will start all the hadoop services., verify by typing jps.

4.  Give special access to mapper and reducer as :
    chmod 777 mapper.py reducer.py

5. My python files are stored in a folder called Testing, hdfs location is /hadoopTesting 
    and my jar file is located in the following path:
    
    hadoop jar hadoop-3.3.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar
    hadoop jar hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar

6. Lastly we run the following command.(for my pc)
    hadoop jar hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
    -file Testing/mapper.py -mapper mapper.py \
    -file Testing/reducer.py -reducer reducer.py \
    -input /hadoopTesting/TestFile.txt \
    -output /hadoopTesting/output