# Large_File_Procesor
1.first of all clone this repository <br />
2.create a virtual environmen (optional) and install the requirements.txt<br />
 pip install -r requirements.txt\
3.download and copy input file from the below into /resource/data/input<br />
https://drive.google.com/file/d/1m4OnasKpLyFhcasSMBv0CuGKF6FFV_-J/view?usp=sharing<br />

### Framework : Python
### Database : SQLite (as it is python in-built database)

### After setup
Under data_processing application we will be having 6 python files.\
BTW lfp stands for large file processing :-)\
1.cmd.py - Main file (Here execution starts)\
2.config.py - All the environmental variables and default constants are updated here.\
3.lfp_method_init.py - Its is store all the abstract methods that were used in the application\
4.lfp_method_init_impl.py - It will be having all the implementations of the abstract methods.\
5.lfp_serive.py - Its the run function type for this application.\
6.log_utils.py - Logs are initialized here.\

### Working
* when the cmd.py is run it triggers the lfp_service which run's the process End to End.\
lfp_service creates 1.Log directory - here all the detailed logs are stored.\
                    2.sqlite - it has the database that stores out data in 2 tables.\
                            2.1 product : Its the source data (data copied from csv file)\
                            2.2 product_Agg : This tables will be having 2 columns 1.productName and 2.number of times as                   
                                               it'srepeated count.\
* we can see the tables created from your comandline/terminal with steps below.\
  1.open commandprompt/terminal\
  2.Run sqlite3 <APPLICATION_HOME>large_File_Processor/sqlite/database/test.db \
    note: Replace APPLICATION_HOME with your project directory.\
  3.Run \
      .databases - shows the databases created in that directory. In our case it's the test.db\
      .tables - shows the tables present in the databases, in our cases it shows 2 tables 1.product and 2.product_Agg.\
      
  4.Run the following to see aggregate data.\
      select * from product_Agg;\
      output:\
        Aaron Abbott|1\
        Aaron Acevedo|1\
        Aaron Acosta|4\
        Aaron Adams|6\
        Aaron Aguilar|1\
        Aaron Alexander|2\
        Aaron Allen|5\
        Aaron Allison|1\
        Aaron Alvarado|3\
        Aaron Alvarez|5\
  5.We can also see the overall time taken and performance either in the console or logs 
  # NOTE
  Overall effective learnings from this application is using Oops concepts in very high standards.
  
  # Development Thoughts.
  1. Input file can be read from any external sources like Amazon S3 or Azure blob.
  2. Databases we can use Snowflake.
  3. Develop application that can handle more than one dimension.
  
                                               
