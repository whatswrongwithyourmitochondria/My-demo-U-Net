# My-demo
**U2-Net: U Square Net**
- official repo of U2-Net: https://github.com/xuebinqin/U-2-Net
- In this demo U2-Net is used for portrait drawing

**Virtual environment was created with the help of *poetry*:**
- to install *poetry* according to your OS visit: https://python-poetry.org/docs/
- if you install *poetry* using **pip**, be aware that it will also install Poetry’s dependencies which might cause conflicts with other packages


**Task 1**

**Follow these steps to run the project:**
 1. Go to My-demo directory
 2. Activate virtual envirnonment with `poetry run`
 3. Run `python demo.py` (can be different according to your OS)
 4. You will see the result of portrait drawing based on the test photo
 5. Then press *exit* to leave the shell
 
 
**Task 2**

**To be able to build a package from the code:**
1. `poetry build`
2. cd ./dist
3. pip install <source file> (`pip install demo-0.1.0.tar.gz`)
4. to watch demo you can run `python demo.py`

**USE** `pip install git+https://github.com/whatswrongwithyourmitochondria/My-demo`
to install a package from the console 

**Task 3**

 - Styling tools such as *black* and *pylint* were added.
 - *pre-commit* tool is used while making commits and has been configured to use styling tools mentioned above. 

 - to install all the necessary packages, run `poetry install`

**Before commit**

 * to format the code with the help of *black* tool, run `black demo.py`
 * to check the list of errors with the help of *pylint* tool, run `pylint demo.py`

 to run all style checking tools at once:
 
 - once run `pre-commit install .`
 - every time you want to check your code with help of all styling tools, run `pre-commit run -a`

 After you fix all the errors, make *git add / git commit* commands again. 

 **Task 4**

 In this task 2 tests are added:
  - visual regression test, that checks our results are always the same
  - a "no error" test, that shows our algorithm works with the images of different sizes
  
 To check how CI works, follow the link below:

https://github.com/whatswrongwithyourmitochondria/My-demo/actions

CI installs dependencies, runs style checks (with the help of pre-commit that hooks *black* and *pylint* tools), tests code with pytest 
and then makes build and pushes it to the Artifacts.

You can also check artifacts selecting job in actions, e.g.:

https://github.com/whatswrongwithyourmitochondria/My-demo/runs/6675396697

You can scroll down and see Artifacts section. If needed, you can download a .zip archive:

<img src="https://github.com/whatswrongwithyourmitochondria/My-demo/blob/main/artifact.png" width="700"/>

**Task 5**

**Web Demo for the project:**

Web Demo is created with help of *streamlit* library. It is a single page application that takes 
image from a user and executes the demo code to draw the results in the browser. 

You can find *web_demo.py* script in the */demo* folder.
In order to run this app, install the package (use local version of */dist* folder) and then type `streamlit run web_demo.py` in */demo* folder. 

Streamlit app will work at localhost:8501.

You can choose .png image on your own and upload it.

**Docker image**

First, you need to install *Docker* to your system.

Second, run `docker build -t unet ./`

After building, use the following command

`docker run -p 8501:8501 unet`

and you'll see a web demo at *localhost:8501*








