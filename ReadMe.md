Note:
=========

api.py is for generate python API for notepad++. 
Place python.xml under you notepad++ APIs path.
My is E:\Program Files\Notepad++\plugins\APIs.

to use Processing and Arduino, you should define the luanguage as userDefineLang first.
rename userDefineLang_processing_arduino.xml to userDefineLang.xml.
And put it under the path ...\Notepad++\ .
If you have other luangage defined, copy the content to userDefineLang.xml use its format.
the copy the processing.xml or arduino.xml to ...\Notepad++\plugins\APIs.

enable auto complete in npp.

theme:put the Monokai.xml into ...\Notepad++\themes.

You can generate your language API too! See more detail in api.py

Require
=======
python 2.7
jinja2

if you already have django or flask. You must already have jinja.

My email:sadnoodles@gmail.com

����˵��
=========

api.py ��������Notepad++��Ҫ��python api�ļ�python.xml��
���Ƶ�notepad++ ��װ·���µ�APIs�ļ�����
�ҵ��ǣ�E:\Program Files\Notepad++\plugins\APIs

Processing �� Arduino:
ʹ����Щ������Ҫ�����û�����������������ǡ�
�� userDefineLang_processing_arduino.xml ������Ϊ userDefineLang.xml.
Ȼ���Ƶ� ...\Notepad++\Ŀ¼�¡�
������Ѿ��Զ�����������ԣ���ô�����ݸ��ƹ�ȥ��Ҫ�����������ʽ��
Ȼ����processing.xml��arduino.xml�� ...\Notepad++\plugins\APIsĿ¼��.



����һ��theme��Monokai.xml���ǳ�Ư����
���޸���һ��python�йصģ���Ȩ��ԭ���ߡ�

��theme���Ƶ�...\Notepad++\themesĿ¼�¼���ʹ����.

��Ҳ����Ϊ�Լ�ʹ�õ���������API���˽�����뿴api.py��

������
=======
python 2.7
jinja2 

�����ʹ��django ����flask ,�����õ�ģ���������jinja.����Ҳ���������ǵ�render��