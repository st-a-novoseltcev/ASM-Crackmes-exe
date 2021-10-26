reqs:
	pip install -U -r requirements.txt

r2:
	sh check.sh

crack: reqs r2
	nuitka3 --follow-imports crack/crack.py
	rm -r crack.build

clean:
	pip uninstall -r requirements.txt
	rm -rf radare2 
	rm crack.bin
	
	
