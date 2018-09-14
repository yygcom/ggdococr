@echo off
@echo 正在OCR 文字识别
@python %~dp0ggorc.py -i %1
@notepad %1.output.txt