F2PY=f2py

demo: example.so
	python fibdemo.py

clean:
	rm -f fib.pyf example.so

fib.pyf: fib.f
	rm -f fib.pyf
	$(F2PY) fib.f -h fib.pyf -m example

example.so: fib.pyf
	$(F2PY) -c fib.pyf fib.f
