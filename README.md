[![Tests](https://github.com/JoNoteJoMaMa/ckanext-statsCharts/workflows/Tests/badge.svg?branch=main)](https://github.com/JoNoteJoMaMa/ckanext-statsCharts/actions)

# ckanext-statsCharts

Statcharts เป็น extension ของ Ckan ที่ทางคณะผู้จัดทำได้พัฒนาขึ้นมาโดยมีการจัดรูปแบบของ
หน้าเว็บไซต์หลักใหม่ทั้งหมดและมีการเพิ่มฟีเจอร์สรุปผลข้อมูลต่างเพิ่มเข้าไปอาทิเช่น กราฟวงกลมแสดง
ผลข้อมูล เพื่อให้การใช้งาน Opendata ได้สะดวกสะบายมากยิ่งขึ้น



## Requirements

ผู้ใช้ต้องติดตั้ง extension ทั้งหมดที่มีอยู่ในขั้นตอนการติดตั้งของ NECTEC จากเว็บไซต์ GitLab .

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | not tested    |

Suggested values:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

วิธีการติดตั้ง ckanext-statsCharts:

1. เปิดใช้งานโหมด Developer โดยพิมพ์ command ตามด้านล่าง

     . /usr/lib/ckan/default/bin/activate

2. เข้าไปใน path ดังนี้
   
    cd /usr/lib/ckan/default

4. ติดตั้งตัว extension ผ่าน command ด้านล่าง

    pip install -e 'git+https://github.com/JoNoteJoMaMa/ckanext-statscharts#egg=ckanext-statscharts'

5. นำ Statchart ไว้ข้างหน้าสุดของ CKAN.PLUGIN ในไฟล์ ckan.ini

    ckan.plugins = statscharts .....

7. รีโหลดตัว CKAN:

    sudo supervisorctl reload


## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.statscharts.some_setting = some_default_value


## Developer installation

To install ckanext-statsCharts for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/JoNoteJoMaMa/ckanext-statsCharts.git
    cd ckanext-statsCharts
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-statsCharts

If ckanext-statsCharts should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
