Note:
=========

api.py is for generate python API for notepad++. 
And it can also generate other luanguage API.
To use Python API, Place python.xml under you notepad++ APIs path.
My is E:\Program Files\Notepad++\plugins\APIs.

Now include:
Python.xml
Processing.xml
Arduino.xml
c_py.xml

To use Processing and Arduino, you should define the luanguage as userDefineLang first.
rename userDefineLang_processing_arduino.xml to userDefineLang.xml.
And put it under the path ...\Notepad++\ .
If you have other luangage defined, copy the content to userDefineLang.xml use its format.
the copy the processing.xml or arduino.xml to ...\Notepad++\plugins\APIs.

c_py.xml is Python C API, copy it to c.xml to use it .

Make sure you have enabled auto complete in npp.

theme:put the Monokai.xml into ...\Notepad++\themes.

You can generate your language API too! See more detail in api.py

Require
=======
python 2.7
jinja2

if you already have django or flask. You must already have jinja.

My email:sadnoodles@gmail.com

中文说明
=========

api.py 用来生成Notepad++需要的python api文件python.xml的。
也可以用来生成其他语言的API文件，只要稍加修改就行。
复制到notepad++ 安装路径下的APIs文件夹下
我的是：E:\Program Files\Notepad++\plugins\APIs

现有的API：
Python.xml
Processing.xml
Arduino.xml
c_py.xml

Processing 和 Arduino:
使用这些语言需要先在用户定义语言中添加它们。
将 userDefineLang_processing_arduino.xml 重命名为 userDefineLang.xml.
然后复制到 ...\Notepad++\目录下。
如果你已经自定义过其他语言，那么将内容复制过去，要按照里面的样式。
然后复制processing.xml或arduino.xml到 ...\Notepad++\plugins\APIs目录下.

c_py.xml是Python C API。将其内容添加到C语言的c.xml中即可使用。

附上一个theme，Monokai.xml。非常漂亮。
我修改了一点python有关的，版权归原作者。

将theme复制到...\Notepad++\themes目录下即可使用了.

你也可以为自己使用的语言生成API！了解更多请看api.py。

依赖项
=======
python 2.7
jinja2 

如果你使用django 或者flask ,它们用的模板引擎就是jinja.所以也可以用它们的render。