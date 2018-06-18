# moodle_BOT

## 介紹

能自動把將moodle上的程式作業拉下來，然後自動編譯，自動比對輸出，接著比對是否抄襲。

## 適用對象

學校程式作業用moodle作為繳交平台，身為助教的你負責批改程式作業。

## 系統需求

- python3
  - beautifulsoup4
- JDK
- Bash

### 使用方式

1. clone

2. 編輯`get_homework.py`裡面的85,87行 填入您的moodle帳號密碼(必須為助教身份)

3. 執行`python3 get_homework.py` 依照提示把作業拉下來

4. 編輯`do_it.sh` 20~24行中區塊

```
#setting main class file#############
TARGET=CalScore
INPUTPWD=../../input/hw1.txt
ANSPWD=../../output/hw1_ans.txt
#####################################
```

TARGET 請填入Main class名稱(進入點)
INPUTPWD 請填入測資路徑 (建議放到input資料夾中)
ANSPWD 請填入答案檔案路徑 (建議放到output資料夾中)

5. 修改完畢後直接執行`do_it.sh`
