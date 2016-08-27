IF NOT EXIST "Scripts\" (
	virtualenv .
	echo %%my_command%% >> Scripts\activate.bat
	set my_command=pip install -r requirements.txt
	Scripts\activate
)
