source bin/activate
python freezer.py
cd static
yui-compressor -o styles.css styles.css
cd javascript
for file in *.js; do
    yui-compressor -o $file $file
done
cd ../..
deactivate
