@echo off
@echo ����OCR ����ʶ��
@python %~dp0ggorc.py -i %1
@notepad %1.output.txt