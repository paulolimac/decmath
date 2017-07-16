# Generate wheel
python3 setup.py bdist_wheel

# Upload
twine upload dist/*
