import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    """
    print('Running systrm command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text= "True")
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output
    #s_err




if __name__ == '__main__':

    version= run_cmd(['hadoop', 'version'])
    print(version)

    new_directory= run_cmd(['hdfs', 'dfs', '-mkdir', '/HadoopCLI'])
    print(new_directory)

    list_all_directory= run_cmd(['hdfs', 'dfs', '-ls', '/'])
    print(list_all_directory)

    #to copy text file
    put_text= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/Testing/TestFile.txt', '/HadoopCLI'])
    print("Text File Created: ",put_text)

    #to put csv
    put_csv= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/Testing/Sample.csv', '/HadoopCLI'])
    print("CSV created: ",put_csv)

    #to put parquet file
    put_parq= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/Testing/ParquetSample.parquet', '/HadoopCLI'])
    print("Parquet Created: ",put_parq)

    #to put json
    put_json= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/Testing/JSONSample.json', '/HadoopCLI'])
    print("JSON created: ",put_json)

    #to put avro
    put_avro= run_cmd(['hdfs', 'dfs', '-put', '/home/hdoop/Testing/AvroSample.avro', '/HadoopCLI'])
    print("Avro created: ",put_avro)

    #listing the HadoopCLI folder
    list_all_directory= run_cmd(['hdfs', 'dfs', '-ls', '/HadoopCLI'])
    for i in list_all_directory:
        print(i)
    #print(list_all_directory)

    #options to read 3 kinds of file

    while(True):
        try:
            num = int(input("Please select your choice: 1. To read Text, 2. CSV, 3.Json, 4.EXIT    "))
            if num == 1:
                print("The text file TestFile is: ")
                cat= run_cmd(['hdfs', 'dfs', '-cat', '/HadoopCLI/TestFile.txt'])
                for i in cat:
                    print(i)

            elif num==2:
                print("The sample CSV file is: ")
                cat= run_cmd(['hdfs', 'dfs', '-cat', '/HadoopCLI/Sample.csv'])
                for i in cat:
                    print(i)

            elif num==3:
                print("The sample JSON file is: ")
                cat= run_cmd(['hdfs', 'dfs', '-cat', '/HadoopCLI/JSONSample.json'])
                for i in cat:
                    print(i)

            elif num==4:
                break
        except Exception as e:
            print(e)           




    remove_directory= run_cmd(['hdfs', 'dfs', '-rm', '-r', '/HadoopCLI'])
    print("Deleted succesfully!: ",remove_directory)
