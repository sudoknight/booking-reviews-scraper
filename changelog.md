## 14-Nov-2023

#### Added
1. added progress printing by starting a new monitoring thread

#### Changed
1. moved language translator object to class level so that it is created once

#### Fixed
1. error in logging (when used in multiprocessing mode)
2. tranlator crashing on emoji
3. avoid translation of punctutaion only or non-alphabetic only strings