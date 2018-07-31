python generate-keys.py
nc -l 8554 > oc.bin &
nc -l 8555 > sitebots.bin &
python encrypt-and-decrypt.py

rm *.bin *.pub *.priv
