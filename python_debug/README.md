- Debugging Techniques
- What is Logging? What is Logger?
- Print vs Logger
- Deep Diving into Logger
- Configuring with Django settings.py
- Developing a visualisation using logger data
- Conclusion


** Debugging Techniques **

Identify -> Analyze -> Remove

- Using outputs statements
- Using Flags
- Comments
- Brute force
- Using Debugging Tools


** What is Logging? What is Logger? **

- Logging: bassically tracking events once a code/software runs. It is very essential for debugging your software.
- Maintaining a log file helps is fixing crashes faster.
- Logger is a build-in python module that allows debugging and recording status messages

** Print vs Logger **

- Print statements works for small scale
- With print statements it's difficult to control the log information one want to capture
- Cannot map the severity level with print statements
- Cannot map the timestamp with the message emitted

** Deep Diving into Logger ** 

- Logger -> A logger is the entry point into the logging system. Is configured to have a log level
- Handler -> Defines the destination of the log record. For example: To a file, Console
- Filter -> Provide a finer grained facility for determining which log records to output
- Formatter -> Specifies layer/entities of record in the output.




** BONUS **
** LOGGER LEVELS **

- DEBUG: Information used for debugging purposes -> logger.debug()
- INFO: General message -> logger.info()
- WARNING: Information used for Minor fault occurrence -> logger.warning()
- ERROR: Information used for Major problem ocurrence -> logger.error()
- CRITICAL: Information used for Critical issue ocurrence -> logger.critical()