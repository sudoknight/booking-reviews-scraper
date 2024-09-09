## 9-September-2024

#### Added
1. Logger can be passed.


## 5-April-2024

#### Added 
1. Added field 'full_review', 'en_full_review' (Combining all the three fields 'review_title', 'review_text_liked', and 'review_text_disliked')

#### Changed
1. Removed translation functionality along with the translated (output fields: 'en_review_title', 'en_review_text_liked', 'en_review_text_disliked')


## 21-Mar-2024

#### Changed
1. Ignore reviews with text: "There are no comments available for this review"


## 20-Mar-2024

#### Added
1. added run_as_module in run.py so that code can be called from third party


## 14-Nov-2023

#### Added
1. added progress printing by starting a new monitoring thread

#### Changed
1. moved language translator object to class level so that it is created once

#### Fixed
1. error in logging (when used in multiprocessing mode)
2. tranlator crashing on emoji
3. avoid translation of punctutaion only or non-alphabetic only strings