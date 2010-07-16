all: ui_phed.py

clean:
	rm *.pyc ui_*.py

ui_phed.py : phed.ui
	pyuic4 phed.ui > ui_phed.py 
