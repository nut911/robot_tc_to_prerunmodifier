# RobotFramework Prerunmodified to Set Timeout for Testcases

## Description
Adds possibility to provide commandline configurable timeout value for executed RobotFramework testcases.

## Usage

### Robot
```
$ robot --pythonpath `pwd` --prerunmodifier tc_timeout.SetTimeout:"4 seconds" tc_timeout_test.robot
```

### Pabot
```
$ pabot --pabotlib --processes 10 --verbose --pythonpath `pwd` --prerunmodifier tc_timeout.SetTimeout:"4 seconds" tc_timeout_test.robot
```

## Result
```
==============================================================================
Tc Timeout Test                                                               
==============================================================================
Prerunmodifier Timeout Test                                           | FAIL |
Test timeout 4 seconds exceeded.
------------------------------------------------------------------------------
Fail
Tc Timeout Test                                                       | FAIL |
1 critical test, 0 passed, 1 failed
1 test total, 0 passed, 1 failed
==============================================================================
```
