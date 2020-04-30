## Function:
this module make it easy for any python script recorde results after some time-consuming task;
so if some unpredictable errors happened and crashed your script, it can pass the funcs that has already 
successfully finished, just begin from the breakpoint;

## Method:
a.  before run your task,import this module, and at the fist run step --  Brestart.preRunCheck() ;
check if something wrong ,and wether it needs breakpoint restart;    
b.  use @Brestart.logFunc to decorate the functions that cost much time,make it a recorde point;    
c.  finally Brestart.end() at the last run step ,can clear temp log and do not affect next run.     