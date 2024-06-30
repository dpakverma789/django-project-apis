echo "======> INSTALLING REQUIREMENTS <======"
pip3 install -r api_requirements.txt
echo "======> REQUIREMENTS INSTALLED <======"

echo "======> COLLECTING STATIC FILES <======"
python3 manage.py collectstatic --noinput --clear
echo "======> STATIC FILES COLLECTED <======"

echo "======> MAKE-MIGRATIONS <======"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
echo "======> MAKE-MIGRATIONS-END <======"