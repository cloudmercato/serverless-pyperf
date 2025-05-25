#/bin/bash

mkdir package
pip install --target ./package ..

cd package
zip -r ../package.zip .

cd ..
zip package.zip lambda_function.py
