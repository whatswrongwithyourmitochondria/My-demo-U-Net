# My-demo
**U2-Net: U Square Net**
- official repo of U2-Net: https://github.com/xuebinqin/U-2-Net
- In this demo U2-Net is used for portrait drawing

**Virtual environment was created with the help of *poetry*:**
- to install *poetry* according to your OS visit: https://python-poetry.org/docs/
- if you install *poetry* using **pip**, be aware that it will also install Poetry’s dependencies which might cause conflicts with other packages

**Follow these steps to run the project:**
 1. Go to My-demo directory
 2. Activate virtual envirnonment with *poetry run*
 3. Run python demo.py (can be different according to your OS)
 4. You will see the result of portrait drawing based on the test photo
 5. Then press *exit* to leave the shell
 
**To be able to build a package from the code:**
1. *poetry build*
2. cd ./dist
3. pip install <source file> (pip install demo-0.1.0.tar.gz)
4. to watch demo you can run *python demo.py*
